from django.test import TestCase
from menu_app.models import Food
from menu_app.models import FoodCategory
from menu_app.models import Topping
from menu_app.views import *
from django.urls import path

class FirstTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        names=['Carrot','Potato','Cucumber','Meat']
        for n in names:
            Topping.objects.create(name=n)

        FoodCategory.objects.create(name='Salad',is_publish=True)
        FoodCategory.objects.create(name='Dessert',is_publish=False)
        FoodCategory.objects.create(name='Drinks',is_publish=True)
        FoodCategory.objects.create(name='Main',is_publish=True)

        top=Food.objects.create(description='first dish',price=20,is_special=0,is_vegan=0,category_id=2,is_publish=False)
        top.toppings.set(Topping.objects.filter(id__in=[2,4]))
        top=Food.objects.create(description='second dish',price=21,is_special=0,is_vegan=1,category_id=1,is_publish=False)
        top.toppings.set(Topping.objects.filter(id__in=[5,6]))

    def test_Foodserializer(self):
        foods =  FoodSerializer(many=True, read_only=True,source='food_set')

    def test_toppingsFoodserializer(self):
        toppings =  ToppingSerializer(many=True, read_only=True,source='food_set')

    def test_FoodCategoryserializer(self):
        serializer_class = FoodCategoriesSerializer

    def test_path1(self):
        path('food_publish/', FoodPublishList.as_view())

    def test_path2(self):
        path('food_publish/?is_vegan=1', FoodPublishList.as_view())

    def test_path3(self):
        path('food_publish/?is_vegan=0', FoodPublishList.as_view())

    def test_path4(self):
        path('food_publish/?is_special=1', FoodPublishList.as_view())

    def test_path5(self):
        path('food_publish/?is_special=0', FoodPublishList.as_view())

    def test_comb_path(self):
        path('food_publish/?is_special=0&is_vegan=0', FoodPublishList.as_view())

    def test_wrong_path(self):
        path('food_publish/?is_special=45&is_vegan=is_is_vegan', FoodPublishList.as_view())
