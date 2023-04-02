import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator


    def test_adding(self):
        assert self.calc.adding(self, 10, 5) == 15

    def test_subtraction(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_multiply(self):
        assert self.calc.multiply(self, 10, 5) == 50

    def test_division(self):
        assert self.calc.division(self, 10, 5) == 2


    def teardown(self):
        print('Выполнение метода Teardown')