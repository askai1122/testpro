from django.apps import AppConfig


class WillflyyConfig(AppConfig):
    name = 'willflyy'

    def ready(self):
    	

        import users.signals