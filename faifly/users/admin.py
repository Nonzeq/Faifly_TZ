from wagtail.contrib.modeladmin.options import modeladmin_register,ModelAdmin

from users.models import User


class UserAdmin(ModelAdmin):
    model = User
    list_display = ['id','username', 'first_name', 'last_name', 'role',]
    list_display_links = ('id', 'nameLocation')
    search_fields = ('first_name', 'last_name', 'role','username')

modeladmin_register(UserAdmin)