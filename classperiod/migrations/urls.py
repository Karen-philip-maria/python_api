from  django.urls import path
from .views import classperiodListView



urlpatterns=[
    path("classperiod/".classperiodListView.as_view(), names="classperiod_list_view")
]