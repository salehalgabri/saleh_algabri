from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class PatientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patients'
class SuitConfig(DjangoSuitConfig):
    layout='horizontal'
    # layout='vertical'