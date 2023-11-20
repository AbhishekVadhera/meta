# Generated by Django 4.2.5 on 2023-11-14 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='account.categories'),
        ),
    ]
