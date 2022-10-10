
import smtplib, ssl
from decouple import config

SMTP_PASS = config("SMTP_PASS")
GOOGLE_SMTP = config("GOOGLE_SMTP")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")

ROLES = ("regular", "staff", "admin")

class User:
    no_of_users = 0
    def __init__(self, first_name, last_name, dob, is_staff=False, is_admin=False) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.is_staff = is_staff
        self.is_admin = is_admin
        self.role = None
        self.dob = dob
        self.email = f"{self.first_name}.{self.last_name}@email.com"
        User.no_of_users += 1

        if self.is_staff:
            self.role = ROLES[1]

        if self.is_admin:
            self.role = ROLES[2]

    def __str__(self) -> str:
        return self.fullname()

    def __repr__(self) -> str:
        return "Something"

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def send_mail(self):
        pass
        # try:
        # context = ssl.create_default_context()
        # server = smtplib.SMTP_SSL(GOOGLE_SMTP, EMAIL_PORT)
        # server.login(EMAIL_HOST, SMTP_PASS)
        # server.ehlo()
        # print("Connected..")
        # except:
        #     print('Something went wrong...')

user1 = User("Peace", "Me", 1990, is_staff=True)
person = User("Josh", "You", 2000)
# print(User.no_of_users)

print(user1.role)
    

# if user1.dob == 1990:
user1.send_mail()

# print(user1)
