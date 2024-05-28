from django.contrib import admin
from .models import MedicalInstitution, Patient, Doctor


@admin.register(MedicalInstitution)
class MedicalInstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'description', 'created_at', 'updated_at')
    search_fields = ['name', 'address']
    list_filter = ['created_at', 'updated_at']


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'medical_institution', 'date_of_birth', 'gender', 'created_at', 'updated_at')
    search_fields = ['user__username', 'medical_institution__name']
    list_filter = ['created_at', 'updated_at']

    def get_username(self, obj):
        return obj.user.username if obj.user else ''

    get_username.short_description = 'Username'


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('get_speciality', 'medical_institution', 'get_username', 'created_at', 'updated_at')
    search_fields = ['user__username', 'medical_institution__name']
    list_filter = ['created_at', 'updated_at']

    def get_speciality(self, obj):
        return obj.speciality

    get_speciality.short_description = 'Speciality'

    def get_username(self, obj):
        return obj.user.username if obj.user else ''

    get_username.short_description = 'Username'

