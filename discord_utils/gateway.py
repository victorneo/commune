from datetime import datetime
import discord as d
import requests

INTENTS = d.Intents(messages=True, guilds=True, voice_states=True)
DISCORD_GATEWAY_BOT_URL = 'https://discord.com/api/v10/gateway/bot'


def get_gateway_url(bot_token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bot {}'.format(bot_token)}

    resp = requests.get(DISCORD_GATEWAY_BOT_URL, headers=headers)
    return resp.json()['url']


def get_streaming_client():
    client = d.Client(intents=INTENTS)
    return client

