import asyncio
import sqlite3
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

# Tokeningizni shu yerga yozing
TOKEN = "BU_YERGA_TOKENINGIZNI_YASHTIRING" 
ADMIN_ID = 7321532345

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.executescript(""" 
CREATE TABLE IF NOT EXISTS users ( user_id INTEGER PRIMARY KEY, balance INTEGER DEFAULT 0, frozen INTEGER DEFAULT 0 ); 
CREATE TABLE IF NOT EXISTS campaigns ( id INTEGER PRIMARY KEY AUTOINCREMENT, file_id TEXT, view_count INTEGER DEFAULT 0, active INTEGER DEFAULT 1 ); 
CREATE TABLE IF NOT EXISTS withdrawals ( id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, amount INTEGER NOT NULL, card_number TEXT ); 
""")
conn.commit()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
