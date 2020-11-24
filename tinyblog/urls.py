from django.urls import path
from . import views


app_name = 'tinyblog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('entry/<int:pk>', views.DetailView.as_view(), name='entry'),
    path('add/', views.CreateView.as_view(), name='add'),
    path('edit/<int:pk>', views.EditView.as_view(), name='edit'),
]
