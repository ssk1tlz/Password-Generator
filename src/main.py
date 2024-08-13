from dotenv import load_dotenv
import string
import random
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()  # Загрузка переменных окружения из .env файла

def send_password_via_email(recipient_email, password):
    sender_email = os.getenv('EMAIL_ADDRESS')
    sender_password = os.getenv('EMAIL_PASSWORD')
    
    
def send_password_via_email(recipient_email, password):
    sender_email = ""  # Замените на вашу почту
    sender_password = "your_email_password"  # Замените на ваш пароль
    
    # Создаем сообщение
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Your Generated Password"
    
    # Текст сообщения
    body = f"Here is your generated password: {password}"
    message.attach(MIMEText(body, "plain"))
    
    try:
        # Настройка SMTP-сервера
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication Error: Unable to log in, please check your email and password.")
    except smtplib.SMTPRecipientsRefused:
        print("Recipient Error: The email address of the recipient was refused.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
def generate_password(length=25, use_uppercase=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generated Password:", generate_password())