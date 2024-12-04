from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
]
