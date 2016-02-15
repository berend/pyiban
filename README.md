# pyiban
validate and generate IBANs


Right now this only supports validating and creating german IBANs. It will be enhanced to cover all IBANs 
out there.


## Install

you can easily install pyiban with pip:

    pip install pyiban
    
    
## Run tests

pyiban comes with some tests, actually currently only one (what a shame!). If you are tinkering with it and want to if you broke something just
run

    tox
    
## Changelog

### V0.1
* Initial commit
* validating and generating of german IBAN should work
* setting up of project, travis, packaging, testing and so on


## Roadmap

* implement all countries that use IBAN (official and unofficial)
* write a parser for SWIFT's list of BBAN formats
* more tests