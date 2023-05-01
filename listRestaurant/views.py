from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from bs4 import BeautifulSoup
import requests


# Create your views here.

class RestaurantView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request):
        req = requests.get('https://www.bestrestaurantsmaroc.com/fr/recherche/ville/casablanca.html')
        soup = BeautifulSoup(req.content, 'html5lib')
        imagesA = []
        imagesI = []
        cuisines = []
        nom = []
        meals = []
        image = soup.find('div', attrs={'id': 'restaurants'}).find_all('div', attrs={
            'class': 'filterData rs-container br-bg-grey'})
        for row in image:
            imagesA.append("https://www.bestrestaurantsmaroc.com/" + row.a['href'])
            imagesI.append(row.img['src'])

        cuisine = soup.find('div', attrs={'id': 'restaurants'}).find_all('div', attrs={'class': 'rs-cuisine rs-info'})
        for row in cuisine:
            cuisines.append(row.a.text)

        noms = soup.find('div', attrs={'id': 'restaurants'}).find_all('div', attrs={'class': 'filterData rs-container br-bg-grey'})
        for row in noms:
            nom.append(row.h3.text)

        for i in range(len(imagesA)):
            req2 = requests.get(imagesA[i])
            soup2 = BeautifulSoup(req2.content, 'html5lib')

            prixx = soup2.find('div', attrs={'class': 'rs-main-column'}).find('div', attrs={'class': 'rs-menu-section menus-et-formules'}).find('div', attrs={'class': 'rs-menu-item'}).find('span', attrs={'class': 'rs-menu-price'}).text
            phones =soup2.find('div', attrs={'class': 'modal-dialog'}).find('div' ,attrs={'class' : 'modal-content'}).find('div' ,attrs={'class' : 'modal-body'}).find('div' ,attrs={'class' : 'restaurant-modal-info-main'}).text
            webs = soup2.find('div', attrs={'class': 'rs-contact'}).find('div', attrs={'class': 'rs-address'}).text
            addresse1 = soup2.find('div', attrs={'class': 'rs-contact'}).find('div', attrs={'class': 'rs-address'}).find('span')
            addresse2 = soup2.find('div', attrs={'class': 'rs-contact'}).find('div', attrs={'class': 'rs-address'}).find('span', attrs={'itemprop': 'streetAddress'})
            addresses = (addresse1.text + addresse2.text)
            menus = soup2.find('div', attrs={'class': 'rs-menu-section'}).find_all('div',attrs=('class', 'rs-menu-item'))
            for row in menus:
                meals.append(row.span.text)
            Restaurant.objects.create(
                imagesA=imagesA[i],
                imagesI=imagesI[i],
                cuisines=cuisines[i],
                nom=nom[i],
                prix=prixx,
                phone=phones,
                web=webs,
                adresse=addresses,
                menu=meals
            )
        return Response({'message': 'Data saved successfully.'})


class RestaurantListView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
