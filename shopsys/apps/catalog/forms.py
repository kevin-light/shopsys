from django import forms
from .models import Product

#为admin模型字段添加自定义验证
class ProductAdminForm(forms.ModelForm):
    #定义元类
    class Meta:
        model = Product
        exclude = []    #必须添加exclude可以为空[]，不然报错

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('价格必须大于0')
        return self.cleaned_data['price']