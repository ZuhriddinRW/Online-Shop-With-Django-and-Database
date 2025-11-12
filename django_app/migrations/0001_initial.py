import django.db.models.deletion
from django.db import migrations, models


class Migration ( migrations.Migration ) :
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel (
            name='Category',
            fields=[
                ('category_id', models.AutoField ( primary_key=True, serialize=False )),
                ('category_name', models.CharField ( max_length=100 )),
                ('description', models.TextField ( default='Default Description' )),
                ('image', models.ImageField ( default='images/category.png', upload_to='photo/%Y/%m/%d' )),
            ],
            options={
                'verbose_name' : 'Category',
                'verbose_name_plural' : 'Categories',
            },
        ),
        migrations.CreateModel (
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField ( primary_key=True, serialize=False )),
                ('company_name', models.CharField ( max_length=50 )),
                ('contact_name', models.CharField ( max_length=50 )),
                ('contact_title', models.CharField ( max_length=50 )),
                ('address', models.CharField ( max_length=50 )),
                ('city', models.CharField ( max_length=50 )),
                ('region', models.CharField ( blank=True, max_length=50, null=True )),
                ('image', models.ImageField ( blank=True, default='images/supplier.png', null=True,
                                              upload_to='photo/%Y/%m/%d' )),
            ],
            options={
                'verbose_name' : 'Supplier',
                'verbose_name_plural' : 'Suppliers',
            },
        ),
        migrations.CreateModel (
            name='News',
            fields=[
                ('id', models.BigAutoField ( auto_created=True, primary_key=True, serialize=False, verbose_name='ID' )),
                ('title', models.CharField ( max_length=100, verbose_name='Title' )),
                ('content', models.TextField ( verbose_name='Content' )),
                ('created_at', models.DateTimeField ( auto_now_add=True, verbose_name='Add_date' )),
                ('updated_at', models.DateTimeField ( auto_now=True )),
                ('photo', models.ImageField ( default='images/news.jpg', upload_to='photo/%Y/%m/%d' )),
                ('bool', models.BooleanField ( default=False, verbose_name='Bool' )),
                ('category', models.ForeignKey ( default=1, on_delete=django.db.models.deletion.CASCADE,
                                                 to='django_app.category' )),
            ],
            options={
                'verbose_name' : 'News',
                'verbose_name_plural' : 'News',
                'ordering' : ['-created_at'],
            },
        ),
        migrations.CreateModel (
            name='Product',
            fields=[
                ('product_id', models.AutoField ( primary_key=True, serialize=False )),
                ('product_name', models.CharField ( max_length=50 )),
                ('unit_price', models.IntegerField ()),
                ('description', models.TextField ( blank=True, null=True )),
                ('image',
                 models.ImageField ( blank=True, default='images/product.png', null=True, upload_to='photo/%Y/%m/%d' )),
                ('category',
                 models.ForeignKey ( on_delete=django.db.models.deletion.CASCADE, to='django_app.category' )),
            ],
            options={
                'verbose_name' : 'Product',
                'verbose_name_plural' : 'Products',
                'ordering' : ['-product_name'],
            },
        ),
    ]