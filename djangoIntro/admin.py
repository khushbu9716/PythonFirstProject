from django.contrib import admin
from djangoIntro.models import User, Product

# admin.site.register(User)
# admin.site.register(Product)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email']
    list_display = ['id','username', 'email']
    search_fields = ['username']
