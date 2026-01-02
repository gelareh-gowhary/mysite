from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    # خط زیر میگیم هر چی اپلود کردیم کجا بره ذخیره شه و اگه عکسی ندادیم از یه عکس پیش فرض استفاده کنه 
    image =models.ImageField(upload_to='blog/',default='blog/default.jpg')
    # همراه پاک شدن یوزر پستهای مربطو به اون یوزر هم پاک بشه 
    # author =models.ForeignKey(User,on_delete=models.CASCADE)
    author =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags = 
    # category = 
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta():
        ordering=['created_date']
        # verbose_name='پست'
        # verbose_name_plural='پستها'
    def __str__(self):
        return f"{self.title}-{self.id}"
        # خط کد بالا و پایین دوتاش یکی هستن 
        # return '{}-{}'.format(self.title,self.id)
       