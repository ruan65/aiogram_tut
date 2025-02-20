from ast import In
from enum import IntEnum, auto
from logging import root
from operator import add
from sys import prefix
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class ShopActions(IntEnum):
    products = auto()
    address = auto()
    root = auto()


class ShopCallbackData(CallbackData, prefix="shop"):
    action: ShopActions


class ProductActions(IntEnum):
    details = auto()
    update = auto()
    delete = auto()


class ProductCallbackData(CallbackData, prefix="product"):
    action: ProductActions
    id: int
    title: str
    price: int


def build_shop_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Show products",
        callback_data=ShopCallbackData(action=ShopActions.products).pack(),
    )
    builder.button(
        text="My address",
        callback_data=ShopCallbackData(action=ShopActions.address).pack(),
    )

    builder.adjust(1)
    return builder.as_markup()


def build_product_keyboard():
    builder = InlineKeyboardBuilder()
    for index, (name, price) in enumerate(
        [
            ("Macbook Air", 1099),
            ("Macbook Pro", 2099),
            ('Macbook Pro 16"', 2499),
            ('Macbook Pro 16" M4', 2999),
        ]
    ):
        builder.button(
            text=f"{name} - {price}$",
            callback_data=ProductCallbackData(
                action=ProductActions.details,
                id=index,
                title=name,
                price=price,
            ).pack(),
        )
    builder.button(
        text="Back to root",
        callback_data=ShopCallbackData(action=ShopActions.root).pack(),
    )
    builder.adjust(1)
    return builder.as_markup()


def build_product_details_keyboard(
    product_callback_data: ProductCallbackData,
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Back to products",
        callback_data=ShopCallbackData(action=ShopActions.products).pack(),
    )
    builder.button(
        text="Update product",
        callback_data=ProductCallbackData(
            action=ProductActions.update,
            id=product_callback_data.id,
            title=product_callback_data.title,
            price=product_callback_data.price,
        ).pack(),
    )
    builder.button(
        text="Delete product",
        callback_data=ProductCallbackData(
            action=ProductActions.delete,
            **product_callback_data.model_dump(include={"id", "title", "price"}),
        ),
    )
    builder.adjust(1, 2)
    return builder.as_markup()
