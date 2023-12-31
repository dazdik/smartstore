from django.contrib import admin

from .models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'author', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity',), 'stripe_product_price_id',
              'category', 'image', 'author', 'release_date', 'amount_pages')
    search_fields = ('name', 'author')


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
