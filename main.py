import discord

client = discord.Client()

token = "ODA4NzQzMjU4ODIxNjIzODU5.YCK-2g.6AJC0vJQNH7X_RZSCVsqmu5zTYo"

bad = ["씨발", "ㅅㅂ", "쌍", "새끼", "느금", "년", "18"]

@client.event
async def on_ready():
    print(client.user.name)
    print("준비완료")
    game = discord.Game("실시간 서버정리 (24시간 운영 불가) ")
    await client.change_presence(status=discord.Status.online, activity=game)

    @client.event
    async def on_message(message):
        if message.author.id == client.user.id:
            return
        if message.content == "재철":
            await message.channel.send("배그 개못해!")
        if message.content == "ㅇㅈ":
            await message.channel.send("인정! 완전 핵 인정")
        if message.content == "인정":
            await message.channel.send("인정! 완전 핵 인정")
        if message.content == "재철이는":
            await message.channel.send("패드립퍼")
        if message.content == "배그":
            await message.channel.send("재철이는 브딱?실딱?")
        if message.content == "앙":
            await message.channel.send("너무달아~~!!")
        mc = message.content
        for i in bad:
            if i in mc:
                await message.channel.send(f"{message.author.mention}님이 비속어 사용으로 댓글이 삭제 되었습니다.")
                await message.delete()
        if message.content == "임배드 실행":
            embed = discord.Embed(color=discord.Colour.red(), title="주황상자", description="블로그")
            embed.add_field(name="필드", value="필드 내용", inline=False)
            embed.set_thumbnail(
                url="https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F469%2F2020%2F11%2F08%2F0000551742_002_20201108090020079.jpg&type=sc960_832")
            embed.set_image(
                url="https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F469%2F2020%2F11%2F08%2F0000551742_002_20201108090020079.jpg&type=sc960_832")
            await message.channel.send(embed=embed)
        if message.content.startswith("청소"):
            number = int(message.content.split()[1])
            await message.channel.purge(limit=number + 1)
            await message.channel.send(f"{number}개 메세지 삭제완료")

client.run(token)