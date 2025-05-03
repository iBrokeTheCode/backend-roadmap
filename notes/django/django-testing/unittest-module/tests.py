import unittest

from app import SuperHero


class TestSuperHero(unittest.TestCase):
    def setUp(self) -> None:
        self.superman = SuperHero("Superman", 50)
        self.batman = SuperHero("Barman", 42)

    def test_stringify(self):
        self.assertEqual(str(self.superman), "Superman")

    def test_is_stronger_than_other_superhero(self):
        self.assertTrue(self.superman.is_stronger_than(self.batman))
        self.assertFalse(self.batman.is_stronger_than(self.superman))
