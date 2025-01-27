from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

# Para modelo categoria
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Para modelo post
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
