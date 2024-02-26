from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import DB_NAME
from utils.database import Database

db = Database(DB_NAME)

def make_category_list() -> InlineKeyboardMarkup:
    categories = db.get_categories()
    rows = []
    for category in categories:
        rows.append([
            InlineKeyboardButton(
                text=str(category[1]),
                callback_data=str(category[1])
            )
        ])
    kb_categories = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb_categories

def make_product_list() -> InlineKeyboardMarkup:
    products = db.get_product()
    rows = []
    for product in products:
        rows.append([
            InlineKeyboardButton(
                text=str(product[1]),
                callback_data=str(product[1])
            )
        ])
    kb_products = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb_products

def make_ad_list() -> InlineKeyboardMarkup:
    ads = db.get_my_ads()
    rows = []
    for ad in ads:
        rows.append([
            InlineKeyboardButton(
                text=str(ad[1]),
                callback_data=str(ad[1])
            )
        ])
    kb_ads = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb_ads