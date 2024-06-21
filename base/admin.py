from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Passenger)
admin.site.register(Line)
admin.site.register(Stop)
admin.site.register(OrdinATAC)
admin.site.register(Bus)
admin.site.register(Driver)