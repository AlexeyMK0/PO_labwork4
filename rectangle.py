import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    def test_float_a_mul(self):
        res = area(10., 5)
        self.assertEqual(res, 50)
    def test_float_b_mul(self):
        res = area(5, 10.)
        self.assertEqual(res, 50)
    def test_float_mul(self):
        res = area(5.0, 10.0)
        self.assertEqual(res, 50.0)
    
    def test_zero_per(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
    def test_square_per(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    def test_float_a(self):
        res = perimeter(10.0, 10)
        self.assertEqual(res, 40.0)
    def test_float_b(self):
        res = perimeter(10, 5.0)
        self.assertEqual(res, 30.0)
    def test_float_ab(self):
        res = perimeter(10.0, 20.0)
        self.assertEqual(res, 60.0)

def area(a, b):
    '''
    Возвращает плоащадь прямоугольника

        Параметры: 
            a (float) - первая сторона прямоугольника
            b (float) - вторая сторона прямоугольника
        Возвращаемое значение:
            area (float) - площадь прямоугольника
    '''
    return a * b 

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника

        Параметры:
            a (float) - первая сторона прямоугольника
            b (float) - вторая сторона прямоугольника
        Возвращаемое значение:
            perimeter (float) - периметр прямоугольника
    '''
    return (a + b) * 2
