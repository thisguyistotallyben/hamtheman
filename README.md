# HamTheMan
HamTheMan (htm) is a Discord bot for various ham radio related things, including callsign lookups (globally with HamQTH), solar conditions, time, and a morse code translator.

# Getting started
Make sure you are running Python 3.6 or higher.

### Discord
You need discord.py: `pip3 install discord.py` or `pip3 install -U discord.py`

### API Keys
You then need an API key for your bot (https://discordapp.com/developers/applications/) and an account with HamQTH (https://hamqth.com).

### Setup
Setup is pretty simple. You need to copy/rename the file `config_default.json` to `config.json` and fill in the information inside.

See the API keys section above for the fields `discord key` and `hamqth`.

The accent color is the hex code of the color that highlights embeds.

The `owner id` field is for you. Find your Discord user id (a long number, not your username#0000) and put it here.
