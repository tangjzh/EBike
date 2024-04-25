from django.db import models

# Create your models here.
class Bike(models.Model):
    brand = models.CharField(blank=True, max_length=100, verbose_name="品牌")
    model = models.CharField(blank=True, max_length=100, verbose_name="型号")
    price = models.DecimalField(blank=True, max_digits=10, decimal_places=2, verbose_name="价格")
    rating = models.FloatField(blank=True, verbose_name="评价")
    release_date = models.DateField(blank=True, verbose_name="上市日期")
    description = models.TextField(blank=True, verbose_name="描述")

    def __str__(self):
        return f"{self.brand} - {self.price}"
    
class BikeImage(models.Model):
    bike = models.ForeignKey(Bike, related_name='images', on_delete=models.CASCADE, verbose_name="电动车")
    image = models.ImageField(upload_to='bike_images/', verbose_name="图片")

    def __str__(self):
        return f"{self.bike.brand} - Image"

class Channel(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name="channels")
    name = models.CharField(max_length=100, verbose_name="渠道名称")
    url = models.URLField(verbose_name="购买链接")
    service_info = models.TextField(verbose_name="服务信息")

    def __str__(self):
        return self.name
