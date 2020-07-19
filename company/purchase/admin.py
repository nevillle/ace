from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered


app_models = apps.get_app_config('purchase').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
