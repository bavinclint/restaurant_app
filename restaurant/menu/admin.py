from django.contrib import admin

# Register your models here.
from .models import Menu, Category

#admin.site.register(Menu)
#admin.site.register(Category)

# Register the Admin classes for Book using the decorator
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')

# Register the Admin classes for BookInstance using the decorator
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

