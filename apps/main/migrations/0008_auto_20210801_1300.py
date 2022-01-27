# Generated by Django 3.2.5 on 2021-08-01 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210727_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Static',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='gallery',
            name='video',
            field=models.URLField(null=True),
        ),
    ]
