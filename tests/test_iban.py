from pyiban import get_account_number
from pyiban import get_bank_code
from pyiban import get_iban


def test_get_iban():
    country = "DE"
    bank_code = 37040044
    account_number = 532013000

    expected_iban = "DE89370400440532013000"
    generated_iban = get_iban(country_code=country,
                              bank_code=bank_code,
                              account_number=account_number)

    assert expected_iban == generated_iban


def test_get_bank_code():
    iban = "DE89370400440532013000"
    retrieved_bank_code = get_bank_code(iban)

    expected_bank_code = 37040044

    assert retrieved_bank_code == expected_bank_code


def test_get_account_number():
    iban = "DE89370400440532013000"
    expected_account_number = 532013000
    retrieved_account_number = get_account_number(iban)
    assert expected_account_number == retrieved_account_number
