from django.contrib import admin
from .models import fileupload, youthpost,January,Feburary,March,April,May,June,July,August,September,October,November,December
from .models import audioMessage, pastorsCorner
# Register your models here.
admin.site.register(youthpost)
admin.site.register(January)
admin.site.register(Feburary)
admin.site.register(March)
admin.site.register(April)
admin.site.register(May)
admin.site.register(June)
admin.site.register(July)
admin.site.register(August)
admin.site.register(September)
admin.site.register(October)
admin.site.register(November)
admin.site.register(December)
admin.site.register(fileupload)
admin.site.register(audioMessage)
admin.site.register(pastorsCorner)

