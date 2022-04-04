from typing import List
import yagmail


EMAIL_ADDRESS = "example@test.com"
EMAIL_PASSWORD = "password"


class EmailClient:
    def __init__(self):
        self.yag = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_PASSWORD)

    def send_emails(self, email_title, email_body):
        self.yag.send(EMAIL_ADDRESS,
                      email_title, email_body)
