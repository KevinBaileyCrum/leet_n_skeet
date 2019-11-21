# A password is considered strong if below conditions are all met:
# It has at least 6 characters and at most 20 characters.
# It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong,
#   assuming other conditions are met).

# first decide if valid
# then decide changes

# 6<=length<=20
# scan ::
#   hash lookup char in a row
#       break aprt
#   after complete scan
#   did have upper? lower? digit?

def strongPasswordChecker(s: str) -> int:
    return 0

