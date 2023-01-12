# Описание
menu_app возврщает списки Food, отсортированные по FoodCategory для всех записей с is_publish=True.
URL:
food_publish/

Доступна фильтрация по is_vegan, is_special. Параметры is_vegan=0/1, is_special=0/1 передаются через URL:
food_publish/?is_vegan=1
food_publish/?is_vegan=1&is_special=0
и т.д.
