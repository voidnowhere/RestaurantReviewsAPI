from django.urls import path

from scrapping.views import ScrapView

urlpatterns = [
    path('', ScrapView.as_view(), name="scrapping"),
]
