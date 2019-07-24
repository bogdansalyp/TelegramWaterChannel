import telegram
from key import token

bot = telegram.Bot(token=token)
msg = "папей воды"
status = bot.send_message(chat_id="@WaterReminder", text=msg, parse_mode=telegram.ParseMode.HTML)

print(status)
