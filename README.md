# second_task
 Range Filter Build a django app which can segment the products w.r.t their price and size, No. Of segment must be dynamic using range filter.(create atleast 30 products in db).


1)django-admin startproject product_segmenter
cd product_segmenter
python manage.py startapp products


Run migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate

run seed comman
python manage.py seed_products
