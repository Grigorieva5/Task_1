import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import * 


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type_data, name_data, price_data', [
        (INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 20.47),
        (INGREDIENT_TYPE_FILLING, 'Кристаллы марсианских альфа-сахаридов', 1000)
    ])
    def test_ingredient_initialization(self, ingredient_type_data, name_data, price_data):
        ingredient = Ingredient(ingredient_type_data, name_data, price_data)

        assert (ingredient.type == ingredient_type_data and
                ingredient.name == name_data and
                ingredient.price == price_data)


    def test_get_price_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 20.47)

        assert ingredient.get_price() == 20.47


    def test_get_price_return_float(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 20.47)

        assert isinstance(ingredient.get_price(), float)


    def test_get_name_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 20.47)

        assert ingredient.get_name() == 'Соус традиционный галактический'


    def test_get_name_return_string(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 20.47)
        
        assert isinstance(ingredient.get_name(), str)


    @pytest.mark.parametrize('ingredient_type_data', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_correct_type(self,ingredient_type_data):
        ingredient = Ingredient(ingredient_type_data, 'Соус традиционный галактический', 20.47)

        assert ingredient.get_type() == ingredient_type_data


    def test_get_type_return_string(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 20.47)
        
        assert isinstance(ingredient.get_type(), str)    


          



