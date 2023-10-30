import phonenumbers
from phonenumbers import geocoder

phone_num = phonenumbers.parse(input("Enter phone number to track: "))

print(f"Phone number location: ")
print(geocoder.description_for_number(phone_num, "en"))
print(f"Additional info: {phone_num}")