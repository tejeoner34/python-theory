"""
Tenemos que importar unittest y el archivo que queremos testear
"""

import unittest
import fileToTest

## Tenemos que crear una clase y pasarle el TestCase del unittest
class TestClass(unittest.TestCase):

    ## Creamos la function de testing
    def testSumFunction(self):
        num1 = 1
        num2 = 2
        result = fileToTest.sum(num2, num1)
        self.assertEqual(result, 3)


## Tenemos que añadir esto para que se ejecute
if __name__ == '__main__':
    unittest.main()