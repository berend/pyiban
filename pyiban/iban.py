# implements https://en.wikipedia.org/wiki/International_Bank_Account_Number

from bban import bban_format

IBAN_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_iban(country_code, bank_code, account_number, branch_number=None):
    data ={"country_code": country_code,
           "bank_code": bank_code,
           "account_number": account_number,
           "branch_number": branch_number }
    bban = _generate_bban(data)
    check_sum = _iban_check_sum(country_code, bban)
    iban = country_code + check_sum + bban
    return iban


def get_bank_code(iban):
    if validate_iban(iban):
        country_code = iban[:2]
        snippet = bban_format.get(country_code).get("bank_code")
        return int(iban[snippet[0]:snippet[1]])


def get_account_number(iban):
    if validate_iban(iban):
        country_code = iban[:2]
        snippet = bban_format.get(country_code).get("account_number")
        return int(iban[snippet[0]:snippet[1]])


def validate_iban(iban):
    # check if country code is valid,
    # then check if iban length is correct for that country
    country_code = iban[:2].upper()
    length_for_country = bban_format.get(country_code,{}).get("length", 0)
    if not length_for_country or len(iban) != length_for_country:
        return False
    return _to_base_10_Str(iban) % 97 == 1


def _to_base_10_Str(iban):
    #remove all spaces
    result = iban.replace(" ", "")
    # move first 4 chars to the end
    result = result[4:]+result[:4]
    # 0->0, 1->1, ..., A -> 10, B->11, ..., Z->35
    result = "".join(str(IBAN_ALPHABET.index(c)) for c in result)
    # cut leading zeros
    return int(result)


def _iban_check_sum(country_code, bban):
    check_string = bban + country_code + "00"
    check_string = "".join(str(IBAN_ALPHABET.index(c)) for c in check_string)
    check_sum = 98 - int(check_string) % 97
    return "%02d" % check_sum


def _generate_bban(data):
    country = data.get("country_code")
    bban = bban_format.get(country,{}).get("composition").format(**data)
    return bban

