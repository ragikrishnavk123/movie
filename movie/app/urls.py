from django.urls import path
from app import views
app_name="app"

urlpatterns = [

    # path('',views.home,name="home"),
    path('',views.Movielist.as_view(),name="home"),

    # path('details/<p>',views.details,name="details"),
    path('movie/<pk>',views.MovieDetail.as_view(),name="details"),

    path('addmovie/',views.Movieadd.as_view(),name="addmovie"),
    # path('update/<p>', views.update, name="update"),
    path('update/<pk>',views.MovieUpdate.as_view(),name='update'),

    # path('delete/<p>', views.delete, name="delete"),
    path('delete/<pk>', views.MovieDelete.as_view(), name="delete"),

]