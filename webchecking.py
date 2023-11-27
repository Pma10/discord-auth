from fastapi import FastAPI, Request, Path
from motor.motor_asyncio import AsyncIOMotorClient

uri = "mongodb"
client = AsyncIOMotorClient(uri)
db = client.auth
app = FastAPI()

@app.get("/auth/{user_id}/{user_token}")
async def authenticate_user(
    request: Request,
    user_id: int = Path(..., title="사용자 아이디", description="사용자의 아이디를 입력하세요."),
    user_token: str = Path(..., title="사용자 토큰", description="사용자의 고유 토큰을 입력하세요."),
):
    user_ip = request.client.host
    check_ip = await db.users.find_one({"user_ip": user_ip})    
    if check_ip:
        return "이미 해당 아이피에서 인증이 처리되었습니다."
    checking = await db.users.find_one({"user_id": user_id, "user_token": user_token})
    if checking is not None:
        result = await db.users.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "user_id": user_id,
                    "user_token": None,
                    "user_ip": user_ip,
                    "user_checked": True,
                }
            }
        )
        print(f"Matched {result.matched_count} document(s) and modified {result.modified_count} document(s).")


        return "인증되셨습니다."
    else:
        return "인증이 실패하였습니다."

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
