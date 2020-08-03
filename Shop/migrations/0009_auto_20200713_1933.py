# Generated by Django 3.0.7 on 2020-07-13 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_auto_20200713_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='vote',
        ),
        migrations.AddField(
            model_name='vote_comment',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.Comment'),
        ),
    ]