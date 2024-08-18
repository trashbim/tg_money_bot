from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from database import db
from keyboards import create_category_keyboard
from states import TransactionStates

async def add_transaction(message: Message, state: FSMContext):
    await message.answer('Выберите категорию:', reply_markup=create_category_keyboard())
    await state.set_state(TransactionStates.waiting_for_category)

async def process_category(message: Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.answer('Введите сумму:')
    await state.set_state(TransactionStates.waiting_for_amount)

async def process_amount(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)
    await message.answer('Введите описание (необязательно):')
    await state.set_state(TransactionStates.waiting_for_description)

async def add_transaction_to_db(message: Message, state: FSMContext):
    data = await state.get_data()
    category = data['category']
    amount = float(data['amount'])
    description = message.text

    db.add_transaction(category, amount, description)
    await message.answer('Транзакция добавлена!')
    await state.clear()

async def get_balance(message: Message):
    balance = db.get_current_balance()
    await message.answer(f"Ваш текущий баланс: {balance}")

# Register all handlers
def register_handlers(dp: Dispatcher):
    dp.message.register(add_transaction, Command(commands=["add"]))
    dp.message.register(process_category, StateFilter(TransactionStates.waiting_for_category))
    dp.message.register(process_amount, StateFilter(TransactionStates.waiting_for_amount))
    dp.message.register(add_transaction_to_db, StateFilter(TransactionStates.waiting_for_description))
    dp.message.register(get_balance, Command(commands=["balance"]))
