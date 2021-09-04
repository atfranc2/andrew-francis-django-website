from django.urls import path
from . import views

# Import into the website urls always end rountes with a forward slash
urlpatterns = [
    path('hello/', views.say_hello)
]
