from motor.motor_asyncio import AsyncIOMotorClient
client = AsyncIOMotorClient('mongodb')
db = client.auth
class Tool():
    @staticmethod
    async def already_verified(userid):
        return await db.users.find_one({'user_id': userid, 'user_checked': True})

    @staticmethod
    async def not_already_verified(userid):
        return await db.users.find_one({'user_id': userid, 'user_checked': False})

    @staticmethod
    async def set_token(userid,user_token):
        await db.users.insert_one({'user_id': userid, 'user_checked': False, 'user_token': user_token})
        return True
