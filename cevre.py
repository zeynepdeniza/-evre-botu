import discord

# İstekler değişkeni botun yetkilerini saklar
intents = discord.Intents.default()
# Mesaj okuma yetkisini etkinleştirme
intents.message_content = True
# Bir bot oluşturma ve yetkileri aktarma
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Plastik şişeler doğada ne kadar sürede kaybolur?'):
        await message.channel.send("$1000 yıl doğada kalırlar:)")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$cam şişeler doğada ne kaybolur?'):
        await message.channel.send("4000 yılda kaybolurlar :(")
    elif message.content.startswith('$Straforlar kaç yılda kaybolur?'):
        await message.channel.send("5000,5 ile 2 milyon yıl arasında kaybolur")
    elif message.content.startswith('Metaller doğada ne kadar sürede kaybolur?'):
        await message.channel.send("10 ile 100 yıl arasında kaybolur.")
    elif message.content.startswith('$Çevremizi korumak için ne yapabiliriz?'):
        await message.channel.send("Yerlere çöp atmayarak çevremizi temiz tutabiliriz!")
    elif message.content.startswith('$Kutuplar neden erimektedir?'):
        await message.channel.send("Küresel ısınma hem atmosferin hem de okyanus sularının sıcaklıklarının artmasını tetikleyerek buzulların her zamankinden daha hızlı erimesine neden olmaktadır.")

client.run("MTIyMTg3NTExNTc3MjM1MDQ2NA.GqnMAC.KKqHND52dgYozwjnLutt-d12PybzgYTur2j_Tc")

