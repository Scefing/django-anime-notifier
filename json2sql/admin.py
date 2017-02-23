import json

from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.shortcuts import render

from .forms import JsonUploadForm
from .models import Json, Show

# Register your models here.


class CustomAdminSite(AdminSite):

    def get_urls(self):
        urls = super(CustomAdminSite, self).get_urls()
        my_urls = [
            url(r'^json_upload/$', self.admin_view(self.json_upload_view)),
        ]
        return my_urls + urls

    def json_upload_view(self, request):
        if request.method == 'POST':
            form = JsonUploadForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print("error!")

        else:
            form = JsonUploadForm()

            request.current_app = self.name
            return render(request, 'json2sql/sometemplate.html', {'form': form})

#admin_site = CustomAdminSite()

#admin_site.register(Json)
#admin_site.register(Show)

admin.site.register(Show)
admin.site.register(Json)
