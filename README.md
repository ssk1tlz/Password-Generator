# Password-Generator

![image](https://github.com/user-attachments/assets/3a18e017-e2d4-4480-9c88-1c71b941cc2a)

A simple and secure password generator with the option to send the generated password via email. This project demonstrates the use of Python's `tkinter` for a graphical user interface and `smtplib` for sending emails.

## Features

- **Password Generation:**
  - Generate random passwords with customizable length and character sets (uppercase letters, digits, special characters).
  - Copy the generated password to the clipboard.

- **Email Integration:**
  - Send the generated password to a specified email address.

## Setup and Installation

### Prerequisites

- Python 3.12 or higher
- Tkinter (included with standard Python installation)
- `python-dotenv` (for environment variable management)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/password-generator.git
    cd password-generator
    ```

2. **Install the required Python packages:**

    ```bash
    pip install python-dotenv
    ```

3. **Create a `.env` file** in the root directory of the project to store your email credentials. The file should contain:

    ```plaintext
    EMAIL_ADDRESS=your_email@gmail.com
    EMAIL_PASSWORD=your_app_password
    ```

    Replace `your_email@gmail.com` with your email address and `your_app_password` with your application-specific password or API key. For Gmail users, you may need to generate an [App Password](https://support.google.com/accounts/answer/185833) if you have 2FA enabled.

4. **Run the application:**

    ```bash
    python src/gui.py
    ```

## Usage

### Generating Passwords

- **Length:** Enter the desired length of the password.
- **Character Sets:**
  - **Uppercase Letters:** Include uppercase letters in the password.
  - **Digits:** Include digits in the password.
  - **Special Characters:** Include special characters in the password.
- Click "Generate" to create a password.
- Click "Copy" to copy the generated password to the clipboard.

### Sending Passwords via Email

- Enter the recipient's email address in the "Email" field.
- Click "Send to Email" to send the generated password to the specified email address.

## Project Structure

- `src/gui.py`: The Python script for the graphical user interface.
- `src/main.py`: Contains the password generation logic and email sending function.
- `.env`: Environment file containing email credentials (not included in version control).
- `README.md`: This README file.
- `requirements.txt`: Lists all the dependencies required by the project (optional).

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact

For any inquiries, please contact [your.email@example.com](mailto:your.email@example.com).
