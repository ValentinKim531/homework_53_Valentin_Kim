# Generated by Django 4.1.6 on 2023-02-15 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='to_do',
            name='title',
            field=models.CharField(help_text='Заголовок задачи', max_length=100, null=True, verbose_name='Заголовок'),
        ),
    ]
