from.import views
from django.urls import path
urlpatterns =[
    path('',views.fun7,name="fun7"),
    path('movie/<int:movie_id>/',views.fundetails,name="fundetails")
]