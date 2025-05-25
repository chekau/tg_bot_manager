import asyncio
from aiogram import Bot,Dispatcher,types,Router
from aiogram.filters import Command
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

balance = 0
all_income = 0
all_expence = 0

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.reply(f"""Привет!
я - бот который будет управлять твоим личным бюджетом!""")


@dp.message(Command("income"))
async def income_money(message: types.Message):
    global balance,all_income
    words = message.text.split()
    balance += int(words[1])
    all_income += int(words[1])
    await message.answer(f"""Отлично!,
доход {words[1]} руб добавлен с пометкой {words[2:]},
текущий баланс: {balance}""")
    

@dp.message(Command("expense"))
async def expense_money(message: types.Message):
    global balance,all_expence
    words = message.text.split()
    balance -= int(words[1])
    all_expence += int(words[1])
    await message.answer(f"""Отлично!,
расход {words[1]} руб в категории {words[2:]},
текущий баланс: {balance}""")

@dp.message(Command("report"))
async def report_money(message: types.Message):
    global all_income,all_expence,balance
    words = message.text.split()
    await message.answer(f"""Отчёт за неделю:
Доходы: {all_income} руб
Расходы: {all_expence} руб
Баланс: {balance} руб
                        """)



if __name__ == "__main__":
    asyncio.run(main())
