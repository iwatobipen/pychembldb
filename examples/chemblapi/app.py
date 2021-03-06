from flask import Flask, jsonify
from pychembldb import chembldb, Molecule, CompoundStructure
app = Flask(__name__)
app.debug = True


def check_query(q):
    queries = q.split(".")
    if len(queries) > 1:
        return queries[0], queries[1]
    else:
        return queries[0], "xml"


def is_known_drug(c):
    if c.therapeutic_flag == 0:
        return "No"
    else:
        return "Yes"


def is_med_chem_friendly(c):
    if c.property.med_chem_friendly == "Y":
        return "Yes"
    else:
        return "No"


def is_ro3_pass(c):
    if c.property.ro3_pass == "Y":
        return "Yes"
    else:
        return "No"


@app.route("/chemblws/compounds/<chembl_id>")
def compound_by_ChEMBLID(chembl_id):
    chembl_id, format = check_query(chembl_id)
    compound = chembldb.query(Molecule).filter_by(chembl_id=chembl_id).one()

    result = {
    "compound": {
        "acdLogd": float(compound.property.acd_logd),
        "acdLogp": float(compound.property.acd_logp),
        "alogp": float(compound.property.alogp),
        "chemblId": chembl_id,
        "knownDrug": is_known_drug(compound),
        "medChemFriendly": is_med_chem_friendly(compound),
        "molecularFormula": compound.structure.molformula,
        "molecularWeight": float(compound.property.full_mwt),
        "numRo5Violations": compound.property.num_ro5_violations,
        "passesRuleOfThree": is_ro3_pass(compound),
        "rotatableBonds": compound.property.rtb,
        "smiles": compound.structure.canonical_smiles,
        "stdInChiKey": compound.structure.standard_inchi_key
        }
    }
    return jsonify(result)


@app.route("/chemblws/compounds/stdinchikey/<inchikey>")
def compound_by_InCHIKEY(inchikey):
    inchikey, format = check_query(inchikey)
    structure = chembldb.query(CompoundStructure).filter_by(standard_inchi_key=inchikey).one()
    compound = structure.molecule

    result = {
    "compound": {
        "acdLogd": float(compound.property.acd_logd),
        "acdLogp": float(compound.property.acd_logp),
        "alogp": float(compound.property.alogp),
        "chemblId": compound.chembl_id,
        "knownDrug": is_known_drug(compound),
        "medChemFriendly": is_med_chem_friendly(compound),
        "molecularFormula": compound.structure.molformula,
        "molecularWeight": float(compound.property.full_mwt),
        "numRo5Violations": compound.property.num_ro5_violations,
        "passesRuleOfThree": is_ro3_pass(compound),
        "rotatableBonds": compound.property.rtb,
        "smiles": compound.structure.canonical_smiles,
        "stdInChiKey": compound.structure.standard_inchi_key
        }
    }
    return jsonify(result)

# Description: Get list of compounds by Canonical SMILES
# Description: Get list of compounds by Canonical SMILES by HTTP POST
# Description: Get list of compounds containing the substructure represented by the given Canonical SMILES
# Description: Get list of compounds containing the substructure represented by the given Canonical SMILES by HTTP POST
# Description: Get list of compounds similar to the one represented by the given Canonical SMILES, at a similarity cutoff percentage score (minimum value=70%, maximum value=
# Description: Get list of compounds similar to the one represented by the given Canonical SMILES, at a similarity cutoff percentage score (minimum value=70%, maximum value=100%) by HTTP POST
# Description: Get the image of a given compound.
# Description: Get individual compound bioactivities
# Description: Get target by ChEMBLID
# Description: Get individual target by UniProt Accession Id
# Description: Get individual target by RefSeq Accession Id
# Description: Get individual target bioactivities
# Description: Get all targets
# Description: Get assay by ChEMBLID
# Description: Get individual assay bioactivities

if __name__ == "__main__":
    app.run()
