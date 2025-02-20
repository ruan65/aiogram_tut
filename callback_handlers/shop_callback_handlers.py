from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.utils import markdown
from keyboards.shop_keyboards import (
    ProductActions,
    ProductCallbackData,
    ShopActions,
    ShopCallbackData,
    build_product_details_keyboard,
    build_product_keyboard,
    build_product_update_keyboard,
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


@router.callback_query(
    ProductCallbackData.filter(F.action == ProductActions.details),
)
async def handle_product_details(
    callback: CallbackQuery,
    callback_data: ProductCallbackData,
):
    await callback.answer()
    message_text = markdown.text(
        markdown.text(
            markdown.hbold("Title:"),
            callback_data.title,
        ),
        markdown.text(
            markdown.hbold("Price:"),
            callback_data.price,
        ),
        sep="\n",
    )
    await callback.message.edit_text(
        text=message_text,
        reply_markup=build_product_details_keyboard(callback_data),
        parse_mode="HTML",
    )


@router.callback_query(
    ProductCallbackData.filter(F.action == ProductActions.update),
)
async def handle_update_product(
    callback: CallbackQuery,
    callback_data: ProductCallbackData,
):
    await callback.answer()
    await callback.message.edit_reply_markup(
        reply_markup=build_product_update_keyboard(callback_data),
    )


@router.callback_query(
    ProductCallbackData.filter(F.action == ProductActions.delete),
)
async def handle_delete_product(
    callback: CallbackQuery,
    callback_data: ProductCallbackData,
):
    await callback.answer("delete is in progress")
