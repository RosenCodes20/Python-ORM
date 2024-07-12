from django.contrib import admin

from main_app.models import MenuReview, Menu, Restaurant


# Register your models here.
@admin.register(MenuReview)
class MenuReviewAdmin(admin.ModelAdmin):
    list_display = ["reviewer_name", "rating"]
    search_fields = ("reviewer_name",)
    list_filter = ("rating",)
    list_per_page = 2


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass