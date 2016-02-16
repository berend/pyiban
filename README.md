# pyiban
validate and generate IBANs


Right now this only supports validating and creating german IBANs. It will be enhanced to cover all IBANs 
out there.


## Install

you can easily install pyiban with pip:

    pip install pyiban
    
    
## Usage
    
    from pyiban import get_iban
    
    country = "DE"
    bank_code = 37040044
    account_number = 532013000

    generated_iban = get_iban(country_code=country,
                                   bank_code=bank_code,
                                   account_number=account_number)

    
## Run tests

pyiban comes with some tests, actually currently only one (what a shame!). If you are tinkering with it and want to if you broke something just
run

    tox
    
## Changelog

### V0.2
* remodelled structure for easier handling/importing

### V0.1
* Initial commit
* validating and generating of german IBAN should work
* setting up of project, travis, packaging, testing and so on


## Roadmap

* implement all countries that use IBAN (official and unofficial)
* write a parser for SWIFT's list of BBAN formats
* more tests