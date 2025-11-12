CIS_bdpm_columns = [
    "cis_code",                          # Unique identifier for the medication (specialty)
    "denomination_du_medicament",                      # Full name of the medication (includes the brand)
    "form_pharmaceutique",              # Pharmaceutical form
    "voies_de_administration",             # Routes of administration
    "statut_administratif_de_iamm",                         # Administrative status of the marketing authorization
    "type_de_procedure_de_amm",                  # Type of marketing authorization procedure
    "etat_de_commercialisation",             # Commercialization status
    "date_de_amm",                           # Marketing authorization date
    "statut_bdm",                         # BDPM status: “Alerte” or “Availability warning”
    "eu_auth_num",      # European authorization number
    "titulaire",                         # Marketing authorization holder(s)
    "survaillance_reinforce"              # “Yes” if under additional monitoring (black triangle)
]

CIS_CPI_bdpm_columns = [
    "cis_code",                          # Links to the specialty (foreign key)
    "cip7_code",                         # 7-digit presentation identifier (box code)
    "livelle_de_apresentation",                             # Full label of the presentation (box description)
    "admin_statut",               # Administrative status of the presentation
    "etat_de_commerce",             # Commercialization status for this presentation
    "date_De_commerce",  # Date when commercialization was declared
    "cip13_code",                        # 13-digit presentation identifier (EAN-like code)
    "aggrement_collective",             # Approved for public institutions (“yes”, “no”, or “unknown”)
    "reimbursement_taux",                # Reimbursement rate(s), separated by “;”
    "prix_publique",                      # Public retail price (TTC)
    "price_prive",               # Institutional price (HT)
    "taux_diff",           # VAT or price difference
    "remboursement_indication"              # Text describing reimbursable indications
]

CIS_COMPO_bdpm_columns = [
    "cis_code",                          # Links to the specialty (foreign key)
    "pharma_element",               # Pharmaceutical element designation
    "code_de_substance",                     # Substance code
    "nom_de_substance",             # Substance name
    "dosage",                   # Dosage amount
    "dosage_ref",                   # Dosage reference (e.g. “per tablet”)
    "component_nature",                   # “SA” (active substance) or “ST” (therapeutic fraction)
    "num_de_liason"                  # Linking number between substances/fractions
]

CIS_CPD_bdpm_columns = [
    "cis_code",
    "condition_d_prescription"  # Prescription conditions
]
