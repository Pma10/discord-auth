@TOOL.command()
async def 인증2(self,ctx):
    user_token = str(uuid.uuid4())
    user_id = ctx.author.id
    if await Tool.already_verified(user_id) is not None:
        return await ctx.respond('인증되었습니다. 축하드립니다.')
    if await Tool.not_already_verified(user_id) is None:
        await Tool.set_token(user_id,user_token)
        link = f'[인증링크](http://127.0.0.1:8001/auth/{user_id}/{user_token})'
        return await ctx.respond( f'{link}를 들어가 인증을 진행해주세요')
    else:
        return await ctx.respond('전에 부여받은 링크에 들어가서 인증을 진행해주세요!')
