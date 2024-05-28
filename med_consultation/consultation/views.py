from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from med_consultation.consultation.serializers import ConsultationSerializer
from .models import MedicalInstitution, Patient, Doctor, Consultation
from .forms import ConsultationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from rest_framework import permissions, generics
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render, redirect
from .models import File
from .forms import FileForm


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


def user_login(request):
    """Обработка запроса на вход пользователя."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('consultation_list')
    else:
        form = AuthenticationForm()
    return render(request, 'consultation/login.html', {'form': form})


def user_signup(request):
    """Обработка запроса на регистрацию пользователя."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('consultation_list')
    else:
        form = UserCreationForm()
    return render(request, 'consultation/signup.html', {'form': form})


@login_required
def user_profile(request):
    """Отображение профиля пользователя."""
    return render(request, 'consultation/profile.html')


@login_required
def consultation_list(request):
    """Отображение списка консультаций."""
    patient = request.user.patient
    consultations = Consultation.objects.filter(patient=patient)
    paginator = Paginator(consultations, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'consultation/consultation_list.html', {'consultations': page_obj})


@login_required
def consultation_detail(request, consultation_id):
    """Отображение деталей консультации."""
    consultation = get_object_or_404(Consultation, id=consultation_id)
    return render(request, 'consultation/consultation_detail.html', {'consultation': consultation})


@login_required
def create_consultation(request):
    """Создание новой консультации."""
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.patient = request.user.patient
            consultation.save()
            messages.success(request, 'Consultation created successfully!')
            return redirect('consultation_list')
    else:
        form = ConsultationForm()
    return render(request, 'consultation/create_consultation.html', {'form': form})


@login_required
def edit_consultation(request, consultation_id):
    """Редактирование консультации."""
    consultation = get_object_or_404(Consultation, id=consultation_id)
    if request.method == 'POST':
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consultation updated successfully!')
            return redirect('consultation_list')
    else:
        form = ConsultationForm(instance=consultation)
    return render(request, 'consultation/edit_consultation.html', {'form': form})


@login_required
def delete_consultation(request, consultation_id):
    """Удаление консультации."""
    consultation = get_object_or_404(Consultation, id=consultation_id)
    if request.method == 'POST':
        consultation.delete()
        messages.success(request, 'Consultation deleted successfully!')
        return redirect('consultation_list')
    return render(request, 'consultation/delete_consultation.html', {'consultation': consultation})


class ConsultationListAPIView(generics.ListAPIView):
    """Представление API для получения списка консультаций."""
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination


class IsPatientOrReadOnly(permissions.BasePermission):
    """
    Пользовательское разрешение, позволяющее только пациентам редактировать свои консультации.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение для всех
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешаем доступ только пациентам, привязанным к консультации.
        return obj.patient == request.user.patient


class ConsultationListCreateAPIView(generics.ListCreateAPIView):
    """Представление API для создания и получения списка консультаций."""
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user.patient)


class ConsultationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Представление API для получения, обновления и удаления консультации."""
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [IsPatientOrReadOnly]


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'upload_file.html', {'form': form})


def file_list(request):
    files = File.objects.filter(user=request.user)
    return render(request, 'file_list.html', {'files': files})


def file_detail(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    content = None
    if file.file.name.endswith('.txt'):
        with open(file.file.path, 'r') as f:
            content = f.read()
    return render(request, 'file_detail.html', {'file': file, 'content': content})