
from django.urls import path
from blog.views import *
app_name='blog'
urlpatterns = [
    path('',blog_view,name='index'),
    path('<int:pid>',blog_single,name='single'),
    path('category/<str:cat_name>',blog_view,name='category'),
    # path('category/<str:cat_name>',blog_category,name='category'),#نیم اسم یو ار المون هست
    path('author/<str:author_username>',blog_view,name='author'),
    path('search/',blog_search,name='search'),

    path('test',test,name='test'),
    path('test2',test2,name='test2')

    # path('<str:name>/<str:family_name>/<int:age>',test,name='test'),
    # path('post-<int:pid>',test,name='test'),

]