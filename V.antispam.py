from discord.ext import commands
import asyncio

cilent = commands.Bot(commands_prefix="?")


@cilent.event
async def on_ready():
    print("ready")
    while True:
        print("cleared")
        await asyncio.sleep(10)
        with open("spam_detect.txt","r+")as file:
            file.truncate(0)

@cilent.event
async def on_message(message):
    counter = 0
    with open("spam_detect.txt","r+")as file:
        for lines in file:
            if lines.strip("\n") == str (message.author.id):
                counter+=1
                file.writelines(f"{str(message.author.id)}\n")
                if counter > 5:
                    await  message.guild.ban(message.author, reason="spam")
                    await  asyncio.sleep(1)
                    await message.guild.unban(message.author)
                    print("uh oh")
cilent.run("NzkyMzU4MDczMDIwNDQ4Nzg4.X-ci9Q.lvR84w9UfkWnlnhd-CeCSAD75i4")
