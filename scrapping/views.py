import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.views import View

from restaurants.models import Restaurant

urls = [
    {
        'name': 'bestrestaurantsmaroc',
        'url': 'https://www.bestrestaurantsmaroc.com/en/',
    },
]


class ScrapView(View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect('/admin/')

        return render(request, 'index.html', {'urls': urls})

    def post(self, request):
        if not request.user.is_superuser:
            return redirect('/admin/')

        index = request.POST.get('url')
        website_url = (urls[int(index)].get('url'))
        if website_url == 'https://www.bestrestaurantsmaroc.com/en/':
            website_url_without_language_code = website_url.split('/en/')[0]

            website_soup = BeautifulSoup(requests.get(website_url).content, 'html.parser')

            cities_divs = website_soup.select_one('.city-categories-slideshow > .swiper-wrapper').find_all('div')
            for cityDiv in cities_divs:
                city_name = cityDiv.find('h3').get_text()
                city_restaurants_url = website_url_without_language_code + cityDiv.find('a')['href']
                restaurants_soup = BeautifulSoup(requests.get(city_restaurants_url).content, 'html.parser')
                restaurants_divs = restaurants_soup.select_one('#restaurants').select('.filterData')
                for restaurantsDiv in restaurants_divs:
                    restaurant_name = restaurantsDiv.find('h3').get_text()

                    if not Restaurant.objects.filter(name__contains=restaurant_name).exists():
                        restaurant_img_url = website_url_without_language_code + '/' + restaurantsDiv.find('img')['src']
                        restaurant_url = website_url_without_language_code + '/' + restaurantsDiv.find('a')['href']
                        restaurant_soup = BeautifulSoup(requests.get(restaurant_url).content, 'html.parser')
                        restaurant_description = ''
                        try:
                            restaurant_description = restaurant_soup.select_one('.rs-description').find('p').get_text()
                        except AttributeError:
                            try:
                                restaurant_description = restaurant_soup.select_one('.rs-description').find(
                                    'span').get_text()
                            except AttributeError:
                                pass
                        restaurant_cuisine = restaurant_soup.select_one('.rs-cuisine').get_text()
                        restaurant_address = restaurant_soup.select_one('.rs-address').find(
                            'span', {'itemprop': 'streetAddress'}
                        ).get_text()
                        restaurant_website_url = 'https://' + \
                                                 restaurant_soup.select_one('.rs-address').find_all('span')[
                                                     -1].get_text()
                        restaurant_phone = restaurant_soup.select_one('.rs-booking').find('a').get('href').split(':')[1]
                        restaurant = Restaurant.objects.create(
                            name=restaurant_name,
                            cuisines=restaurant_cuisine,
                            description=restaurant_description,
                            address=restaurant_address,
                            city=city_name,
                            phone_number=restaurant_phone,
                            website=restaurant_website_url,
                        )
                        restaurant.image.save(
                            name=restaurant.name,
                            content=ContentFile(requests.get(restaurant_img_url).content)
                        )
        return render(request, 'index.html', {'urls': urls})
