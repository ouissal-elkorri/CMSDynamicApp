from django.contrib import admin
from .models import Application, Menu_element, Sous_menu, Block_article

# Register your models here.


class ProjetAdmin(admin.ModelAdmin):
    list_display = ('id', 'intitule')


admin.site.register(Application, ProjetAdmin)
admin.site.register(Menu_element, ProjetAdmin)
admin.site.register(Sous_menu, ProjetAdmin)
admin.site.register(Block_article, ProjetAdmin)
