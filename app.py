import logging
from aoigram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot=Bot(token="", parse_mode='html'))
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message)
  await message.answer(f"Assalomu Alaykum <b>@{message.from_user.username}!</b>")
if __name__ == "__main__":
  executor.start_polling(dp, skip_updates=True)
