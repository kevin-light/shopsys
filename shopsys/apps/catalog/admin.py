from django.contrib import admin        #admin密码admin123，
from .models import Category,Product
from .forms import ProductAdminForm

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #为admin模型字段添加自定义验证
    form = ProductAdminForm
    # 设置admin界面如何显示产品列表
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
    #设置点击name链接
    list_display_links = ('name',)
    #admin界面一叶显示50条
    list_per_page = 50
    #排序方式-倒序
    ordering = ['-created_at']
    #搜索字段
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    #不用手动填写包含的字段，和field相反
    exclude = ('created_at', 'updated_at',)
    #自动填充
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('name',)}