from cadenapalindroma import palindromo
import unittest

class Testdecimaltoroman(unittest.TestCase):
    def test1(self):
        pal = palindromo("a")
        self.assertEqual(pal, True)

    def test2(self):
        pal = palindromo("aba")
        self.assertEqual(pal, True)

    def test3(self):
        pal = palindromo("palabranopalindroma")
        self.assertEqual(pal, False)

    def test4(self):
        pal = palindromo("arenera")
        self.assertEqual(pal, True)

    def test5(self):
        pal = palindromo("cualquiercosa")
        self.assertEqual(pal, False)        

if __name__ == "__main__":
    unittest.main()
