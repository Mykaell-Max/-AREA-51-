import discord
import logging
import TOKEN
import asyncio

# token
TOKEN = TOKEN.token()

# logging
logging.basicConfig(level=logging.INFO)

# intents
intents = discord.Intents.all()
intents.members = True
# client
client = discord.Client(intents=intents)

# ----------------------------------------------------------------------------------------------------------------------
@client.event
async def on_ready():
    print('-' * 24)
    print(f'{client.user.name} online!')
    print(f'ID: {client.user.id}')
    print('-' * 24)
    channel = client.get_channel(----------secret-----------)
    online = discord.Embed(
        title='',
        color=15158332,
        description='BOT ONLINE'
    )
    await channel.send(embed=online)
# ----------------------------------------------------------------------------------------------------------------------
@client.event
async def on_message(message):

    # ------------------------------------------------------------------------------
    if message.author == client.user:
        return

    # ------------------------------------------------------------------------------
    if message.content.lower().startswith('p!'):

        # --------------------------------------------------------------------------
        if message.content.lower().startswith('p!help'):
            cmd = discord.Embed(
                title='**__Commands:__**',
                color=15158332,
                description='''**- p!invite:** Gives you the server's invite.
                
**- p!banner:** Shows the server's banner.
                
**- p!math:** Calculator. (For more information, use "p!mathhelp")

**- p!morse:** Converts the phrase to morse.

**- p!rmorse:** Converts the morse to phrase.

**- p!clear:** Clear the messages history. (Only admins)

**- p!binary:** Converts the number to its binary.

**- p!rbinary:** Converts the binary to its number.'''
            ).set_footer(text="[ 𝐏𝐨𝐥𝐲𝐠𝐥𝐨𝐭'𝐬 𝐡𝐨𝐮𝐬𝐞 ]", icon_url='https://cdn.discordapp.com/attachments/794688823950966784/796167627293982720/Logo.png')
            await message.channel.send(embed=cmd)

        # mathhelp-------------------------------------------------------------------
        elif message.content.lower().startswith('p!mathhelp'):
            mh = discord.Embed(
                title='**__Math help:__**',
                color=15158332,
                description='''**- Adding:** To add numbers, you must use " + ".
_Example:_
x + y + ... = z
1 + 1 = 2
                
**- Subtracting:** To subtract numbers, you must use " - ".
_Example:_
x - y - ... = z
1 - 1 = 0
                
**- Multiplying:** To multiply numbers, you must use " * ".
_Example:_
x * y * ... = z
2 * 2 = 4
                
**- Dividing:** To divide numbers, you must use " / ".
_Example:_
x / y = z
4 / 2 = 2

**- Power:** To power a number, you must use " \\** ".
_Example:_
x \\** y = z
2 \\** 3 = 8

**- Root:** To get the root of a number, you must consider two things:
First is the number you want the root (i'll call it " x ") and second is the root itself (i''l call it " ( 1 / y ) " ). For example: If you want a square-root, you have to consider " y " equals to 2 ( y = 2 ), if you want a cube-root, consider " y " as 3 ( y = 3 ). And so on.
_Example:_
x \\** (1 / y) = z
9 \\** (1 / 2) = 3

**Note:** Please remember to add space between numbers and operators!'''
            ).set_footer(text="[ 𝐏𝐨𝐥𝐲𝐠𝐥𝐨𝐭'𝐬 𝐡𝐨𝐮𝐬𝐞 ]", icon_url='https://cdn.discordapp.com/attachments/794688823950966784/796167627293982720/Logo.png')
            await message.channel.send(embed=mh)

        # banner---------------------------------------------------------------------
        elif message.content.lower().startswith('p!banner'):
            await message.channel.send('https://media.discordapp.net/attachments/772211661125451826/793678183257341992/Polyglots_house_-_banner_1.gif?width=863&height=431')

        # invite---------------------------------------------------------------------
        elif message.content.lower().startswith('p!invite'):
            await message.channel.send("> Polyglot's house invite: https://discord.gg/23PECHpqWq")

        # clean----------------------------------------------------------------------
        elif message.content.lower().startswith('p!clear'):
            if message.author.id != [secret]:
                await message.channel.send('> You have no permission!')
            else:
                try:
                    num = int(message.content[8:])
                    async for Message in message.channel.history(limit=num):
                        await Message.delete()
                    await message.channel.send(f'> Done! Cleared {num} messages!')
                except:
                    await message.channel.send(f'> You must inform a number!')

        # math-----------------------------------------------------------------------
        elif message.content.lower().startswith('p!math'):
            allwd = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '*', '/', '+', '-', '(', ')', '%', ' ', '']
            okay = True
            msg = message.content.lower()[7:].replace('{', '(').replace('}', ')').replace('[', '(').replace(']', ')')
            for c in msg:
                if c not in allwd:
                    await message.channel.send('> Invalid operation!')
                    okay = False
                    break
            if okay:
                try:
                    c = eval(msg)
                    cc = discord.Embed(
                        title='Result:',
                        color=15158332,
                        description=f'{msg} = {c}'
                    )
                    await message.channel.send(embed=cc)
                except:
                    await message.channel.send('> Invalid operation!')

        # morse----------------------------------------------------------------------
        # codif
        elif message.content.lower().startswith('p!morse'):
            try:
                morse = {' ': '/ ', 'a': '.- ', 'b': '-... ', 'c': '-.-. ', 'd': '-.. ', 'e': '. ', 'f': '..-. ',
                         'g': '--. ',
                         'h': '.... ', 'i': '.. ', 'j': '.--- ', 'k': '-.- ', 'l': '.-.. ', 'm': '-- ', 'n': '-. ',
                         'o': '--- ',
                         'p': '.--. ', 'q': '--.- ', 'r': '.-. ', 's': '... ', 't': '- ', 'u': '..- ', 'v': '...- ',
                         'w': '.-- ',
                         'x': '-..- ', 'y': '-.-- ', 'z': '--.. ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
                         '4': '....- ',
                         '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ', '9': '----. ', '0': '----- ',
                         '.': '.-.-.- ',
                         '?': '..--.. ', ',': '--..-- ', '!': '-.-.-- '}
                new = ''
                phrase = message.content.lower()[8:].strip()
                for l in phrase:
                    letter = morse[f"{l}"]
                    new += letter
                ph = discord.Embed(
                    title='**__Morse code__**',
                    color=15158332,
                    description=f'''**Phrase:**
{message.content[8:]}
    
**Morse:**
{new}''').set_footer(text="[ 𝐏𝐨𝐥𝐲𝐠𝐥𝐨𝐭'𝐬 𝐡𝐨𝐮𝐬𝐞 ]", icon_url='https://cdn.discordapp.com/attachments/794688823950966784/796167627293982720/Logo.png')
                await message.channel.send(embed=ph)
            except:
                await message.channel.send('> Invalid phrase!')

        # descodif
        elif message.content.lower().startswith('p!rmorse'):
            try:
                morse = {'/': ' ', '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
                         '--.': 'g',
                         '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n',
                         '---': 'o',
                         '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v',
                         '.--': 'w',
                         '-..-': 'x', '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2', '...--': '3',
                         '....-': '4',
                         '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
                         '.-.-.-': '.',
                         '..--..': '?', '--..--': ',', '-.-.--': '!'}
                new = ''
                nw = []
                newphr = ''
                phrase = message.content.lower()[9:].strip().split()
                phrase.append('/')
                for e in phrase:
                    if e == '/':
                        nw.append(new)
                        new = ''
                    else:
                        letter = morse[e]
                        new += letter
                for w in nw:
                    newphr += f'{w} '
                n = newphr.capitalize()
                cm = discord.Embed(
                    title='**__Morse code__**',
                    color=15158332,
                    description=f'''**Morse:**
{message.content[9:]}
    
**Phrase:**
{n}''').set_footer(text="[ 𝐏𝐨𝐥𝐲𝐠𝐥𝐨𝐭'𝐬 𝐡𝐨𝐮𝐬𝐞 ]", icon_url='https://cdn.discordapp.com/attachments/794688823950966784/796167627293982720/Logo.png')
                await message.channel.send(embed=cm)
            except:
                await message.channel.send('> Invalid morse!')

        # binary--------------------------------------------------------------------
        # num => binary
        elif message.content.lower().startswith('p!binary'):
            try:
                num = int(message.content[9:])
                b = ''
                while True:
                    if num == 1 or num == 0:
                        b += f'{str(num)} '
                        break
                    bi = num % 2
                    num //= 2
                    b += f'{str(bi)} '
                l = b.split()
                l.reverse()
                b = ''
                for n in l:
                    b += f'{str(n)}'
                bb = discord.Embed (
                    title='**__Binary__**',
                    color=15158332,
                    description=f'''**Number:**
{int(message.content[9:])}

**Binary:**
{b}''').set_footer(text="[ 𝐏𝐨𝐥𝐲𝐠𝐥𝐨𝐭'𝐬 𝐡𝐨𝐮𝐬𝐞 ]", icon_url='https://cdn.discordapp.com/attachments/794688823950966784/796167627293982720/Logo.png')
                await message.channel.send(embed=bb)
            except:
                await message.channel.send('> You should inform a valid number.')

        # binary => num
        elif message.content.lower().startswith('p!rbinary'):
            try:
                bina = message.content[10:].strip()
                count = num = 0
                lst = []
                for n in bina:
                    lst.append(n)
                lst.reverse()
                for n in lst:
                    num += int(n) * (2 ** count)
                    count += 1
                n = discord.Embed(
                    title='**__Binary__**',
                    color=15158332,
                    description=f'''**Binary:**
{bina}

**Number:**
{num}''').set_footer(text="[ 𝐏𝐨𝐥𝐲𝐠𝐥𝐨𝐭'𝐬 𝐡𝐨𝐮𝐬𝐞 ]", icon_url='https://cdn.discordapp.com/attachments/794688823950966784/796167627293982720/Logo.png')
                await message.channel.send(embed=n)
            except:
                await message.channel.send('> You should inform a valid binary.')
                
        # unknown command--------------------------------------------
        else:
            await message.channel.send('> Invalid command!\n> Type "p!help" to see a list of commands!')

# run token--------------------------------------------------------------------------
client.run(TOKEN)
