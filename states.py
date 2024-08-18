from aiogram.fsm.state import StatesGroup, State

class TransactionStates(StatesGroup):
    waiting_for_category = State()
    waiting_for_amount = State()
    waiting_for_description = State()
