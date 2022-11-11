#from sqlite3 import Time
import discord
from discord.ext import commands, tasks
#import asyncio
import time
#from time import sleep
import random
from discord import Member
import os
import asyncio
import googletrans
from io import BytesIO
#from typing import Union, Optional
from petpetgif import petpet as petpetgif
import requests
#import imagecomparison
import re
import flag
from datetime import datetime, timedelta
now = datetime.now()
#secondstillrun = ((timedelta(hours=24) - (now - now.replace(hour=9, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600))
#tdd = timedelta(seconds=secondstillrun)
futuretime = str((now + timedelta( seconds= ((timedelta(hours=24) - (now - now.replace(hour=9, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600)) )).replace(microsecond=0))
#uturedate = now+tdd
#print(futuredate)
#timevalues = type('', (), {})()
#timevalues.value = [secondstillrun, futuredate]
#timevalues.stamp = futuredate
#def TimeMemRW(InputVV, read):
#    if read:
#        return timevalues.value
#    else:
#        timevalues.value = InputVV

def getNation(codein):
    langtonatexp = {
    'af': 'ZA',
    'agq': 'CM',
    'ak': 'GH',
    'am': 'ET',
    'ar': 'AE',
    'as': 'IN',
    'asa': 'TZ',
    'az': 'AZ',
    'bas': 'CM',
    'be': 'BY',
    'bem': 'ZM',
    'bez': 'IT',
    'bg': 'BG',
    'bm': 'ML',
    'bn': 'BD',
    'bo': 'CN',
    'br': 'FR',
    'brx': 'IN',
    'bs': 'BA',
    'ca': 'ES',
    'cgg': 'UG',
    'chr': 'US',
    'cs': 'CZ',
    'cy': 'GB',
    'da': 'DK',
    'dav': 'KE',
    'de': 'DE',
    'dje': 'NE',
    'dua': 'CM',
    'dyo': 'SN',
    'ebu': 'KE',
    'ee': 'GH',
    'en': 'GB',
    'el': 'GR',
    'es': 'ES',
    'et': 'EE',
    'eu': 'ES',
    'ewo': 'CM',
    'fa': 'IR',
    'fil': 'PH',
    'fr': 'FR',
    'ga': 'IE',
    'gl': 'ES',
    'gsw': 'CH',
    'gu': 'IN',
    'guz': 'KE',
    'gv': 'GB',
    'ha': 'NG',
    'haw': 'US',
    'he': 'IL',
    'hi': 'IN',
    'ff': 'CN',
    'fi': 'FI',
    'fo': 'FO',
    'hr': 'HR',
    'hu': 'HU',
    'hy': 'AM',
    'id': 'ID',
    'ig': 'NG',
    'ii': 'CN',
    'is': 'IS',
    'it': 'IT',
    'ja': 'JP',
    'jmc': 'TZ',
    'ka': 'GE',
    'kab': 'DZ',
    'ki': 'KE',
    'kam': 'KE',
    'mer': 'KE',
    'kde': 'TZ',
    'kea': 'CV',
    'khq': 'ML',
    'kk': 'KZ',
    'kl': 'GL',
    'kln': 'KE',
    'km': 'KH',
    'kn': 'IN',
    'ko': 'KR',
    'kok': 'IN',
    'ksb': 'TZ',
    'ksf': 'CM',
    'kw': 'GB',
    'lag': 'TZ',
    'lg': 'UG',
    'ln': 'CG',
    'lt': 'LT',
    'lu': 'CD',
    'lv': 'LV',
    'luo': 'KE',
    'luy': 'KE',
    'mas': 'TZ',
    'mfe': 'MU',
    'mg': 'MG',
    'mgh': 'MZ',
    'ml': 'IN',
    'mk': 'MK',
    'mr': 'IN',
    'ms': 'MY',
    'mt': 'MT',
    'mua': 'CM',
    'my': 'MM',
    'naq': 'NA',
    'nb': 'NO',
    'nd': 'ZW',
    'ne': 'NP',
    'nl': 'NL',
    'nmg': 'CM',
    'nn': 'NO',
    'nus': 'SD',
    'nyn': 'UG',
    'om': 'ET',
    'or': 'IN',
    'pa': 'PK',
    'pl': 'PL',
    'ps': 'AF',
    'pt': 'PT',
    'rm': 'CH',
    'rn': 'BI',
    'ro': 'RO',
    'ru': 'RU',
    'rw': 'RW',
    'rof': 'TZ',
    'rwk': 'TZ',
    'saq': 'KE',
    'sbp': 'TZ',
    'seh': 'MZ',
    'ses': 'ML',
    'sg': 'CF',
    'shi': 'MA',
    'si': 'LK',
    'sk': 'SK',
    'sl': 'SI',
    'sn': 'ZW',
    'so': 'SO',
    'sq': 'AL',
    'sr': 'RS',
    'sv': 'SE',
    'sw': 'TZ',
    'swc': 'CD',
    'ta': 'IN',
    'te': 'IN',
    'teo': 'UG',
    'th': 'TH',
    'ti': 'ER',
    'to': 'TO',
    'tr': 'TR',
    'twq': 'NE',
    'tzm': 'MA',
    'uk': 'UA',
    'ur': 'PK',
    'uz': 'UZ',
    'vai': 'LR',
    'vi': 'VN',
    'vun': 'TZ',
    'xog': 'UG',
    'yav': 'CM',
    'yo': 'NG',
    'zh': 'CN',
    'zu': 'ZA'
  }
    try:
        return langtonatexp[codein]
    except:
        return None


#import traceback
setprefix = "//"
petalias=["pat","petpet","patpat"]
petaliaspref = [setprefix + sub for sub in petalias]
petaliaspref.append("//pet")

femboygifs = ["cum"]
CHANNEL_MENTION_PATTERN = re.compile('<#(\\d+)>')
EMOJI_PATTERN = re.compile('<:[^:]+?:(\\d+)>')
USER_MENTION_PATTERN = re.compile('<@(\\d+)>')
ROLE_MENTION_PATTERN = re.compile('<@&(\\d+)>')

def returnIQ(iqFLOAT):
    match iqFLOAT:
        case x if x<=1:
            return("cum")
        case x if 1<x<=30:
            return("cum")
        case x if 30<x<=60:
            return("cum")
        case x if 60<x<=100:
            return("cum")
        case x if 100<x<=110:
            return("cum")
        case x if 110<x<=120:
            return(f"cum")
        case x if 120<x<=150:
            return("cum")
        case x if 150<x<300:
            return("cum")
        case x if 300<=x<=400:
            return("cum")
        case x if 400<x:
            return("cum")
        case _:
            return("rotten cum (bitch)")


regex = r'cum'

# Scheme (HTTP, HTTPS, FTP and SFTP):
regex += r'cum'

 # www:
regex += r'cum'

regex += r'cum'

 # Host and domain (including ccSLD):
regex += r'cum'

 # TLD:
regex += r'cum'

 # IP Address:
regex += r'|cum'   

regex += r'cum'

 # Port:
regex += r'cum'

 # Query path:
regex += r'cum'

regex += r'cum'

def get_emote(emoji):               #idk tf this does but its korgus now - me 2022
    """                 
   cum
    """
    lookup, eid = emoji, None
    if ':' in emoji:
        # matches custom emote
        server_match = re.search(r'cum', emoji)
        # matches global emote
        custom_match = re.search(r'cum', emoji)
        if server_match:
            lookup, eid = server_match.group(1), server_match.group(2)
        elif custom_match:
            lookup, eid = custom_match.group(1), None
        else:
            lookup, eid = emoji.split('cum')
        try:
            eid = int(eid)
        except (ValueError, TypeError):
            eid = None
    return eid

translator = googletrans.Translator()
#import dotenv
#NOT USING THIS FUCK THIS LMAO
#from dotenv import load_dotenv
RE_TEST = re.compile('sex', re.IGNORECASE)
#global shitter
#shitter = 0
objectF = type('', (), {})()
bufferMN = type('', (), {})()
imagedata = type('', (), {})()
shitpostermode = type('', (), {})()
reactionmode = type('', (), {})()
#Bot = type('',(),{})()
reactionmode.value = True
shitpostermode.value = False
imagedata.value = None
bufferMN.value = ""
objectF.value = 80
def bufferMImportVaule(stringV, boolV):
    if boolV:
        return bufferMN.value
    else:
        bufferMN.value = stringV
def ShitpostingMode(InputVV, read):
    if read:
        return shitpostermode.value
    else:
        shitpostermode.value = InputVV
def ReactionMode(InputVV, read):
    if read:
        return reactionmode.value
    else:
        reactionmode.value = InputVV
def AttRead(inputV, boolV):
    if boolV:
        return imagedata.value
    else:
        imagedata.value = inputV

def incrementValueInObject(objectF):
    objectF.value = objectF.value + 1
def IfInString(String, SubstringList, CaseSens=True):
    if CaseSens:
        return any(x in String for x in SubstringList)
    else:
        return any(x.lower() in String.lower() for x in SubstringList)
        
#load_dotenv() //FUCK THIS LMAO
TOKEN = "MTA0MDQwMjQ3MDc3OTc0ODQzMw.GOe-RL.LfWmww8AhK9C0SCvMNaSX8U8fE6W_IQMjrJXSI"
intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = setprefix, activity=discord.Activity(type=discord.ActivityType.playing, name="GNU C Compiler"), intents=intents)

@client.event
async def on_ready(): 
    print('Logged in as: {}'.format(client.user))
    #await client.get_channel(921945359243153448).send(f"Morning message will be sent at this timestamp:\n``{str((now + timedelta( seconds= ((timedelta(hours=24) - (now - now.replace(hour=9, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600)) )).replace(microsecond=0))}``")
    morning_msg.start()

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    #print(msg.content)
    if msg.content.strip() == "cum": ##"<@1026940282278776954>":
        #msg.reply("https://media.discordapp.net/attachments/959447085269266442/1003714243599794336/ezgif.com-gif-maker_6.gif")
        await msg.reply("cum")
    if re.search("cum", msg.content, re.IGNORECASE):
        print("cum")
        await msg.reply(f"cum")

    if ShitpostingMode("", True):
        if re.search("cum", msg.content, re.IGNORECASE) or re.search("cum", msg.content, re.IGNORECASE): #or re.search("dess", msg.content, re.IGNORECASE):
            await msg.reply("cum", mention_author=True)
        if re.search("cum", msg.content, re.IGNORECASE) or re.search("cum", msg.content, re.IGNORECASE) or re.search("cum", msg.content, re.IGNORECASE) or re.search("cum", msg.content, re.IGNORECASE): #or re.search("dess", msg.content, re.IGNORECASE):
            await msg.reply(femboygifs[random.randrange(0,len(femboygifs)-1)], mention_author=True)
        if re.search("cum", msg.content, re.IGNORECASE) or re.search("cum", msg.content, re.IGNORECASE):
            await msg.reply("cum", mention_author=True)#https://cdn.discordapp.com/attachments/941621893436424242/1026098045164732496/unknown.png
        if re.search("cum", msg.content, re.IGNORECASE) or re.search("cum", msg.content, re.IGNORECASE):
            await msg.reply("cum", mention_author=True)#https://cdn.discordapp.com/attachments/941621893436424242/1026098045164732496/unknown.png
        if re.search("cum", msg.content, re.IGNORECASE):
            #await msg.reply("HOLY SHIT!!!! YOU SAID THE S*X WORD!!!! :bangbang: :bangbang: :interrobang: :moyai:\nI AM PINGING THE OWNER RIGHT NOW!!!!!!!!! :bangbang: :bangbang:") ##("<@463162198181806082>")
            await msg.reply("cum")
        if "@" not in msg.content:
            if 'i am ' in msg.content.lower():
                await msg.reply('cum '+msg.content[msg.content.lower().index('cum ')+5:len(msg.content)]+' cum')
            if 'i\'m ' in msg.content.lower():
                await msg.reply('cum '+msg.content[msg.content.lower().index('i\'m ')+4:len(msg.content)]+' cum')
            if 'im ' in msg.content.lower():
                if msg.content.lower().index('cum ') == 0 or msg.content[msg.content.lower().index('cum ')-1] == ' ':
                    await msg.reply('cum '+msg.content[msg.content.lower().index('im ')+3:len(msg.content)]+' cum')

    if ReactionMode("", True):
        if IfInString(msg.content, ["cum","cum","cum","cum","cum"],False):
            await msg.add_reaction("cum")
        try:
            if discord.utils.get(msg.guild.roles, id=1029465397935747243) in msg.author.roles:
                await msg.add_reaction("cum")
        except:
            #print(f"{msg.content}, {msg.author};;;; This is not a user.")
            pass
            #await msg.reply("This message fucked up role lookup, what the fuck?\n<@444785578152558592>")
        if IfInString(msg.content,["cum"],False) and not IfInString(msg.content,["cum"],False):
            await msg.add_reaction("cum")
            await msg.add_reaction("cum")
        elif "sussy" in msg.content.lower():
            match random.randint(1, 2):
                case 1:  
                    await msg.add_reaction("cum")
                case 2:
                    await msg.add_reaction("cum")
                    await msg.add_reaction("cum")
        if IfInString(msg.content,["cum","cum","cum","cum","cum","cum","cum"],False):
            await msg.add_reaction(random.choice(["cum","cum","cum"]))
        if IfInString(msg.content,["cum","cum","cum"],False):
            await msg.add_reaction("cum")
        if "cum" in msg.content:
            if msg.reference:
                await msg.reference.resolved.reply("cum")
            else:
                await msg.channel.send("cum")

    
    if msg.attachments != [] and msg.content.startswith(tuple(petaliaspref)):
        AttRead([msg.attachments[0].url, msg.id], False)
    if msg.content.lower().startswith("cum") and msg.author != client.user and msg.reference:
        if msg.reference.resolved:
            print(msg.reference.resolved.content)
            await msg.reply(f"cum ``{msg.reference.resolved.content}``")
        else:
            await msg.channel.send("cum")

 
    if msg.content.lower().startswith("cum"):
        global bufferM
        if msg.author != client.user and msg.reference:
            if msg.reference.resolved:
                bufferMImportVaule(msg.reference.resolved.content, False)
            else:
                await msg.channel.send("cum")
                return
        else:
            bufferMImportVaule(msg.content[len("cum")+1:], False)
        bufferM = bufferMImportVaule("", True)
        if "@everyone" in bufferM or "cum" in bufferM:
            await msg.channel.send("cum")
            return
        if "cum" in bufferM:
            #await msg.channel.send("Pls remove le funny ``@`` from your nick input. Thanks")
            bufferM = bufferM.replace("cum","cum")
        #print(f"{bufferM}, {type(bufferM)}")
        #print(translator.detect(bufferM).lang)
        message_destination = translator.detect(bufferM).lang #TODO: add lang filter 
        print(message_destination)
        if type(message_destination) == list:
            message_destination = random.choice(message_destination)
        if message_destination == "cum":
            await msg.channel.send("cum")
            return
        translated_message = translator.translate(bufferM,src=message_destination, dest="en")
        returned_nation = getNation(message_destination)
        flagbuf = flag.flag(returned_nation) if returned_nation != None else "``[no flag]``"
        await msg.channel.send(f"``{bufferM}`` -> ``{translated_message.text}``, cum`` ->  cum | ``cum``")#.format(bufferM, translated_message.text, msg.author, message_destination, "en"))
        return
        
    await client.process_commands(msg)

@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def avatar_old(ctx, member:discord.Member = None):
    member = ctx.author if not member else member
    userAvatarUrl = member.avatar.url
    embed=discord.Embed(title=f"cum")
    embed.set_image(url=f'{userAvatarUrl}')
    await ctx.send(embed=embed)

@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == "cum" and discord.utils.get(reaction.message.guild.roles, id=941621150293843979) in user.roles:
        print(reaction.message)
        await reaction.message.pin()


@client.event
async def on_reaction_remove(reaction, user):
    if reaction.emoji == "cum" and discord.utils.get(reaction.message.guild.roles, id=941621150293843979) in user.roles:
        if not "cum" in [ reaction.emoji for reaction in  reaction.message.reactions]:
            print(reaction.message)
            await reaction.message.unpin()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'cum')
    else:
        print(error)


