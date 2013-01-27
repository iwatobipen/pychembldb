import unittest
from pychembldb import chembldb, MoleculeDictionary


class MoleculeDictionaryTest(unittest.TestCase):
    def setUp(self):
        self.mol = chembldb.query(MoleculeDictionary).get(1)

    def test_molregno(self):
        self.assertEqual(self.mol.molregno, 1)

    def test_pref_name(self):
        self.assertIsNone(self.mol.pref_name)

    def test_chembl_id(self):
        self.assertEqual(self.mol.chembl_id, "CHEMBL6329")

    def test_max_phase(self):
        self.assertEqual(self.mol.max_phase, 0)

    def test_therapeutic_flag(self):
        self.assertEqual(self.mol.therapeutic_flag, 0)

    def test_dosed_ingredient(self):
        self.assertEqual(self.mol.dosed_ingredient, 0)

    def test_structure_type(self):
        self.assertEqual(self.mol.structure_type, "MOL")

    def test_chebi_id(self):
        self.assertEqual(self.mol.chebi_id, 100001L)

    def test_chebi_par_id(self):
        self.assertIsNone(self.mol.chebi_par_id)

    def test_molecule_type(self):
        self.assertEqual(self.mol.molecule_type, "Small molecule")

    def test_first_approval(self):
        self.assertIsNone(self.mol.first_approval)

    def test_oral(self):
        self.assertEqual(self.mol.oral, 0)

    def test_parenteral(self):
        self.assertEqual(self.mol.parenteral, 0)

    def test_topical(self):
        self.assertEqual(self.mol.topical, 0)

    def test_black_box_warning(self):
        self.assertEqual(self.mol.black_box_warning, 0)

    def test_natural_product(self):
        self.assertEqual(self.mol.natural_product, 0)

    def test_prodrug(self):
        self.assertEqual(self.mol.prodrug, 0)

    # mol-compound_records
    def test_compounds(self):
        self.assertEqual(len(self.mol.compounds), 1)

    def test_compounds_backref(self):
        self.assertEqual(self.mol.compounds[0].molregno, self.mol.molregno)

    # mol-activities
    def test_activities(self):
        self.assertEqual(len(self.mol.activities), 2)

    def test_activities_backref(self):
        self.assertEqual(self.mol.activities[0].molregno, self.mol.molregno)

    # mol-compound_structure
    def test_structure(self):
        self.assertEqual(len(self.mol.structures), 1)

    def test_structure_backref(self):
        self.assertEqual(self.mol.structures[0].molregno, self.mol.molregno)

    # mol-compound_properties
    def test_properties(self):
        self.assertEqual(len(self.mol.properties), 1)

    def test_properties_backref(self):
        self.assertEqual(self.mol.properties[0].molregno, self.mol.molregno)

    ### Todo (relation)
    # chembl_id, protein_therapy, formulation
    # molecule_hierarchy, molecule_synonym
