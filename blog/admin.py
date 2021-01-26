from django.contrib import admin
from .models import Post

admin.site.site_header = 'LearnShare'
admin.site.site_title = 'LearnShare Admin Area'
admin.site.index_title = 'Welcome to admin area'

# Add Model
admin.site.register(Post)
