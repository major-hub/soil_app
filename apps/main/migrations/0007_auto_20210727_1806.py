# Generated by Django 3.2.5 on 2021-07-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210727_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='function',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='function',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='function',
            name='text_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='function',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='function',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='function',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
