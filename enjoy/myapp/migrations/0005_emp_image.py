# Generated by Django 2.2.3 on 2019-07-03 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_emp_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='image',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
