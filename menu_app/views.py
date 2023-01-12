from django.shortcuts import render
from rest_framework import serializers
from rest_framework import generics
#from . import serializers
from menu_app.models import Food
from menu_app.models import FoodCategory
from menu_app.models import Topping
from django.core.serializers import serialize

def to_bool(s):
    try:
        s=int(s)
        if s==True:
            return True
        if s==False:
            return False
        return None
    except:
        return None


class FilterFoodListSerializer(serializers.ListSerializer):
    def to_representation(self,data):
        if type(to_bool(request.GET.get('is_vegan')))==bool:
            if type(to_bool(request.GET.get('is_special')))==bool:
                data=data.filter(is_publish=True,is_vegan=request.GET.get('is_vegan'),is_special=request.GET.get('is_special'))
                return super().to_representation(data)
            if type(to_bool(request.GET.get('is_special')))!=bool:
                data=data.filter(is_publish=True,is_vegan=request.GET.get('is_vegan'))
                return super().to_representation(data)
        if type(to_bool(request.GET.get('is_special')))==bool:
            data=data.filter(is_publish=True,is_special=request.GET.get('is_special'))
            return super().to_representation(data)
        return super().to_representation(data.filter(is_publish=True))


class FilterToppingListSerializer(serializers.ListSerializer):
    def to_representation(self,data):
        return super().to_representation(data)


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class=FilterFoodListSerializer
        model = Food
        fields = '__all__'


class ToppingSerializer(serializers.ModelSerializer):
    list_serializer_class=FilterToppingListSerializer

    class Meta:
        model = Topping
        fields = ['names']


class FoodCategoriesSerializer(serializers.ModelSerializer):
    foods =  FoodSerializer(many=True, read_only=True,source='food_set')
    toppings =  ToppingSerializer(many=True, read_only=True,source='topping_set')

    class Meta:
        model = FoodCategory
        fields = ['id','name','foods','toppings']


class FoodPublishList(generics.ListAPIView):
    serializer_class = FoodCategoriesSerializer

    def get_queryset(self):
        global request
        request=self.request
        queryset = FoodCategory.objects.all()
        queryset = queryset.filter(is_publish = True)
        return queryset
