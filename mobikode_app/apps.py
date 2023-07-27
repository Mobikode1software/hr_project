from django.apps import AppConfig


class MobikodeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mobikode_app'
    
    def ready(self):
        # Import and connect signals here
        import mobikode_app.models 
