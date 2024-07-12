from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator, MaxValueValidator
from django.db import models

from main_app.validators import validate_menu_categories


class ReviewMixin(models.Model):
    review_content = models.TextField()

    rating = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5)
        ]
    )

    class Meta:
        ordering = ["-rating"]
        abstract = True


class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(
                2,
                message="Name must be at least 2 characters long."
            ),
            MaxLengthValidator(
                100,
                message="Name cannot exceed 100 characters.")
        ]
    )

    location = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(
                2,
                message="Location must be at least 2 characters long."
            ),
            MaxLengthValidator(
                200,
                message="Location cannot exceed 200 characters."
            )
        ]
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(
                0,
                message="Rating must be at least 0.00."
            ),
            MaxValueValidator(
                5,
                message="Rating cannot exceed 5.00."
            )
        ]
    )
    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        validators=[
            validate_menu_categories
        ]
    )

    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.description

class RestaurantReview(ReviewMixin):
    reviewer_name = models.CharField(
        max_length=100
    )

    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE
    )

    # review_content = models.TextField()
    #
    # rating = models.PositiveIntegerField(
    #     validators=[
    #         MaxValueValidator(5)
    #     ]
    # )

    class Meta(ReviewMixin.Meta):
        abstract = True
        # ordering = ["-rating"]
        verbose_name = "Restaurant Review"
        verbose_name_plural = "Restaurant Reviews"
        unique_together = ["reviewer_name", "restaurant"]


class RegularRestaurantReview(RestaurantReview):
    pass


class FoodCriticRestaurantReview(RestaurantReview):
    food_critic_cuisine_area = models.CharField(
        max_length=100
    )

    class Meta(RestaurantReview.Meta):
        verbose_name = "Food Critic Review"
        verbose_name_plural = "Food Critic Reviews"


class MenuReview(ReviewMixin):
    reviewer_name = models.CharField(
        max_length=100
    )

    menu = models.ForeignKey(
        to=Menu,
        on_delete=models.CASCADE
    )

    # review_content = models.TextField()
    #
    # rating = models.PositiveIntegerField(
    #     validators=[
    #         MaxValueValidator(5)
    #     ]
    # )

    class Meta(ReviewMixin.Meta):
        # ordering = ["-rating"]
        verbose_name = "Menu Review"
        verbose_name_plural = "Menu Reviews"
        unique_together = ["reviewer_name", "menu"]
        indexes = [models.Index(fields=["menu"], name="main_app_menu_review_menu_id")]

    def __str__(self):
        return self.reviewer_name