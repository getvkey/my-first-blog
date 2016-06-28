from django.contrib import admin
from TestModel.models import Test,Contact,Tag

admin.site.register([Test,Contact,Tag])