from django.contrib import admin

from boards.models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass
