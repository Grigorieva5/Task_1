from praktikum.bun import Bun


class TestBun:

    def test_bu_initialization(self):
        bun = Bun('Космическая булка', 349.9)
        
        assert bun.name == 'Космическая булка' and bun.price == 349.9

    def test_get_name_correct_name(self):
        bun = Bun('Космическая булка', 349.9)

        assert bun.get_name() == 'Космическая булка'

    def test_get_name_return_string(self):
        bun = Bun('Космическая булка', 349.9)

        assert isinstance(bun.get_name(), str)

    def test_get_price_correct_price(self):
        bun = Bun('Космическая булка', 349.9)

        assert bun.get_price() == 349.9

    def test_get_price_return_float(self):
        bun = Bun('Космическая булка', 349.9)

        assert isinstance(bun.get_price(), float)
