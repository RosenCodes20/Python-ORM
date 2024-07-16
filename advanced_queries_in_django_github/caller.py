import os
import django
from django.db.models import Sum, Q, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct


def product_quantity_ordered():
    products_quantity = OrderProduct.objects.values("product__name").annotate(sum_quantity=Sum("quantity")).order_by("-sum_quantity")
    result = []

    for product in products_quantity:
        result.append(f"Quantity ordered of {product['product__name']}: {product['sum_quantity']}")

    return "\n".join(result)


def ordered_products_per_customer():
    orders = Order.objects.prefetch_related("orderproduct_set__product__category").order_by("id")
    result = []

    for order in orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")
        for ordered_product in order.orderproduct_set.all():
            result.append(f"- Product: {ordered_product.product.name}, Category: {ordered_product.product.category.name}")

    return "\n".join(result)


def filter_products():
    filtered_products = Product.objects.filter(Q(is_available=True) & Q(price__gt=3)).order_by("-price", "name")
    result = []

    for product in filtered_products:
        result.append(f"{product.name}: {product.price}lv.")

    return "\n".join(result)


def give_discount():
    Product.objects.filter(Q(price__gt=3) & Q(is_available=True)).order_by("-price", "name").update(price=F("price") * 0.7)
    available_products = Product.objects.filter(is_available=True).order_by("-price", "name")
    result = []

    for product in available_products:
        result.append(f"{product.name}: {product.price}lv.")

    return "\n".join(result)

