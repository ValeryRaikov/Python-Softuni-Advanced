class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

class ContainsMoreThanOneAtSymbolError(Exception):
    pass

class ContainsInvalidSymbolsError(Exception):
    pass

MIN_LENGTH = 4
VALID_DOMAINS = [".com", ".bg", ".org", ".net"]
INVALID_SYMBOLS = ["~", "!", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "/", "<", ">" "=", ",", "?"]

email = input("Enter email: ")
while email != "End":
    if email.count("@") > 1:
        raise ContainsMoreThanOneAtSymbolError("Email must contain only one '@' symbol!")
    
    if "@" in email:
        first_part, second_part = email.split("@")
    else: 
        raise MustContainAtSymbolError("Email must contain '@' symbol!")
    
    if len(first_part) < 4:
        raise NameTooShortError("Too short username!")
    
    if "." in second_part:
        second_part, third_part = second_part.split(".")
    else:
        raise InvalidDomainError("Domain must be one of the following: .com/.bg/.org/.net")
    
    if f".{third_part}" not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com/.bg/.org/.net")
    
    for symbol in INVALID_SYMBOLS:
        if symbol in email:
            raise ContainsInvalidSymbolsError(f"Invalid symbol {symbol} in email!")
    
    print(f"This is your chosen email: {email}")
    
    email = input("Enter email or End to quit: ")