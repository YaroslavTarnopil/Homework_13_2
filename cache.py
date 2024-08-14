import aioredis
from fastapi import Depends

redis = aioredis.from_url(os.getenv("REDIS_URL"))

async def cache_user(user_id: str, user_data: dict):
    await redis.set(f"user:{user_id}", str(user_data))

async def get_cached_user(user_id: str):
    user = await redis.get(f"user:{user_id}")
    if user:
        return eval(user)
    return None

@app.post("/login/")
async def login(user: UserLogin):
    # Авторизація користувача
    cached_user = await get_cached_user(user.id)
    if cached_user:
        return cached_user
    
    # Якщо користувач не закешований
    user_data = {"id": user.id, "name": user.name}  # Приклад
    await cache_user(user.id, user_data)
    return user_data
