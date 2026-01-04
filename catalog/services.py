from config.settings import CACHE_ENABLED
from django.core.cache import cache
from .models import Product


def get_products_from_cache():
    """
        Получет данные по собакам из кеша, 
        если кеш пуст, то получает данные из БД
    """
    if not CACHE_ENABLED:
        return Product.objects.all()
    products = cache.get("product_list")
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set("product_list", products, 60 * 2)
    return products
