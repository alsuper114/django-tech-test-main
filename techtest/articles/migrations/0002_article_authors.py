# Generated by Django 3.2.7 on 2023-10-18 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('articles', '0001_schema__initial_model_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='authors', to='authors.Author'),
        ),
    ]
