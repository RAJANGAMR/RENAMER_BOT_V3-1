from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	await message.reply_text("Bot :- @RenameProRobot\nTamil Support :- @Tamil_Support\nநன்பர்கள் குழு :- @Tamil_Astrology\nபஞ்சாங்கம் :- @Tamil_Panchangam\nAdmin Contact :- @tamil_message_bot")
