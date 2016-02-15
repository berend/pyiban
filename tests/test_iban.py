from iban.iban import Iban


def test_get_iban():
    country = "DE"
    bank_code = 37040044
    account_number = 532013000

    expected_iban = "DE89370400440532013000"
    generated_iban = Iban.get_iban(country_code=country,
                                   bank_code=bank_code,
                                   account_number=account_number)

    assert(expected_iban == generated_iban)