@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def pussy(ctx, member:discord.Member = None):
    if not ShitpostingMode("", True):
        await ctx.reply(f"cum``")
        return
    member = ctx.author if not member else member
    rand_depth = random.uniform(1, 30)
    depth_inches = rand_depth * 0.393701
    mesg = f"pussy depth is {round(rand_depth, 2)}cm / {round(depth_inches, 2)} inches deep! <:trolley:987681249759989780>"
    print(mesg)
    await ctx.channel.send(f"Result: {member.name}'s {mesg}")

@client.command(pass_context=True)
##@commands.has_permissions(administrator=True)

##TODO: Fix this trashy version of clear: add int type checking n stuff - he fixed it :D -Local shower shitter#6969
##async def clear(ctx, limit: int=None):
##    if type(limit) != int:
##        await ctx.reply(f"That can't work, right? You can't clear an invalid amount of messages!")
##        return
##    if ctx.author.id == 444785578152558592:
##        if limit <= 0:
##            await ctx.reply(f"That can't work, right? You can't clear ``{limit}`` messages!")
##            return
##        await ctx.channel.purge(limit=limit)
##        await ctx.send(f'{limit} messages have been cleared by {ctx.author.name}.')
##        await ctx.message.delete()
##    else:
##        await ctx.reply("https://tenor.com/view/rat-toilet-mouse-toiler-ew-gif-21327850")

