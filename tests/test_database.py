import pytest
from praktikum.database import Database


class TestDatabase:

    def test_available_buns_correct(self, bun_mock):
        database = Database()
        database.buns = [bun_mock]
        result = database.available_buns()

        assert result == database.buns

    def test_available_buns_empty(self):
        database = Database()
        result = database.available_buns()

        assert result != []

    def test_available_ingredients_correct(self, ingredients_mock):
        database = Database()
        database.ingredients = [ingredients_mock]
        result = database.available_ingredients()

        assert result == database.ingredients

    def test_available_ingredients_empty(self):
        database = Database()
        result = database.available_ingredients

        assert result != []


