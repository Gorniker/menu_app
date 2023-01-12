from rest_framework import serializers
from menu_app.models import Food
from menu_app.models import FoodCategory
from menu_app.models import Topping


class FilterFoodListSerializer(serializers.ListSerializer):
    def to_representation(self,data):
        data=data.filter(is_publish=True)
        return super().to_representation(data)


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class=FilterFoodListSerializer
        model = Food
        fields = '__all__'


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'


class FoodCategoriesSerializer(serializers.ModelSerializer):
    foods =  FoodSerializer(many=True, read_only=True,source='food_set')
    toppings =  ToppingSerializer(many=True, read_only=True,source='topping_set')

    class Meta:
        model = FoodCategory
        fields = ['id','name','foods','toppings']
