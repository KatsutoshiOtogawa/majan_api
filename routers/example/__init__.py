""" package_init"""
from fastapi import APIRouter # pylint: disable=import-error
from routers.example import et

router = APIRouter()

router.include_router(et.router)
