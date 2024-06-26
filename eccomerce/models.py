from django.contrib.auth.models import User
from django.db import models


class TimeStampedModel(models.Model):
    """
    Bazaviy model bo'lishi uchun TimeStampedModel yaratildi.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Abstract=True yaratilishini maqsadi ma'lumotlar ba'zasida model yaratilmasligini taminlaydi.
        """
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product_img/', blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    info = models.TextField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    # @property
    # def image_url(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #
    #     return url


# class Customer(TimeStampedModel):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=120, null=True)
#     email = models.CharField(max_length=120, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Order(TimeStampedModel):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     complete = models.BooleanField(default=False, null=True, blank=True)
#     transaction_id = models.CharField(max_length=120, null=True, blank=True)
#
#     def __str__(self):
#         return self.customer.name
#
#     @property
#     def get_cart_total(self):
#         order_items = self.orderitem_set.all()
#         total = sum([item.get_items_total_price for item in order_items])
#         return total
#
#     @property
#     def get_cart_items(self):
#         order_items = self.orderitem_set.all()
#         total = sum([item.quantity for item in order_items])
#         return total
#
#
# # [1, 2, 3 ,4, 5]
# # [i for i in range(1, 6)]
#
# class OrderItem(TimeStampedModel):
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
#     quantity = models.IntegerField(default=0, blank=True, null=True)
#
#     def __str__(self):
#         return self.product.name
#
#     @property
#     def get_items_total_price(self):
#         order_total = self.quantity * self.product.price
#         return order_total
#
#
# class ShippingAddress(TimeStampedModel):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     address = models.CharField(max_length=200, null=False)
#     city = models.CharField(max_length=200, null=False)
#     state = models.CharField(max_length=200, null=False)
#     zipcode = models.CharField(max_length=200, null=False)
#
#     def __str__(self):
#         return self.address