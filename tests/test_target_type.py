import unittest
from pychembldb import chembl, TargetType


class TargtTypeTest(unittest.TestCase):
    def setUp(self):
        self.target_type = chembl.query(TargetType).first()

    def test_target_type(self):
        self.assertEqual(self.target_type.target_type, "ADMET")

    def test_target_desc(self):
        self.assertEqual(self.target_type.target_desc, "ADMET")

    def test_target_relation(self):
        self.assertEqual(len(self.target_type.target_dictionaries), 3)
