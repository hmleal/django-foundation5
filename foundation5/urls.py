from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.FormView.as_view(), name='forms'),
]
