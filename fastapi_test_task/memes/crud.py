"""Обработка записей с мемами."""
from fastapi import APIRouter

memes_crud_router = APIRouter()


@memes_crud_router.get(path='/memes')
def get_memes_list():
    """Получить список всех мемов."""
    ...


@memes_crud_router.get(path='/meme/{meme_id}')
def get_meme_by_id(meme_id: int):
    """Получить конкретный мем по его ID."""
    ...


@memes_crud_router.post(path='/memes')
def get_meme_by_id(meme_data):
    """Добавить новый мем."""
    ...


@memes_crud_router.put(path='/memes/{meme_id}')
def get_meme_by_id(meme_id: int):
    """Обновить существующий мем."""
    ...


@memes_crud_router.delete(path='/memes/{meme_id}')
def get_meme_by_id(meme_id: int):
    """Удалить мем."""
    ...
