from django.apps import AppConfig


class MetadataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'metadata'

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
