from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menus/', views.MenuListView.as_view(), name='menus'),
    path('menu/<int:pk>', views.MenuDetailView.as_view(), name='menu-detail'),
    path('categories/', views.CategoryListView.as_view(), name='category'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success')
]
