from Bio import Entrez
import xml.etree.ElementTree as ET

def get_clinical_significance(rsID, email='rgarcia@inmegen.gob.mx'):
    Entrez.email = email
    response = Entrez.efetch(db='SNP', id=rsID, rettype='xml').read()
    tree = ET.fromstring(response)

    clinical_significance = None
    for e in tree.getiterator():
        if e.tag.endswith('ClinicalSignificance'):
            clinical_significance = e.text            
           
    return clinical_significance
