"""
Settings and configuration for your bot.
"""

# Bot's API Token granted by the @BotFather
api_token = "000000000:aaaaaaaaaaaaaaaa-aaaaaaaaaaaaaaaaaa"

# This field will be auto-populated
username = None

# A list of user IDs who can manage the bot
admins = []

user_schema = {
	'telegram_id': {
		'type': 'INTEGER',
		'options': 'PRIMARY KEY'
	}
}
