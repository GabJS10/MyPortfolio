from django.urls import path, include
from portfolio import views
app_name='portfolio'
urlpatterns = [
    path('',views.home,name='home'),
    path('projects/',views.ViewProjects.as_view(),name='projects'),
    path('detail/<slug>/',views.DetailViewProject.as_view(),name='detail'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('filter/<int:pk>/',views.FilterViewProjects.as_view(),name='filter'),

]