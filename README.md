
# Brute-force Password Cracker for Login Page

This script attempts to find the correct password for a given login page by iterating through a list of possible passwords from a wordlist file. It sends POST requests to the target URL with different passwords until it finds the correct one.

## Overview

### Features:
- **Targeted URL**: The script targets a specific login page, defined by `target_url`.
- **Wordlist-based Password Brute-forcing**: Reads passwords from a file (`passwords.txt`) and attempts each one.
- **POST Request**: Uses the `requests` library to send POST data containing the username and each password.
- **Success Detection**: Checks the response to determine if the login attempt was successful.

## Prerequisites

- Python 3.x
- `requests` library (Install it using `pip install requests`)

## Usage

1. **Prepare the Wordlist**: Create a file named `passwords.txt` with potential passwords, each on a new line.

2. **Update the Target URL**: Modify the `target_url` variable in the script to match the login page you want to test.

3. **Run the Script**:

    ```bash
    python3 script.py
    ```

    Replace `script.py` with the name of your Python file.

4. **Interpreting Results**: 
    - If a password is found, it will print:
        ```
        Password is --> <found_password>
        ```
    - If no password is found in the wordlist, it will print:
        ```
        [+] Program is done
        ```

## Example

Make sure the login form has the same field names for "username" and "password" as in the `data_dictionnary` of the script.

```python
target_url = "http://192.168.1.5/dvwa/login.php"
```

## Disclaimer

This script is for educational purposes only. Brute-forcing login credentials without explicit permission is illegal and unethical. Use this script responsibly and only on systems where you have permission to test.


# 0x1tsjusthicham