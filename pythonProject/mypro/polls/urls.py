
from django.contrib import admin
from django.urls import path

import polls.views

app_name = 'polls'
urlpatterns = [
    path('', polls.views.index),
    path('admin/', admin.site.urls),
    path('generic.html', polls.views.generic),
]
