from fastapi import FastAPI, Depends, HTTPException
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr

class EmailSchema(BaseModel):
    email: EmailStr

conf = ConnectionConfig(
    MAIL_USERNAME = "your_email@example.com",
    MAIL_PASSWORD = "your_password",
    MAIL_FROM = "your_email@example.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "your_smtp_server",
    MAIL_FROM_NAME="Your Name",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

app = FastAPI()

@app.post("/send-email/")
async def send_email(email: EmailSchema):
    message = MessageSchema(
        subject="Верифікація електронної пошти",
        recipients=[email.email],
        body="Будь ласка, натисніть на посилання для верифікації вашої електронної пошти.",
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
    return {"message": "Лист для верифікації надіслано"}
