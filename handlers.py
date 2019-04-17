"""
Handler functions to be dispatched.
"""

from validators import is_registered, is_message_for_bot
from database import create_user
import messages


def start(bot, update):
	m = update.message
	if not is_message_for_bot(m):
		return
	m.reply_text(messages.START_MESSAGE)
	if not is_registered(m.from_user):
		create_user({'telegram_id': m.from_user.id, 'first_name': m.from_user.first_name})


def stop(bot, update):
	# Unsubscribe user from bot
	update.message.reply_text(messages.STOP_MESSAGE)


def normal_message(bot, update):
	m = update.message
	chat = m.chat
	chat_id = chat.id
	text = m.text
	reply = m.reply_text
	# Handle non-command text messages
