import random
import re
import string
import time

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

def is_valid_email(email):
    return bool(re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email))

def is_valid_phone(phone):
    return bool(re.fullmatch(r"(?:\+91[-\s]?)?[6-9]\d{9}", phone))

def is_valid_aadhaar(aadhaar):
    return bool(re.fullmatch(r"\d{4}\s\d{4}\s\d{4}", aadhaar))

def is_valid_pan(pan):
    return bool(re.fullmatch(r"[A-Z]{5}\d{4}[A-Z]", pan))

def is_strong_password(password):
    return bool(re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$", password))

value = int(input("[1] Generate password\n[2] Validate Email\n[3] Validate Phone Number\n[4] Validate Aadhaar Number\n[5] Validate PAN Number\n[6] Validate Password Strength\n[0] Exit\nEnter Value: "))

match value:
    case 0:
        print("exiting program")
        for i in range(5):
            print(5-i)
            time.sleep(1)
        pass
    case 1:
        print("Generated Password:", generate_password())
    case 2:
        email = input("enter email id: ")
        print(is_valid_email(email))
    case 3:
        no = input("enter phone number: ")
        print(is_valid_phone(no))
    case 4:
        aadhar = input("enter aadhar number: ")
        print(is_valid_aadhaar(aadhar))
    case 5:
        pan = input("enter pan number: ")
        print(is_valid_pan(pan))
    case 6:
        password = input("enter password: ")
        print(is_strong_password(password))
    case _:
        print("invalid option")

