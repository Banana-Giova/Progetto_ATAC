from django.contrib import admin
from .models import *

admin.site.register(Passenger)
admin.site.register(Line)
admin.site.register(Stop)
admin.site.register(Bus)
admin.site.register(Driver)

admin.site.register(OrdinATAC)
admin.site.register(LiveTrATAC)
admin.site.register(MultiDriver)