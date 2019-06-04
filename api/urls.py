from django.urls import path
from .views.namespace import *
from .views.swaggerjson import *
from .views.project import *



urlpatterns = [
    path('namespaces/', namespaces),
    path('namespace/', namespace),
    path('swagger.json/', swagger_json),
    path('<str:namespace>/project', project),
    path('<str:namespace>/projects', projects),
]


