""" package_init"""
from fastapi import APIRouter # pylint: disable=import-error
from routers.debug import aaa

router = APIRouter()

router.include_router(aaa.router)
