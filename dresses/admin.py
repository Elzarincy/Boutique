from django.contrib import admin

# Register your models here.
from dresses.models import kurta, kurtaset, saree, jewellery, top, handbag


#class productAdmin(admin.ModelAdmin):
 #   list_display = ('image','name','description','price')

admin.site.register(kurta)
admin.site.register(kurtaset)
admin.site.register(saree)
admin.site.register(top)
admin.site.register(jewellery)
admin.site.register(handbag)

