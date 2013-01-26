import unittest
from pychembldb import chembl, RelationshipType


class RelationshipTypeTest(unittest.TestCase):
    def setUp(self):
        self.target = chembl.query(RelationshipType).first()

    def test_relationship_type(self):
        self.assertEqual(self.target.relationship_type, "D")

    def test_relationship_desc(self):
        self.assertEqual(self.target.relationship_desc, "Direct protein target assigned")
