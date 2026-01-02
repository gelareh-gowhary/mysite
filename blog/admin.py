from django.contrib import admin
from blog.models import Post
# Register your models here.
# @admin.register(Post) #از این خط میتوانیم به جای خط  ۸ استفاده کنیم 
class PostAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','counted_views','status','published_date','created_date')
    list_filter=('status',)
    # ordering=['-created_date']
    # میخوای داخل کدوم فیلدها رات جست و جو کنه از خط زیر
    search_fields=('title','content')

admin.site.register(Post,PostAdmin) #یا از این خط یا خط ۴