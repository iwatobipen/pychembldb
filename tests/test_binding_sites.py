import unittest
from pychembldb import chembldb, BindingSite


class BindingSiteTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(BindingSite).get(1)

    def test_site_id(self):
        self.assertEqual(self.target.site_id, 1)

    def test_site_name(self):
        self.assertEqual(self.target.site_name, "Female germline-specific tumor suppressor gld-1, KH_1 domain")

    def test_tid(self):
        self.assertEqual(self.target.tid, 103735L)

    def test_sitecomponents(self):
        self.assertEqual(len(self.target.sitecomponents), 1)

    def test_predicted_binding_domains(self):
        self.assertEqual(len(self.target.predicted_binding_domains), 68)

    def test_components(self):
        self.assertEqual(len(self.target.components), 1)

    def test_domains(self):
        self.assertEqual(len(self.target.domains), 1)
