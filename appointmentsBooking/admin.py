from django.contrib import admin
from .models import Practioner, Clients, Appointmentsdetail,Recommendation,Calenderslots
# Register your models here.

admin.site.register(Practioner)
admin.site.register(Clients)
admin.site.register(Appointmentsdetail)
admin.site.register(Recommendation)
admin.site.register(Calenderslots)
