from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.urls import reverse
from rest_framework import serializers
from django.db.models import Q

from rest_framework.response import Response
from rest_framework import viewsets


from .models import City 
from .serializers import CityNameSerializer, CitySerializer

from .models import Zone
from .serializers import ZoneSerializer

from .models import Apartment
from .serializers import ApartmentSerializer

from rest_framework.decorators import api_view

class CityView(viewsets.GenericViewSet):

        #______________________________GET ALL CITIES______________________________________________________________
        
        def getAllCities(self,request):   
            cities = City.objects.all()
            cities_serializer = CitySerializer(cities, many=True)
            return JsonResponse(cities_serializer.data, safe=False)    
    
        #______________________________CREATE ONE CITY______________________________________________________________

        def post(self,request):
            city_data = JSONParser().parse(request)
            city_serializer = CitySerializer(data=city_data)

            if city_serializer.is_valid():
                city_serializer.save()
                return JsonResponse(city_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(city_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #______________________________DELETE ONE CITY_______________________________________________________________
        
        def delete(self, request, slug_city):
            city = City.objects.get(slug=slug_city) 
            city.delete() 
            return JsonResponse({'message': 'City was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
        #______________________________GET ONE CITY BY SLUG_______________________________________________________________
        
        def getOneCity(self,request, slug_city):
            try: 
                city = City.objects.get(slug=slug_city)
                city_serializer = CitySerializer(city) 
                return JsonResponse(city_serializer.data)
            except City.DoesNotExist: 
                return JsonResponse({'message': 'The City does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        #______________________________GET ONE CITY BY ID_______________________________________________________________
        
        def getOneCityById(self,request, id):
            try: 
                city = City.objects.get(pk=id)
                city_serializer = CitySerializer(city) 
                return JsonResponse(city_serializer.data)
            except City.DoesNotExist: 
                return JsonResponse({'message': 'The City does not exist'}, status=status.HTTP_404_NOT_FOUND)

        #______________________________UPDATE ONE CITY_____________________________________________________________
        
        def put(self, request, slug_city):
            try:
                city = City.objects.get(slug=slug_city)
                city_data = JSONParser().parse(request) 
                city_serializer = CitySerializer(city, data=city_data) 
                if city_serializer.is_valid(): 
                    city_serializer.save() 
                return JsonResponse(city_serializer.data) 
            except City.DoesNotExist:
                return JsonResponse({'message': 'The City does not exist'}, status=status.HTTP_404_NOT_FOUND)
            

class ZoneView(viewsets.GenericViewSet):

        #______________________________GET ALL ZONES______________________________________________________________
        
        def getAllZones(self,request):   
            zones = Zone.objects.all()
            zones_serializer = ZoneSerializer(zones, many=True)
            return JsonResponse(zones_serializer.data, safe=False)
        
        #______________________________CREATE ONE ZONE______________________________________________________________
        
        def post(self,request):
            
            name = request.data['name']
            zone_type = request.data['zone_type']
            city = request.data['city']
            zone_image = request.data['zone_image']

            try:
                city_2 = City.objects.get(pk=city)

                zone = Zone.objects.create(
                    name=name,
                    zone_type=zone_type,
                    city=city_2,
                    zone_image=zone_image
                )
                zone_serializer = ZoneSerializer(instance=zone)

                return JsonResponse(zone_serializer.data , status=status.HTTP_201_CREATED)

            except City.DoesNotExist:
                return JsonResponse({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)
        
        #______________________________UPDATE ONE ZONE_____________________________________________________________
        
        def put(self, request, slug_zone):
            try:
                zone = Zone.objects.get(slug=slug_zone)
                zone_data = JSONParser().parse(request) 
                zone_serializer = ZoneSerializer(zone, data=zone_data) 
                if zone_serializer.is_valid(): 
                    zone_serializer.save() 
                return JsonResponse(zone_serializer.data) 
            except Zone.DoesNotExist:
                return JsonResponse({'message': 'The Zone does not exist'}, status=status.HTTP_404_NOT_FOUND)

        #______________________________GET ONE ZONE BY SLUG_______________________________________________________________
            
        def getOneZone(self,request, slug_zone):
            try: 
                zone = Zone.objects.get(slug=slug_zone)
                zone_serializer = ZoneSerializer(zone) 
                return JsonResponse(zone_serializer.data)
            except Zone.DoesNotExist: 
                return JsonResponse({'message': 'The Zone does not exist'}, status=status.HTTP_404_NOT_FOUND)
            
        #______________________________GET ONE ZONE BY ID_______________________________________________________________
        
        def GetZoneById(self,request, id):
            try: 
                zone = Zone.objects.get(pk=id)
                zone_serializer = ZoneSerializer(zone) 
                return JsonResponse(zone_serializer.data)
            except Zone.DoesNotExist: 
                return JsonResponse({'message': 'The Zone does not exist'}, status=status.HTTP_404_NOT_FOUND)
            
        #______________________________DELETE ONE ZONE_______________________________________________________________
        
        def delete(self, request, slug_zone):
            zone = Zone.objects.get(slug=slug_zone) 
            zone.delete() 
            return JsonResponse({'message': 'Zone was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
        #______________________________GET ALL ZONES BY CITY______________________________________________________________
        
        def getAllZonesByCity(self,request, slug_city):   
            try:
                city = City.objects.get(slug=slug_city)
                zones = Zone.objects.filter(city=city)
                zones_serializer = ZoneSerializer(zones, many=True)
                return JsonResponse(zones_serializer.data, safe=False)
            except City.DoesNotExist:
                return JsonResponse({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)
            
            
class ApartmentView(viewsets.GenericViewSet):

        #______________________________GET ALL APARTMENTS______________________________________________________________
        
        def getAllApartments(self,request):
            apartments = Apartment.objects.all()
            apartments_serializer = ApartmentSerializer(apartments, many=True)
            return JsonResponse(apartments_serializer.data, safe=False)
    
        #______________________________GET ONE APARTMENT_______________________________________________________________
        
        def post(self,request):
            
            location = request.data['location']
            price = request.data['price']
            rooms = request.data['rooms']
            bathrooms = request.data['bathrooms']
            size = request.data['size']
            apartment_images = request.data['apartment_images']
            zone = request.data['zone']

            try:
                zone_2 = Zone.objects.get(pk=zone)

                apartment = Apartment.objects.create(
                    location=location,
                    price=price,
                    rooms=rooms,
                    bathrooms=bathrooms,
                    size=size,
                    apartment_images=apartment_images,
                    zone=zone_2
                )

                apartment_serializer = ApartmentSerializer(instance=apartment)
                return JsonResponse(apartment_serializer.data , status=status.HTTP_201_CREATED)

            except Zone.DoesNotExist:
                return JsonResponse({'error': 'Zone not found'}, status=status.HTTP_404_NOT_FOUND)
        
        #______________________________UPDATE ONE APARTMENT_____________________________________________________________
        
        def put(self, request, slug_apartment):
            try:
                apartment = Apartment.objects.get(slug=slug_apartment)
                apartment_data = JSONParser().parse(request)                
                apartment_serializer = ApartmentSerializer(apartment, data=apartment_data)
                
                if apartment_serializer.is_valid():
                    apartment_serializer.save()
                return JsonResponse(apartment_serializer.data) 
            except Apartment.DoesNotExist:
                return JsonResponse({'message': 'The Apartment does not exist'}, status=status.HTTP_404_NOT_FOUND)
            
        #______________________________GET ONE APARTMENT_______________________________________________________________
        
        def getOneApartment(self,request, slug_apartment):
            try: 
                apartment = Apartment.objects.get(slug=slug_apartment)
                apartment_serializer = ApartmentSerializer(apartment) 
                return JsonResponse(apartment_serializer.data)
            except Apartment.DoesNotExist: 
                return JsonResponse({'message': 'The Apartment does not exist'}, status=status.HTTP_404_NOT_FOUND)
            
        
        #______________________________GET ONE APARTMENT_______________________________________________________________
        
        def getOneApartmentById(self,request, id):
            try: 
                apartment = Apartment.objects.get(pk=id)
                apartment_serializer = ApartmentSerializer(apartment) 
                return JsonResponse(apartment_serializer.data)
            except Apartment.DoesNotExist: 
                return JsonResponse({'message': 'The Apartment does not exist'}, status=status.HTTP_404_NOT_FOUND)
            
        #______________________________DELETE ONE APARTMENT_______________________________________________________________
        
        def delete(self, request, slug_apartment):
            apartment = Apartment.objects.get(slug=slug_apartment) 
            apartment.delete() 
            return JsonResponse({'message': 'Apartment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
        #______________________________GET ALL APARTMENTS BY ZONE______________________________________________________________
        
        def getApartmentsByZone(self,request, slug_zone):   
            try:
                zone = Zone.objects.get(slug=slug_zone)
                apartments = Apartment.objects.filter(zone=zone)
                apartments_serializer = ApartmentSerializer(apartments, many=True)
                return JsonResponse(apartments_serializer.data, safe=False)
            except Zone.DoesNotExist:
                return JsonResponse({'error': 'Zone not found'}, status=status.HTTP_404_NOT_FOUND)
        

        def getfilteredApartments(self, request):
            if request.method == 'POST':
                filters = Q()  # Inicializamos un objeto Q

                #  Para cada uno de los campos que se envíen en el request, se añade una condición al objeto Q
                if 'rooms' in request.data and request.data['rooms'] not in [None, ""]:
                    filters &= Q(rooms=request.data['rooms'])
                if 'bathrooms' in request.data and request.data['bathrooms']not in [None, ""]:
                    filters &= Q(bathrooms=request.data['bathrooms'])
                if 'city' in request.data and request.data['city'] not in [None, ""]:
                    city_slug = request.data['city']
                    city = City.objects.get(slug=city_slug) #get the city object

                    zones = Zone.objects.filter(city=city)
                    print(zones)
                    filters &= Q(zone__in=zones)
                    print( 'this are the filters', filters)

                # Con el objeto Q lleno, se filtran los apartamentos
                apartments = Apartment.objects.filter(filters)

                # Serializamos los apartamentos y los devolvemos al frontend
                apartments_serializer = ApartmentSerializer(apartments, many=True)
                return JsonResponse(apartments_serializer.data, safe=False)

            else:
                return JsonResponse({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            


        def getAvailableCitiesFromApartments(self,request):
            apartments = Apartment.objects.all()

            zone_ids = apartments.values_list('zone', flat=True).distinct()

            zones = Zone.objects.filter(id__in=zone_ids)

            city_ids = zones.values_list('city', flat=True).distinct()

            cities = City.objects.filter(id__in=city_ids)
            
            cities_serializer = CityNameSerializer(cities, many=True)
            return JsonResponse(cities_serializer.data, safe=False)
        

        #______________________________GET APARTMENTS BY CITY______________________________________________________________
        
        # def getApartmentsByCity(self,request, slug_city):   
        #     try:
        #         city = City.objects.get(slug=slug_city)
        #         zones = Zone.objects.filter(city=city)
        #         apartments = Apartment.objects.filter(zone__in=zones)
        #         apartments_serializer = ApartmentSerializer(apartments, many=True)
        #         return JsonResponse(apartments_serializer.data, safe=False)
        #     except City.DoesNotExist:
        #         return JsonResponse({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # #______________________________GET APARTMENTS BY BEDROOMS______________________________________________________________
        
        # def getApartmentsByBedrooms(self,request, ):
        #     # print(request.data)
        #     # print('hoplaaasamkaljsakoljdfakljsdkajkldasjkldasjklsdajklasdjklsdajklasdjkldasjklasdjkl')
        #     rooms = request.data['rooms']
        #     print(rooms)
        #     try:
        #         apartments = Apartment.objects.filter(rooms=rooms)
        #         apartments_serializer = ApartmentSerializer(apartments, many=True)
        #         return JsonResponse(apartments_serializer.data, safe=False, status=status.HTTP_200_OK)
        #     except Apartment.DoesNotExist:
        #         return JsonResponse({'error': 'Apartments not found'}, status=status.HTTP_404_NOT_FOUND)
            
        # #______________________________GET APARTMENTS BY BATHROOMS______________________________________________________________
        
        # def getApartmentsByBathrooms(self,request):   
        #     bathrooms = request.data['bathrooms']
        #     try:
        #         apartments = Apartment.objects.filter(bathrooms=bathrooms)
        #         apartments_serializer = ApartmentSerializer(apartments, many=True)
        #         return JsonResponse(apartments_serializer.data, safe=False)
        #     except Apartment.DoesNotExist:
        #         return JsonResponse({'error': 'Apartments not found'}, status=status.HTTP_404_NOT_FOUND)
            

        # #______________________________GET APARTMENTS BY MORE THAN THIS SIZE______________________________________________________________
        
        # def getApartmentsBySize(self,request):
        #     size = request.data['size']
        #     try:
        #         apartments = Apartment.objects.filter(size__gt=size)
        #         apartments_serializer = ApartmentSerializer(apartments, many=True)
        #         return JsonResponse(apartments_serializer.data, safe=False)
        #     except Apartment.DoesNotExist:
        #         return JsonResponse({'error': 'Apartments not found'}, status=status.HTTP_404_NOT_FOUND)
            
        # #______________________________GET APARTMENTS BY RANGE OF PRICE______________________________________________________________

        # def getApartmentsByPriceRange(self,request):
        #     price_min = request.data['price_min']
        #     price_max = request.data['price_max']
        #     try:
        #         apartments = Apartment.objects.filter(price__range=(price_min, price_max))
        #         apartments_serializer = ApartmentSerializer(apartments, many=True)
        #         return JsonResponse(apartments_serializer.data, safe=False)
        #     except Apartment.DoesNotExist:
        #         return JsonResponse({'error': 'Apartments not found'}, status=status.HTTP_404_NOT_FOUND)
            


        #______________________________GET CITIES FROM AVAILABLE APARTMENTS______________________________________________________________
        
