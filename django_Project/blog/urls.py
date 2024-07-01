from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('post/<str:judulurl>',views.slugyfy,name="detail"),
    path('category/<str:categoryurl>',views.category,name="category")
]