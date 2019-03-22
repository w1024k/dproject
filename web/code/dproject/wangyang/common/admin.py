from django.contrib import admin

# Register your models here.

from common.models import UrlVisitCount, DailyCount, OpenUser, Profile
admin.site.register(UrlVisitCount)
admin.site.register(DailyCount)
admin.site.register(OpenUser)
admin.site.register(Profile)

