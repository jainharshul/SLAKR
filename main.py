import random
import discord.ext
from discord.ext import commands

user_name_list = []

client = discord.Client()
prefix = "#"
client = commands.Bot(command_prefix=prefix)
say_name = ''


@client.command()
async def info(ctx):
    await ctx.send('''
        This is a Fun Bot that is currently in development, the commands that this bot provides so far include:
        - hello (Registers all new users)
        - #info (shows all commands and their functions)
        - #say (repeats what you type after '#say')
        - #changename (changes the name you registered  with)
        - #flipacoin (flips a coin)
        - #chooseone (chooses a name from a list you provide)
        That's all for now stay tuned for more
        ''')


@client.command()
async def say(ctx, *, content: str):
    await ctx.send(content)


@client.command()
async def flipacoin(ctx):
    coin = [1,2]
    choice = random.choice(coin)
    await ctx.send("Fliping a quarter...")
    if choice == 1:
        await ctx.send("Its Heads!")
    else:
        await ctx.send("Its Tails!")


@client.command()
async def new(ctx):
    my_file = open("nick_names.txt", "a")
    user_name = str(ctx.author)
    if str(user_name) not in userid_name_dic:
        await ctx.channel.send("What do you want me to call you?")

        def check(m):
            return m.author.id == ctx.author.id

        message = await client.wait_for('message', check=check)
        await ctx.send(f'Hello, {message.content}! I will remember you now!')
        userid_name_dic[user_name] = message.content
        my_file.write(f'{user_name}:{message.content}\n')

    else:
        await ctx.channel.send('You are already registered')
        await ctx.channel.send("If you want to change your name do '#changename'")
    my_file.close()


@client.command()
async def changename(ctx):
    user_name = str(ctx.author)
    await ctx.channel.send("What is your new name?")

    def check(m):
        return m.author.id == ctx.author.id

    message = await client.wait_for('message', check=check)
    await ctx.send(f'Hello, {message.content}! I will remember you now!')
    change_txt(userid_name_dic[user_name], message.content)
    userid_name_dic[user_name] = message.content
    nicknames = open('nick_names.txt')
    nicknames.close()


@client.command()
async def chooseone(ctx):
    await ctx.channel.send("Give me a list of names separated by a comma")

    def check(m):
        return m.author.id == ctx.author.id

    message = await client.wait_for('message', check=check)
    x = message.content.split(',')
    rand = random.choice(x)

    await ctx.channel.send(f'''You gave me the following names: {x}
I choose {rand}!''')


userid_name_dic = {}


@client.command()
async def read(ctx):
    nicknames = open('nick_names.txt', 'r')
    user_code = ''
    user_name = ''
    for line in nicknames:
        user_code_name = line.split(':')
        user_code = user_code_name[0]
        user_name = user_code_name[1]
    await ctx.send(f'the username is {user_code} and the nickname is {user_name}')


@client.event
async def on_ready():
    print("Everything's all ready to go~")


def read_txt_build_dic():
    names = open('nick_names.txt', 'r')

    for line in names:
        user_code_name = line.split(':')
        userid_name_dic[user_code_name[0]] = user_code_name[1]
    names.close()


def change_txt(previous, newer):
    fin = open("nick_names.txt", "rt")
    data = fin.read()
    data = data.replace(previous, newer)
    fin.close()
    fin = open("nick_names.txt", "wt")
    fin.write(data)
    fin.close()


@client.event
async def on_message(message):
    message.content = message.content.lower()
    user = message.author
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        read_txt_build_dic()
        if str(user) in userid_name_dic:
            await message.channel.send(f'Hello {userid_name_dic.get(str(user))} what do you want?')
        else:
            await message.channel.send("""
                                        Hello there! I haven't seen you before
                                        please use '#new' command so that I can remember you!
                                        """)
    await client.process_commands(message)

client.run('ODUyMzQzOTQ4Njc1NTE0NDE4.YMFdKQ.3DjzB3aye4woytq4q4dLsPMgU7w')