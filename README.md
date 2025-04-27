[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
# Password-Manager-CLI

## Project Purpose
The purpose of this project is to create a password manager that stores your passwords in a file. The data is stored in a .json file. This password manager currently supports the following operations:

### Add a Password
You can create or add a new entry to store your password.
You will be prompted to enter two parameters:
- **App name**: The name of the application or service..
- **Password**: Your password for that application/service.

If the entries are valid, the app name and password will be saved to the .json file.

### View Password
You can retrieve the password for a specific application.
You will be prompted to enter the application's name. The program will:
- Search if the application exists in the stored passwords.
- If it exists, the associated password will be displayed.
- If it doesn't exist, an error message will be shown.

### Update Password
You can update an existing password that you previously stored.
The program will:
- Prompt you for the application's name.
- Check if the application exists.
- If it exists, you will be prompted for a new password, which will overwrite the old one in the .json file.
- If it does not exist, an error message will be displayed.

### Delete Password
You can delete login details that you no longer require.
You will be prompted to enter the application's name. If the application exists:
- The corresponding entry (app name and password) will be deleted from the .json file.
- If it does not exist, an error message will be displayed.

## How To Run
1. Make sure you have **Python 3** installed
2. Clone this repository or download the project files
3. Run the script using:
   - Python passmanager.py

## Technologies Used
- Python 3
- JSON (for data storage)

## To Do:

1. Add encryption to protect stored passwords
2. Improve UI for a better user experience

## Future Features
- Implement user authentication (login system)
- Add a password generator for creating strong passwords

## Notes
Currently, passwords are stored in plain text in a .json file.
Encryption and additional security features are planned to make this password manager more secure.


## Demo Run
![image](https://github.com/user-attachments/assets/e42d4a18-c3a6-4b03-97e3-3b259416d936)


![image](https://github.com/user-attachments/assets/c8dedbae-efc5-4f64-9e3d-b04ded2b8d8b)

![image](https://github.com/user-attachments/assets/5822c2f5-2859-4616-a684-9521fa968154)
