@app.post("/request-password-reset/")
async def request_password_reset(email: EmailStr):
    # Генеруємо токен для скидання паролю і надсилаємо на email
    reset_token = generate_reset_token(email)
    send_reset_email(email, reset_token)
    return {"message": "Інструкції для скидання паролю надіслано"}

@app.post("/reset-password/")
async def reset_password(token: str, new_password: str):
    # Перевірка токену і скидання паролю
    email = verify_reset_token(token)
    if email:
        # Логіка для оновлення паролю
        update_user_password(email, new_password)
        return {"message": "Пароль успішно змінено"}
    return {"message": "Невірний або прострочений токен"}
