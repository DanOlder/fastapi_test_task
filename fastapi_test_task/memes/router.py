"""Модуль роутера алгоритмов."""
from fastapi import APIRouter, Request
from fastapi.routing import APIRoute

from fastapi_test_task.memes.crud import memes_crud_router

memes_router = APIRouter(
    prefix='/memes',
)

memes_router.include_router(memes_crud_router)


@memes_router.get('/', name='Cписок сервисов', tags=['meta'])
async def algorithms_list(request: Request):
    """Список алгоритмов."""
    services_list = []
    for route in memes_router.routes:
        route_url = request.url_for(route.name)
        if isinstance(route, APIRoute) and 'meta' not in route.tags:
            services_list.append({
                'name': route.name,
                'url': str(route_url),
                'description': route.description,
            })

    return services_list
