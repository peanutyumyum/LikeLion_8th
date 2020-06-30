from django.contrib import admin
from .models import Orders, members, Goods, Sheets

# Register your models here.

admin.site.register(Orders)
admin.site.register(members)
admin.site.register(Goods)
admin.site.register(Sheets)