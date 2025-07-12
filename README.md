# Python Data Validator Tool

A simple **command-line tool** written in Python to:

- Generate strong passwords
- Validate:
  - Email addresses
  - Indian phone numbers
  - Aadhaar numbers
  - PAN numbers
  - Password strength

> Built using core modules: `re`, `random`, `string`, `time`, and Python's `match-case` feature (Python 3.10+)

---

## Features

- **Password Generator** – customizable, strong passwords
- **Regex-based input validation** for real-world formats
- **Fast CLI interaction** with a clear menu
- Exit timer with countdown animation

---

## Preview

```bash
[1] Generate password
[2] Validate Email
[3] Validate Phone Number
[4] Validate Aadhaar Number
[5] Validate PAN Number
[6] Validate Password Strength
[0] Exit
Enter Value:
```

---

## How to Use

### 1. Clone the repository
```bash
git clone https://github.com/Moltenshoe/python_data_validator.git
cd python_data_validator
```

### 2. Run the program
```bash
python password_validator.py
```

Make sure you're using **Python 3.10+** (for `match-case`)

---

## Sample Validation Rules

| Input Type | Valid Format Example          |
|------------|-------------------------------|
| Email      | `john.doe@example.com`        |
| Phone      | `+91 9876543210`, `9876543210`|
| Aadhaar    | `1234 5678 9012`              |
| PAN        | `ABCDE1234F`                  |
| Password   | Must have 1 uppercase, 1 lowercase, 1 digit, min 8 chars |

---

## Modules Used

- `random` – For generating passwords
- `string` – Character sets
- `re` – Regular expressions for validation
- `time` – For animated countdown
- `match-case` – Clean switch-case style logic (Python 3.10+)

---

## Author

Made by [**Moltenshoe**](https://github.com/Moltenshoe)  
Part of a **7-day Python Module Challenge**

---

## Tags

`#Python` `#Regex` `#CLI` `#Validation` `#PasswordGenerator` `#Python3.10`
