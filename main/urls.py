from django.urls import path
from .views import main_index,main_view_post,main_about,main_cat

app_name="main"

urlpatterns = [
	path('',main_index,name="index"),
	path('view/<int:id>/',main_view_post,name="view"),
	path('products/',main_about,name="about"),
	path('cat/<int:id>/',main_cat,name="cat")
]