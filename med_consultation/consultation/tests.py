from django.test import TestCase
from .forms import ConsultationForm, CustomUserCreationForm
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Consultation, MedicalInstitution, Patient, Doctor


# forms
class ConsultationFormTestCase(TestCase):
    def test_valid_consultation_form(self):
        form_data = {'doctor': 1, 'date': '2024-05-27', 'duration': 60, 'description': 'Test description'}
        form = ConsultationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_consultation_form(self):
        form = ConsultationForm(data={})
        self.assertFalse(form.is_valid())


class CustomUserCreationFormTestCase(TestCase):
    def test_valid_user_creation_form(self):
        form_data = {'username': 'testuser', 'password1': 'testpassword123', 'password2': 'testpassword123'}
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_user_creation_form(self):
        form_data = {'username': 'testuser', 'password1': 'testpassword123', 'password2': 'differentpassword'}
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())


#API
class ConsultationAPITestCase(APITestCase):
    def setUp(self):
        self.consultation = Consultation.objects.create(patient_id=1, doctor_id=1, medical_institution_id=1, date="2024-05-27", duration=60)

    def test_consultation_list_api_view(self):
        url = reverse('api_consultation_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_consultation_create_api_view(self):
        url = reverse('api_consultation_list')
        data = {'patient': 1, 'doctor': 1, 'medical_institution': 1, 'date': '2024-05-28', 'duration': 30}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_consultation_detail_api_view(self):
        url = reverse('api_consultation_detail', kwargs={'pk': self.consultation.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# models
class ConsultationModelTestCase(TestCase):
    def test_consultation_creation(self):
        consultation = Consultation.objects.create(patient_id=1, doctor_id=1, medical_institution_id=1, date="2024-05-27", duration=60)
        self.assertIsInstance(consultation, Consultation)
        self.assertEqual(consultation.patient_id, 1)
        self.assertEqual(consultation.doctor_id, 1)
        self.assertEqual(consultation.medical_institution_id, 1)
        self.assertEqual(consultation.date, "2024-05-27")
        self.assertEqual(consultation.duration, 60)


class MedicalInstitutionModelTestCase(TestCase):
    def test_medical_institution_creation(self):
        institution = MedicalInstitution.objects.create(name="Test Hospital", address="123 Test St", description="A test hospital")
        self.assertIsInstance(institution, MedicalInstitution)
        self.assertEqual(institution.name, "Test Hospital")
        self.assertEqual(institution.address, "123 Test St")
        self.assertEqual(institution.description, "A test hospital")


class PatientModelTestCase(TestCase):
    def test_patient_creation(self):
        patient = Patient.objects.create(date_of_birth="2000-01-01", gender="M")
        self.assertIsInstance(patient, Patient)
        self.assertEqual(patient.date_of_birth, "2000-01-01")
        self.assertEqual(patient.gender, "M")


class DoctorModelTestCase(TestCase):
    def test_doctor_creation(self):
        doctor = Doctor.objects.create(speciality="Cardiologist")
        self.assertIsInstance(doctor, Doctor)
        self.assertEqual(doctor.speciality, "Cardiologist")