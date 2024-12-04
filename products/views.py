from django.shortcuts import render
from products.models import Product

def product_list(request):
    # Get filter parameters from the request
    min_price = float(request.GET.get('min_price', 0))
    max_price = float(request.GET.get('max_price', 100))
    size = request.GET.get('size', None)

    # Filter products dynamically
    products = Product.objects.filter(price__gte=min_price, price__lte=max_price)
    if size:
        products = products.filter(size=size)

    # Calculate price ranges dynamically
    price_step = (max_price - min_price) / 5
    price_segments = [
        (min_price + i * price_step, min_price + (i + 1) * price_step)
        for i in range(5)
    ]

    context = {
        'products': products,
        'price_segments': price_segments,
        'selected_size': size,
        'sizes': ['Small', 'Medium', 'Large'],
    }
    return render(request, 'products/product_list.html', context)
