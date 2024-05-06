import openai
import time
import smtplib

from config import USE_API, OPENAI_API_KEY, PROMPT, SUBJECT, MESSAGE, EMAIL_ADDRESS, EMAIL_PASSWORD, RECIPIENT_EMAIL, SMTP_SERVER, SMTP_PORT

def generate_text(prompt, model_engine='gpt-3.5-turbo-instruct', max_tokens = 300, temperature = 0.8):
    try:
        openai.api_key = OPENAI_API_KEY
        completion = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = max_tokens, n = 1, stop = None, temperature = temperature)
        generated_text = list(completion.choices)[0]['text'].lstrip()
        return generated_text
    except Exception as e:
        print(f"An error occurred while generating text: {e}")

def send_email(email, password, recipient_email, subject, message, smtp_server = SMTP_SERVER, smtp_port = SMTP_PORT):
    try:
        smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
        smtp_obj.ehlo()
        smtp_obj.starttls()
        smtp_obj.login(email, password)
        from_address = email
        msg = f"Subject: {subject}\n\n{message}"
        smtp_obj.sendmail(from_address, recipient_email, msg.encode('utf-8'))
        smtp_obj.quit()
    except Exception as e:
        print(f"An error occurred while sending email: {e}")

def main():
    if USE_API:
      message = generate_text(PROMPT)
      time.sleep(5)
    else:
        message = MESSAGE

    email_address = EMAIL_ADDRESS
    email_password = EMAIL_PASSWORD
    recipient_email = RECIPIENT_EMAIL
    subject = SUBJECT

    send_email(email_address, email_password, recipient_email, subject, message)

if __name__ == "__main__":
    main()