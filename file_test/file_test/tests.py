from django.test import TestCase, Client
from django.urls import reverse
from .models import File
from .forms import FileUploadForm

class FileModelTestCase(TestCase):
    def test_file_creation(self):
        file = File.objects.create(name='test_file', file='path/to/your/test/file.txt')
        self.assertEqual(File.objects.count(), 1)
        self.assertEqual(file.name, 'test_file')
        self.assertTrue(file.file.name.endswith('.txt'))

class FileUploadFormTestCase(TestCase):
    def test_file_upload_form(self):
        form_data = {'name': 'test_file', 'file': 'path/to/your/test/file.txt'}
        form = FileUploadForm(data=form_data)
        self.assertTrue(form.is_valid())

class FileViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_upload_file_view_GET(self):
        response = self.client.get(reverse('upload_file'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload_file.html')

    def test_upload_file_view_POST(self):
        with open('path/to/your/test/file.txt', 'rb') as file:
            response = self.client.post(reverse('upload_file'), {'file': file})
        self.assertEqual(response.status_code, 302)

    def test_file_list_view(self):
        response = self.client.get(reverse('file_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'file_list.html')

