from django.core.urlresolvers import reverse
from  django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="名称")
    slug = models.SlugField(verbose_name="Slug", max_length=50, unique=True)
    description = models.TextField(verbose_name="描述")
    is_active = models.BooleanField(verbose_name="是否激活", default=True)
    meta_keywords = models.CharField(verbose_name="Meta关键词", max_length=255)
    meta_description = models.CharField(verbose_name="Meta描述", max_length=255)
    created_at = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日期", auto_now=True)

    class Meta:
        db_table = "categories"
        ordering = ["-created_at"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog_category", args=(self.slug,))


class Product(models.Model):
    name = models.CharField(verbose_name="名称", max_length=255, unique=True)
    slug = models.SlugField(verbose_name="Slug", max_length=255, unique=True)
    brand = models.CharField(verbose_name="品牌", max_length=50)
    sku = models.CharField(verbose_name="计量单位", max_length=50)
    price = models.DecimalField(verbose_name="价格", max_digits=9, decimal_places=2)
    old_price = models.DecimalField(verbose_name="旧价格", max_digits=9,decimal_places=2,
                                    blank=True, default=0.00)
    image = models.ImageField(verbose_name="图片", max_length=50)
    is_active = models.BooleanField(verbose_name="设为激活", default=True)
    is_bestseller = models.BooleanField(verbose_name="标为畅销", default=False)
    is_featured = models.BooleanField(verbose_name="标为推荐", default=False)
    quantity = models.IntegerField(verbose_name="数量")
    description = models.TextField(verbose_name="描述")
    meta_keywords = models.CharField(verbose_name="Meta关键词", max_length=255)
    meta_description = models.CharField(verbose_name="Meta描述", max_length=255)
    created_at = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日期", auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = "products"
        ordering = ["-created_at"]
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog_product", args=(self.slug,))

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