async def clear(ctx, amount = "0"):
    if ctx.author.id == 444785578152558592:
        pass
    else:
        await ctx.reply("cum")
        return
    if amount == "all":
        await ctx.channel.purge(limit=50)
        await ctx.send("cum")
        print("cum")
    else :
        try:
            amount = int(amount)
        except ValueError:
            await ctx.reply(f"cum", delete_after=5)
            return
        if amount <= 0:
            await ctx.reply(f"cum``{amount}`` messages!", delete_after=5)
            return
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"cum", delete_after=5)
        print(f'``{amount}`` cum')



@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def bussy(ctx, member:discord.Member = None):
    if not ShitpostingMode("", True):
        await ctx.reply(f"cum")
        return
    member = ctx.author if not member else member
    rand_depth = random.uniform(1, 50)
    depth_inches = rand_depth * 0.393701
    mesg = f"cum"
    print(mesg)
    await ctx.channel.send(f"Result: {member.name}'s {mesg}")

@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def iqtest(ctx, member:discord.Member = None):
    if not ShitpostingMode("", True):
        await ctx.reply(f"cum")
        return
    member = ctx.author if not member else member
    rand_depth = random.uniform(1, 300)
    rand_depth2 = random.uniform(0.2, 2)
    xff = round(rand_depth*rand_depth2, 2)
    if member.id == 444785578152558592:
        xff = 500
    elif member.id == 371425463060398090:
        xff= 70
    mesg = f"IQ is {xff}"
    print(mesg)
    await ctx.channel.send(f"Result: {member.name}'s {mesg}.\n{returnIQ(xff)}")

