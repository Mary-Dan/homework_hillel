from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Chat, Message, User
from .forms import ChatForm, MessageForm, AddUserForm, EditMessageForm, DeleteMessageForm, DeleteUserForm
from django.contrib.auth.models import User
from django.http import JsonResponse


def get_user_status(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                user_status = {'status': 'online' if user.is_online() else 'offline'}
                return JsonResponse(user_status)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)



@login_required
def chats(request):
    chats = request.user.chats.all()
    return render(request, 'messenger/chats.html', {'chats': chats})


@login_required
def chat(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    if request.user not in chat.users.all():
        return redirect('chats')
    messages = chat.messages.all().order_by('created_at')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.chat = chat
            message.save()
            return redirect('chat', chat_id=chat.id)
    else:
        form = MessageForm()
    return render(request, 'messenger/chat.html', {'chat': chat, 'messages': messages, 'form': form})


@login_required
def create_chat(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.users.add(request.user)
            chat.save()
            return redirect('chats')
    else:
        form = ChatForm()
    return render(request, 'messenger/create_chat.html', {'form': form})


@login_required
def add_user(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    if request.user != chat.author:
        return redirect('chat', chat_id=chat.id)
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            chat.users.add(user)
            return redirect('chat', chat_id=chat.id)
    else:
        form = AddUserForm()
    return render(request, 'messenger/add_user.html', {'chat': chat, 'form': form})


@login_required
def edit_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, author=request.user)
    if request.method == 'POST':
        form = EditMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('chat', chat_id=message.chat.id)
    else:
        form = EditMessageForm(instance=message)
    return render(request, 'messenger/edit_message.html', {'form': form, 'message': message})


@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, author=request.user)
    if request.method == 'POST':
        message.delete()
        return redirect('chat', chat_id=message.chat.id)
    return render(request, 'messenger/delete_message.html', {'message': message})


def delete_user(request, chat_id, user_id):
    chat = get_object_or_404(Chat, id=chat_id, author=request.user)
    user = get_object_or_404(get_user_model(), id=user_id)
    if request.user != chat.author and request.user != user:
        return redirect('chat', chat_id=chat.id)
    if request.method == 'POST':
        form = DeleteUserForm(request.POST)
        if form.is_valid():
            chat.users.remove(user)
            chat.save()
            return redirect('chat', chat_id=chat.id)
    else:
        form = DeleteUserForm(initial={'username': user.username})
    return render(request, 'messenger/delete_user.html', {'chat': chat, 'user': user, 'form': form})