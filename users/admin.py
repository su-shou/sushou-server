from django.contrib import admin

from .models import wxUser, wxUserLog

admin.site.register(wxUser)
admin.site.register(wxUserLog)