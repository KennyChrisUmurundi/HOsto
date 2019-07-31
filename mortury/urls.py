from django.urls import path
from . import views as mortury_views
from django.conf.urls.static import static


app_name = 'mortury'
urlpatterns = [
path('scan/',mortury_views.scancode,name="scan"),
path('patient/<slug:code>',mortury_views.deadpatient,name="deadpatient"),
path('list/',mortury_views.list,name="listOfDead"),

]
