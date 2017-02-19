from django.contrib import admin

# Register your models here.
from .models import Kyoten, Nori

admin.site.register([Kyoten, Nori])
