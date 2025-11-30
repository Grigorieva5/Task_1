import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import * 


@pytest.fixture
def bun_mock():
    mock_bun = Mock(name='BunMock')
    mock_bun.get_name.return_value = 'Космическая булка'  
    mock_bun.get_price.return_value = 349.99   
    return mock_bun


@pytest.fixture(params=[INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
def ingredients_mock(request):
    ingredient_type_data = request.param
    mock_ingredient = Mock(name='IngredientMock')
    mock_ingredient.get_name.return_value = 'Соус традиционный галактический'
    mock_ingredient.get_type.return_value = ingredient_type_data
    mock_ingredient.get_price.return_value = 349.99
    return mock_ingredient

