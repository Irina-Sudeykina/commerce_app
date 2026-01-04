from config.settings import CACHE_ENABLED
from django.core.cache import cache
from .models import Product, Category


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


class CategoryService:

    @staticmethod
    def category_products_list(category_id):
        category = Category.objects.get(id=category_id)
        products_list = Product.objects.filter(category=category)

        if not products_list.exists():
            return None

        return products_list
