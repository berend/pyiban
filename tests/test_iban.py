from pyiban import extract_account_number
from pyiban import extract_bank_code
from pyiban import generate_iban


def test_get_iban():
    country = "DE"
    bank_code = 37040044
    account_number = 532013000

    expected_iban = "DE89370400440532013000"
    generated_iban = generate_iban(country_code=country,
                                   bank_code=bank_code,
                                   account_number=account_number)

    assert expected_iban == generated_iban


def test_get_bank_code():
    iban = "DE89370400440532013000"
    retrieved_bank_code = extract_bank_code(iban)

    expected_bank_code = 37040044

    assert retrieved_bank_code == expected_bank_code


def test_get_account_number():
    iban = "DE89370400440532013000"
    expected_account_number = 532013000
    retrieved_account_number = extract_account_number(iban)
    assert expected_account_number == retrieved_account_number
