from django.apps import AppConfig # importing the AppConfig, which is used to configure applications in Django


class ArticlesConfig(AppConfig): # configuration class for the "articles" application
    default_auto_field = 'django.db.models.BigAutoField' # setting the type of field that will be automatically used to create primary keys (ID)
    name = 'articles' # app name
