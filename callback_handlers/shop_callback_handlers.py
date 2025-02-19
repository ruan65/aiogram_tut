from aiogram import F, Router
from aiogram.types import CallbackQuery
from keyboards.shop_keyboards import (
    ShopActions,
    ShopCallbackData,
    build_product_keyboard,
    build_shop_keyboard,
)

router = Router(name=__name__)


@router.callback_query(
    ShopCallbackData.filter(F.action == ShopActions.products),
)
async def send_products_list(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        text="Available products",
        reply_markup=build_product_keyboard(),
    )


@router.callback_query(
    ShopCallbackData.filter(F.action == ShopActions.address),
)
async def handle_address(callback: CallbackQuery):
    await callback.answer(
        text="Your address",
        cache_time=30,
    )


@router.callback_query(
    ShopCallbackData.filter(F.action == ShopActions.root),
)
async def handle_root(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        text="Choose shopping action",
        reply_markup=build_shop_keyboard(),
    )
