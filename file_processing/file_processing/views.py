from django.shortcuts import render, redirect
from .models import File
from .forms import FileUploadForm

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'upload_file.html', {'form': form})

def file_list(request):
    files = File.objects.all()
    return render(request, 'file_list.html', {'files': files})

def view_file(request, file_id):
    file = File.objects.get(id=file_id)
    if file.file.name.endswith('.txt'):
        editable = True
    else:
        editable = False
    return render(request, 'view_file.html', {'file': file, 'editable': editable})