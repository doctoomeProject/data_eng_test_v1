import pandas as pd
import pytest

username = "dinis_timoteo"

@pytest.fixture(scope="module")
def medication_merged():
    """Load the processed parquet file once for all tests."""

    path = f"s3://data-eng-interviews/results/{username}.parquet"
    df = pd.read_parquet(path)
    return df


def test_shape(medication_merged):
    """Test final shape of the dataframe."""
    assert medication_merged.shape == (71521, 13), \
        f"Expected shape (71521, 13), got {medication_merged.shape}"


def test_nan_counts(medication_merged):
    """Test allowed NaN columns and their exact counts."""
    allowed_nans = {
        "cip7_code": 6996,
        "cip13_code": 6996,
        "dosage": 7716,
        "condition_d_prescription": 13271
    }

    # check only these columns have NaNs
    nan_counts = medication_merged.isna().sum()
    for col in medication_merged.columns:
        if col in allowed_nans:
            assert nan_counts[col] == allowed_nans[col], \
                f"Unexpected NaN count for {col}: {nan_counts[col]}"
        else:
            assert nan_counts[col] == 0, f"Column {col} should not contain NaN values"

    # check no empty strings
    for col in allowed_nans.keys():
        if medication_merged[col].dtype == "object":
            assert not (medication_merged[col] == "").any(), \
                f"Column {col} contains empty strings ('') instead of NaN/None"


def test_column_types(medication_merged):
    """Validate the data types of each column."""
    expected_types = {
        "cis_code": "int64",
        "survaillance_reinforce": "int64",
        "cip7_code": "float64",
        "cip13_code": "float64",
        "denomination_du_medicament": "object",
        "form_pharmaceutique": "object",
        "titulaire": "object",
        "statut_bdm": "object",
        "pharma_element": "object",
        "nom_de_substance": "object",
        "dosage": "object",
        "condition_d_prescription": "object",
        'code_de_substance':"float64"
    }
    # Check for extra/missing columns
    assert set(medication_merged.columns) == set(expected_types.keys()), \
        f"Columns mismatch. Expected: {set(expected_types.keys())}, got: {set(medication_merged.columns)}"

    # Check each dtype
    for col, expected_dtype in expected_types.items():
        actual_dtype = str(medication_merged[col].dtype)
        assert actual_dtype == expected_dtype, \
            f"Column '{col}' has dtype {actual_dtype}, expected {expected_dtype}"
