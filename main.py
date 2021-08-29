from discord.ext import commands
import requests
import logging
import random
import json
import ticker_assigner

logging.basicConfig(level=logging.INFO)

token = 'NjA5MTU1MDkxNTYzNTQ0NTc4.XUyl4w.lrMm_RL-Uza3edQZw7faxXbxK7s'
prefix = '!'


client = commands.Bot(command_prefix=prefix)


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return quote


@client.event
async def on_voice_state_update(member, before, after):
    channel = client.get_channel(809632052051050548)
    a = str(member.display_name)
    b = str(ticker_assigner.get_random_ticker())
    c = str(ticker_assigner.get_ticker_price())
    if before.channel is None and after.channel is not None:
        await channel.send(
            f'hi {a} did you know that {b} is ${c}'
        )


@client.event
async def on_ready():
    print('Bot online as {0.user}'.format(client))


@client.command()  # test function to check whether the commands are going through
async def ping(ctx):
    await ctx.send('Pong!')


@client.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.message.channel.send(quote)


@client.command(aliases=['8 ball', '8ball'])
async def _8ball(ctx, *, question):
    responses = [
        'It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes - definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs point to yes',
        'Reply hazy, try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        "Don't count on it",
        'My reply is no',
        'My sources say no',
        'Outlook not good',
        'Very doubtful'
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def hello(ctx):
    response = [
        'Hey!',
        'Hi!',
        "How's it going?",
        "What's up?",
        'Hello!',
        'Howdy',
        'Hi there!'
    ]
    await ctx.send(random.choice(response))


@client.command()
async def bye(ctx):
    response = [
        "I'm still here",
        'I was here before you, I will be here after you',
        'I am unstoppable',
        "You can't beat me!",
        'I am eternal'
    ]
    await ctx.send(random.choice(response))


@client.event  # so the bot doesn't talk to itself endlessly
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)  # this is required to make the other commands function


client.run(token)

#  realistic binaural audio knocking at random times
#  microsoft sam - with names - greeting when join and leaves - and gives you a random ticker price
#  set up a stack overflow API to answer FAQ before teacher is pinged
#  use stripe to handle transactions