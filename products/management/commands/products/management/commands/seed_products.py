from django.core.management.base import BaseCommand
from products.models import Product
import random

class Command(BaseCommand):
    help = 'Seed the database with products'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        sizes = ['Small', 'Medium', 'Large']
        for i in range(30):
            Product.objects.create(
                name=f'Product {i+1}',
                price=random.uniform(10, 100),
                size=random.choice(sizes)
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded products!'))
