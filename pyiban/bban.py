bban_format ={
    "AD": {
        "composition": "{04:bank_code}{04:branch_code}{012:account_number}",
        "country": "Andorra",
        "bank_code"
        "length": 24

    },
    "DE": {
        "composition": "{bank_code:08d}{account_number:010d}",
        "country": "Germany",
        "length": 22,
        "bank_code" : [4,12],
        "account_number":[12,22]
    },

}