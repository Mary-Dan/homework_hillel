from django.apps import AppConfig

class ConsultationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'consultation'

    def ready(self):
        import med_consultation.consultation.signals

