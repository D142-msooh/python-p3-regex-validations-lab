import re

# --------------------------
# NAME REGEX
# --------------------------
# Rules inferred from tests:
# ✔ Must match capitalized names
# ✔ Allows letters, apostrophes, hyphens
# ✔ Allows ONE optional space between first/last name
# ✔ Cannot start lowercase
# ✔ Cannot contain digits
# ✔ Cannot contain multiple spaces

name_regex = re.compile(
    r"^[A-Z][A-Za-z'\-]*(?: [A-Z][A-Za-z'\-]*)?$"
)

# --------------------------
# PHONE NUMBER REGEX
# --------------------------
# Must match:
#   5555555555
#   555-555-5555
#   (555) 555-5555
# Must not match:
#   9 digits
#   letters
#   multiple dashes (--)

phone_regex = re.compile(
    r"^(?:\d{10}|(?:\d{3}-){2}\d{4}|\(\d{3}\) \d{3}-\d{4})$"
)

# --------------------------
# EMAIL REGEX
# --------------------------
# Must match:
#   johncena@wwe.com
#   john.cena@wwe.com
#   john.cena123@wwe.com
# Must NOT match:
#   starting with number
#   missing @
#   contains $
#   missing domain

email_regex = re.compile(
    r"^[A-Za-z][A-Za-z0-9\.]*@[A-Za-z]+\.[A-Za-z]+$"
)