from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()
app.state.limiter = limiter

@app.post("/contacts/")
@limiter.limit("5/minute")
async def create_contact(contact: ContactModel):
    # Логіка створення контакту
    return {"message": "Контакт створено"}
