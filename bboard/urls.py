from django.contrib import admin
from django.urls import path,include
from .views import by_rubric, BbCreateView, BbDetailView, BbEditView, BbDeleteView, BbIndexView

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', BbCreateView.as_view(), name="add"),
    path('detail/<int:pk>', BbDetailView.as_view(), name="detail"),
    path('update/<int:pk>', BbEditView.as_view(), name="update"),
    path('delete/<int:pk>', BbDeleteView.as_view(), name="delete"),
    path('', BbIndexView.as_view(), name='main'),
]
