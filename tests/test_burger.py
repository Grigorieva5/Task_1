import pytest
from praktikum.burger import Burger


class TestBurger:

    def test_burger_initialization(self):
        burger = Burger()

        assert burger.ingredients == [] and len(burger.ingredients) == 0

    def test_set_buns_correct_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)

        assert burger.bun == bun_mock

    def test_add_ingredient_correct_add_ingredients(self, ingredients_mock):
        burger = Burger()
        burger.add_ingredient(ingredients_mock)

        assert burger.ingredients == [ingredients_mock]

    # удаление различных индексов
    @pytest.mark.parametrize('index, expected_count', [(0, 2), (1, 2), (-1, 2) ])
    def test_remove_ingredient_remove_different_index(self, index, expected_count, ingredients_mock):
        burger = Burger()
        for _ in range(3):
            burger.add_ingredient(ingredients_mock)
        
        burger.remove_ingredient(index)

        assert len(burger.ingredients) == expected_count

    # Удаление единственного элемента
    def test_remove_ingredient_single_element(self, ingredients_mock):
        burger = Burger()
        burger.add_ingredient(ingredients_mock)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0 and burger.ingredients == []  

    @pytest.mark.parametrize('index, new_index, expected_result', [
        (0, 2, ['B', 'C', 'A']),
        (2, 0, ['C', 'A', 'B']),
        (1, 0, ['B', 'A', 'C']),
        (1, 1, ['A', 'B', 'C']),
    ])
    def test_move_ingredient_different_positions(self, index, new_index, expected_result):
        burger = Burger()
        burger.ingredients = ['A', 'B', 'C']
        burger.move_ingredient(index, new_index) 

        assert burger.ingredients == expected_result

    def test_get_price_bun_price(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        price = burger.get_price()

        assert price == bun_mock.get_price() * 2

    def test_get_price_bun_plus_ingredient(self, bun_mock, ingredients_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredients_mock)
        price = burger.get_price()
        total_price = bun_mock.get_price() * 2 + ingredients_mock.get_price()  

        assert price == total_price

    def test_get_price_bun_plus_two_ingredient(self, bun_mock, ingredients_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredients_mock)
        burger.add_ingredient(ingredients_mock)
        price = burger.get_price()
        total_price = bun_mock.get_price()*2 + ingredients_mock.get_price()*2 

        assert price == total_price

    def test_get_receipt_two_bun(self, bun_mock, ingredients_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredients_mock)
        receipt = burger.get_receipt()

        assert  (f'(==== {bun_mock.get_name()} ====)' in receipt and
                receipt.count(f'(==== {bun_mock.get_name()} ====)')==2)
        
    def test_get_receipt_ingredients(self, bun_mock, ingredients_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredients_mock)
        burger.add_ingredient(ingredients_mock)
        receipt = burger.get_receipt()

        assert  (f'= {str(ingredients_mock.get_type()).lower()} {ingredients_mock.get_name()} =' in receipt and
                receipt.count(f'= {str(ingredients_mock.get_type()).lower()} {ingredients_mock.get_name()} =')==2) 

    def test_get_receipt_price(self, bun_mock, ingredients_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredients_mock)
        burger.add_ingredient(ingredients_mock)
        receipt = burger.get_receipt()
        total_price = bun_mock.get_price()*2 + ingredients_mock.get_price()*2

        assert  f'Price: {total_price}' in receipt

    def test_get_receipt_structure(self, bun_mock, ingredients_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredients_mock)
        burger.add_ingredient(ingredients_mock)
        receipt = burger.get_receipt()
        total_price = bun_mock.get_price()*2 + ingredients_mock.get_price()*2
        structure = (
            f"(==== {bun_mock.get_name()} ====)\n"
            f"= {ingredients_mock.get_type().lower()} {ingredients_mock.get_name()} =\n"
            f"= {ingredients_mock.get_type().lower()} {ingredients_mock.get_name()} =\n"
            f"(==== {bun_mock.get_name()} ====)\n"
            f"\n"
            f"Price: {total_price}"
        )
        
        assert structure == receipt   
        


