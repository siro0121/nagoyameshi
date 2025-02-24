from django.contrib import admin
from .models import restaurant, Category
from django.utils.safestring import mark_safe


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","name","category", "img")

    def image(self, obj):
        return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(restaurant, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
