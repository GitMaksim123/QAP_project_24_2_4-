import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self,1,1) == 2  # позитивный тест сложение

    def test_adding_unsuccess(self):
        assert self.calc.adding(self,1,1) == 3  # негативный тест сложение

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1,0)        # деление на ноль

    def test_division_success(self):
        assert self.calc.division(self,2,2) == 1        # позитивный тест деление

    def test_multiply_success(self):
        assert self.calc.multiply(self,3,3) == 9  # позитивный тест умножение

    def test_multiply_unsuccess(self):
        assert self.calc.multiply(self, 3, 3) == 10  # негативный тест умножение

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 3, 3) == 0  # позитивный тест вычитание

    def test_subtraction_unsuccess(self):
        assert self.calc.subtraction(self, 3, 2) == 0  # негативный тест вычитание

    def teardown(self):
        print ('Выполнение terdown')
