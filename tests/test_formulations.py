import unittest
from pychembldb import chembl, Formulation


class FormulationTest(unittest.TestCase):
    def setUp(self):
        self.target = chembl.query(Formulation).first()

    def test_product_id(self):
        self.assertEqual(self.target.product_id, "PRODUCT19072")

    def test_ingredient(self):
        self.assertEqual(self.target.ingredient, "INFLIXIMAB")

    def test_strength(self):
        self.assertIsNone(self.target.strength)

    def test_molregno(self):
        self.assertEqual(self.target.molregno, 675617L)