from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    # Test the make_full_name function
    result = make_full_name("Sally", "Brown")
    expected = "Brown; Sally"
    assert result == expected, f"Expected: {expected}, Got: {result}"

def test_extract_family_name():
    # Test the extract_family_name function
    result = extract_family_name("Brown; Sally")
    expected = "Brown"
    assert result == expected, f"Expected: {expected}, Got: {result}"

def test_extract_given_name():
    # Test the extract_given_name function
    result = extract_given_name("Brown; Sally")
    expected = "Sally"
    assert result == expected, f"Expected: {expected}, Got: {result}"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
