from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.best_menu import best_button
import gspread
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=best_button)

@dp.message_handler(text="Balans")
async def bot_start(message: types.Message):
    await message.answer(f"{message.from_user.full_name}\n"
                         f"Fiksal daromad: 500 000 so’m\n"
                         f"Sotuvdan ulush: 79 621 so’m\n"
                         f"Xizmatlar:\n"
                         f"  ⚠️Bajarilyapti: 0 so’m\n"
                         f"  ✅   Bajarildi: 120 000 so’m\n"
                         f"  ⛔   Kechiktirildi: 0 so’m\n"
                         f"Joriy balans: 689 621 so’m\n"
                         f"Umumiy yechib olingan summa: 10 000 so’m, !")




# Connect to Google Sheet using gspread
gc = gspread.service_account(filename='BotSpreadsheets',)
sh = gc.open_by_url(url='https://docs.google.com/spreadsheets/d/1wgBmY43oT3e6uNv4Gw62f23mswQdyucJpZhzNAVx72A/edit#gid=2103330706')
worksheet = sh.sheet1

# Create Aiogram bot
bot = Bot(token='5849420926:AAGrJjMHl3qYJ4acrnumAQHmfjslgWRpcFo')
dp = Dispatcher(bot)


# Define command handler
@dp.message_handler(commands=['data'])
async def send_data(message: types.Message):
    # Read data from Google Sheet
    data = worksheet.get_all_values()

    # Create message to send to user
    response = 'Here is the data from the Google Sheet:\n\n'
    for row in data:
        response += ', '.join(row) + '\n'

    # Send message to user via bot
    await bot.send_message(chat_id=message.chat.id, text=response)


# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