@client.command()
async def avatar(ctx, avamember: discord.Member = None):
    if avamember == None:
        member = ctx.author if not avamember else avamember
        userAvatarUrl = member.avatar.url
        embed = discord.Embed(title=('{}\'cum))
        embed.set_image(url='{}'.format(userAvatarUrl))
        await ctx.reply(embed=embed, mention_author=True) 
    else:
        userAvatarUrl = avamember.avatar.url
        embed = discord.Embed(title=('{}\'s Avatar'.format(avamember.name)), colour=discord.Colour.red())
        embed.set_image(url='{}'.format(userAvatarUrl))
        await ctx.reply(embed=embed, mention_author=True) 


@client.command(pass_context=True, aliases=petalias)
async def pet(ctx, thing: str = ""):
    print(type(thing))
    print(AttRead("", True))
    if AttRead("", True) == None:
        AttRead(["",0], False)
    #print(ctx.attachments == [])
    #print(ctx.attachments)
    try:
        print(re.compile(regex, re.IGNORECASE).search(thing).group(0).strip())
        itworks = True
    except:
        print("cum")
        itworks = False
        pass
    #print(f"{type(thing)};; {thing}")
    #print(USER_MENTION_PATTERN.findall(thing))
    if bool(re.match(EMOJI_PATTERN, thing)):
        #print(type(EMOJI_PATTERN.findall(thing)))
        buf = (int(EMOJI_PATTERN.findall(thing)[0]))
        #print("fuckup 1")
        url = buf
        #print(url)
        if not url:
            await ctx.reply('cum')
            return
        response = requests.get(f"cum")
    elif bool(re.match(USER_MENTION_PATTERN, thing)):
        #print("hello")
        a = (int(USER_MENTION_PATTERN.findall(thing)[0]))
        zf = client.get_user(a)
        buf = a
        url = zf.avatar.url 
        response = requests.get(url)
    elif AttRead("", True)[1] == ctx.message.id: ##TODO: Dodaj ctx provjeru za korisnika tako da je attread jednak ctx.id
        buf = ctx.author.id
        url = AttRead("", True)[0]
        response = requests.get(url)

    elif itworks:
        find_urls_in_string = re.compile(regex, re.IGNORECASE)
        urlBF = find_urls_in_string.search(thing)
        try:
            #url = 
            if urlBF.group(0).strip().endswith(">"): url = urlBF.group(0).strip()[:-1]
            else: url = urlBF.group(0).strip()
            buf = urlBF.group(3).strip()
            response = requests.get(url)
        except:
            await ctx.reply('cum')
            return
#    elif ctx.attachment and type(thing) != None:
#        url = message.attachments[0].url
#        buf = ctx.author.id
    else:
        await ctx.reply('cum')
        return

    source = BytesIO(response.content) # file-like container to hold the emoji in memory
    dest = BytesIO() # container to store the petpet gif in memory
    try:
        petpetgif.make(source, dest)
    except:
        await ctx.reply('cum')
        return
    dest.seek(0) # set the file pointer back to the beginning so it doesn't upload a blank file.
    await ctx.reply(file=discord.File(dest, filename=f"cum"))

@client.command()
async def clussy(ctx):
    if not ShitpostingMode("", True):
        await ctx.reply(f"cum``")
        return
    embed=discord.Embed(title=f"{ctx.author} cum")
    #embed=discord.Embed("")
    embed.set_image(url=f'cum')
    await ctx.reply(embed=embed, mention_author=True)

@client.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    print(ctx.message.author.id)
    if ctx.message.author.id != 444785578152558592:
        await ctx.reply("cum")
        return
    if len(nick) >= 32:
        await ctx.reply("cum")
        return
    await member.edit(nick=nick)
    await ctx.reply(f'cum')


@client.command(pass_context=True)
@commands.cooldown(1, 15, commands.BucketType.user)
async def botname(ctx):
    if not ShitpostingMode("", True):
        await ctx.reply(f"cum")
        return
    nick = ctx.message.content[len("botname")+3:]
    if len(nick) >= 32:
        await ctx.reply("cum")
        return
    if "@everyone" in nick or "@here" in nick:
        await ctx.reply("cum")
        return
    if "@" in nick:
        await ctx.reply("cum")
        return
    await ctx.message.guild.me.edit(nick=nick)
    await ctx.reply(f'cum')#

#@client.command(pass_context=True)
#async def getpfp(ctx):
#    if ctx.message.author.id != 444785578152558592:
#        await ctx.reply("Nope, blocked + ratio + cope + seethe + mald + you lose + no admin + trolled + no bitches")
#        return
#    await ctx.reply("Finding this specified pfp:\nhttps://cdn.discordapp.com/attachments/967479617734705153/1032350270119751741/unknown.png")
#    for i in ctx.guild.members:
#        try:
#            ffb = imagecomparison.imagematch(f"{i.avatar.url}")
#            print(ffb, i)
#            if ffb[1] > 0.40:
#                print(f"found match!!!!!!!!!!!!!!!!!!!!!!!!!!! {i}")
#                await ctx.author.send(f"Perhaps a match?, {i} , {i.avatar.url}")
#        except:
#            await ctx.author.send(f"Uh oh, something went wrong for user {i}, couldn't fetch their image.")
#        time.sleep(1)
#    ctx.reply("Image search complete!")
#    #print(imagecomparison.imagematch(f"{ctx.author.avatar.url}"))


@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def shitter(ctx):
    if not ShitpostingMode("", True):
        await ctx.reply(f"cum")
        return
#    incrementValueInObject(objectF)
#    await ctx.reply(f"<@{ctx.message.author.id}> shits on {random.choice(ctx.guild.members).mention}. Total shits: {objectF.value}")
    await ctx.reply("cum")

##@commands.cooldown(1, 1, commands.BucketType.user)
@client.command(pass_context=True)
async def toggleshit(ctx):
    if ctx.message.author.id != 444785578152558592:
        await ctx.reply("cum")
        return
    ShitpostingMode(not ShitpostingMode("", True), False)
    await ctx.reply(f"cum")

@client.command(pass_context=True)
async def togglereactions(ctx):
    if ctx.message.author.id != 444785578152558592:
        await ctx.reply("cum")
        return
    ReactionMode(not ReactionMode("", True), False)
    await ctx.reply(f"cum`")

@client.command(aliases=["mcrnow"])
async def member_count(ctx):

    a=ctx.guild.member_count
    b=discord.Embed(title=f"cum))
    await ctx.send(embed=b)

@tasks.loop(count=None,)
async def morning_msg():
    print(((timedelta(hours=24) - (now - now.replace(hour=9, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600)))
    #await asyncio.sleep((timedelta(hours=24) - (now - now.replace(hour=18, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600))
    #await client.get_channel(921945359243153448).send("Current time is exactly 6:00PM")
    await asyncio.sleep((timedelta(hours=24) - (now - now.replace(hour=9, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600))
    await client.get_channel(921945359243153448).send("cum")


#@client.event
#async def on_error(event, *args, **kwargs):
#    message = args[0] #Gets the message object
#    logging.warning(traceback.format_exc()) #logs the error
#    await client.send_message(message.channel, "Error encoutnered, report to dev (Uru)!!\nhttps://tenor.com/view/computer-smash-rage-flash-gif-19862483") #send the message to the channel
#bot = client
client.lavalink_nodes = [
#{"host": "lv.cowcat.cf", "port": 2223, "password": "derpylava", "https": False},
    {"host": "lavalink.botsuniversity.ml", "port": 443, "password": "mathiscool", "https": True },
    {"host": "lavalink2.botsuniversity.ml", "port": 443, "password": "mathiscool", "https": True },
    {"host": "node2.lewdhutao.tech", "port": 443, "password": "lewdhutao", "https": True },
]
client.spotify_credentials = {
    'client_id': '905fab4830e44104b41a5ffe03ee695f',
    'client_secret': '696fa36e81824c00a401b70fb7744315'
}
client.load_extension('dismusic')
client.run(TOKEN)
#https://media.tenor.com/MW1mSw50oK0AAAAC/clown-clown-meme.gif
TOKEN = "MTA0MDQwMjQ3MDc3OTc0ODQzMw.Gg0TfB.FVGfhLrjmt4XqdB16hzco_Qa6c1LF0zV6DtAeM"