"""
ibans = [
    "AL47 2121 1009 0000 0002 3569 8741",     # Albania
    "AD12 0001 2030 2003 5910 0100",          # Andorra
    "AT61 1904 3002 3457 3201",               # Austria
    "AZ21 NABZ 0000 0000 1370 1000 1944",     # Azerbaijan
    "BH67 BMAG 0000 1299 1234 56",            # Bahrain
    "BE62 5100 0754 7061",                    # Belgium
    "BA39 1290 0794 0102 8494",               # Bosnia  and Herzegovina
    "BG80 BNBG 9661 1020 3456 78",            # Bulgaria
    "HR12 1001 0051 8630 0016 0",             # Croatia
    "CY17 0020 0128 0000 0012 0052 7600",     # Cyprus
    "CZ65 0800 0000 1920 0014 5399",          # Czech  Republic
    "DK50 0040 0440 1162 43",                 # Denmark
    "EE38 2200 2210 2014 5685",               # Estonia
    "FO97 5432 0388 8999 44",                 # Faroe Islands
    "FI21 1234 5600 0007 85",                 # Finland
    "FR14 2004 1010 0505 0001 3M02 606",      # France
    "GE29 NB00 0000 0101 9049 17",            # Georgia
    "DE89 3704 0044 0532 0130 00",            # Germany
    "GI75 NWBK 0000 0000 7099 453",           # Gibraltar
    "GR16 0110 1250 0000 0001 2300 695",      # Greece
    "GL56 0444 9876 5432 10",                 # Greenland
    "HU42 1177 3016 1111 1018 0000 0000",     # Hungary
    "IS14 0159 2600 7654 5510 7303 39",       # Iceland
    "IE29 AIBK 9311 5212 3456 78",            # Ireland
    "IL62 0108 0000 0009 9999 999",           # Israel
    "IT40 S054 2811 1010 0000 0123 456",      # Italy
    "JO94 CBJO 0010 0000 0000 0131 0003 02",  # Jordan
    "KW81 CBKU 0000 0000 0000 1234 5601 01",  # Kuwait
    "LV80 BANK 0000 4351 9500 1",             # Latvia
    "LB62 0999 0000 0001 0019 0122 9114",     # Lebanon
    "LI21 0881 0000 2324 013A A",             # Liechtenstein
    "LT12 1000 0111 0100 1000",               # Lithuania
    "LU28 0019 4006 4475 0000",               # Luxembourg
    "MK072 5012 0000 0589 84",                # Macedonia
    "MT84 MALT 0110 0001 2345 MTLC AST0 01S", # Malta
    "MU17 BOMM 0101 1010 3030 0200 000M UR",  # Mauritius
    "MD24 AG00 0225 1000 1310 4168",          # Moldova
    "MC93 2005 2222 1001 1223 3M44 555",      # Monaco
    "ME25 5050 0001 2345 6789 51",            # Montenegro
    "NL39 RABO 0300 0652 64",                 # Netherlands
    "NO93 8601 1117 947",                     # Norway
    "PK36 SCBL 0000 0011 2345 6702",          # Pakistan
    "PL60 1020 1026 0000 0422 7020 1111",     # Poland
    "PT50 0002 0123 1234 5678 9015 4",        # Portugal
    "QA58 DOHB 0000 1234 5678 90AB CDEF G",   # Qatar
    "RO49 AAAA 1B31 0075 9384 0000",          # Romania
    "SM86 U032 2509 8000 0000 0270 100",      # San Marino
    "SA03 8000 0000 6080 1016 7519",          # Saudi Arabia
    "RS35 2600 0560 1001 6113 79",            # Serbia
    "SK31 1200 0000 1987 4263 7541",          # Slovak Republic
    "SI56 1910 0000 0123 438",                # Slovenia
    "ES80 2310 0001 1800 0001 2345",          # Spain
    "SE35 5000 0000 0549 1000 0003",          # Sweden
    "CH93 0076 2011 6238 5295 7",             # Switzerland
    "TN59 1000 6035 1835 9847 8831",          # Tunisia
    "TR33 0006 1005 1978 6457 8413 26",       # Turkey
    "AE07 0331 2345 6789 0123 456",           # UAE
    "GB29 RBOS 6016 1331 9268 19",            # United Kingdom
    "AL47212110090000000235698741",
    "DZ4000400174401001050486",
    "AD1200012030200359100100",
    "AO06000600000100037131174",
    "AT611904300234573201",
    "AZ21NABZ00000000137010001944",
    "BH29BMAG1299123456BH00",
    "BA391290079401028494",
    "BE68539007547034",
    "BJ11B00610100400271101192591",
    "BR9700360305000010009795493P1",
    "BG80BNBG96611020345678",
    "BF1030134020015400945000643",
    "BI43201011067444",
    "CM2110003001000500000605306",
    "CV64000300004547069110176",
    "CR0515202001026284066",
    "HR1210010051863000160",
    "CY17002001280000001200527600",
    "CZ6508000000192000145399",
    "DK5000400440116243",
    "DO28BAGR00000001212453611324",
    "TL380080012345678910157",
    "EE382200221020145685",
    "FO1464600009692713",
    "FI2112345600000785",
    "FR1420041010050500013M02606",
    "GT82TRAJ01020000001210029690",
    "GE29NB0000000101904917",
    "DE89370400440532013000",
    "GI75NWBK000000007099453",
    "GR1601101250000000012300695",
    "GL8964710001000206",
    "HU42117730161111101800000000",
    "IS140159260076545510730339",
    "IR580540105180021273113007",
    "IE29AIBK93115212345678",
    "IL620108000000099999999",
    "IT60X0542811101000000123456",
    "CI05A00060174100178530011852",
    "JO94CBJO0010000000000131000302",
    "KZ176010251000042993",
    "KW74NBOK0000000000001000372151",
    "LV80BANK0000435195001",
    "LB30099900000001001925579115",
    "LI21088100002324013AA",
    "LT121000011101001000",
    "LU280019400644750000",
    "MK07300000000042425",
    "MG4600005030010101914016056",
    "MT84MALT011000012345MTLCAST001S",
    "MR1300012000010000002037372",
    "MU17BOMM0101101030300200000MUR",
    "ML03D00890170001002120000447",
    "MD24AG000225100013104168",
    "MC5813488000010051108001292",
    "ME25505000012345678951",
    "MZ59000100000011834194157",
    "NL91ABNA0417164300",
    "NO9386011117947",
    "PK24SCBL0000001171495101",
    "PS92PALS00000000040012345670",
    "PL27114020040000300201355387",
    "PT50000201231234567890154",
    "QA58DOHB00001234567890ABCDEFG",
    "XK051212012345678906",
    "RO49AAAA1B31007593840000",
    "SM86U0322509800000000270100",
    "SA0380000000608010167519",
    "SN12K00100152000025690007542",
    "RS35260005601001611379",
    "SK3112000000198742637541",
    "SI56191000000123438",
    "ES9121000418450200051332",
    "SE3550000000054910000003",
    "CH9300762011623852957",
    "TN5914207207100707129648",
    "TR330006100519786457841326",
    "AE260211000000230064016",
    "GB29NWBK60161331926819",
    "VG96VPVG0000012345678901"]
"""
