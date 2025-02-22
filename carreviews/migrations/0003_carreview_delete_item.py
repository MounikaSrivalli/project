# Generated by Django 5.1.1 on 2024-09-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreviews', '0002_rename_name_item_carname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carname', models.CharField(max_length=100)),
                ('reviewer_name', models.CharField(max_length=100)),
                ('ratings', models.FloatField()),
                ('review_description', models.TextField()),
            ],
            options={
                'db_table': 'cardekho',
            },
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
