from django.db import models

# Create your models here.
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
    digital = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url

    @property
    def total_count(self):
        return None