from django.urls import path
from main import views

urlpatterns = [
    path('new' ,views.new_post),
    path('',views.list_posts),

]