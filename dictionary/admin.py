from django.contrib import admin

# Register your models here.
from .models import Meta, Clause, Lemma

admin.site.register(Meta)
admin.site.register(Clause)
admin.site.register(Lemma)