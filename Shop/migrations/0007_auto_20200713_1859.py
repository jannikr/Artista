# Generated by Django 3.0.7 on 2020-07-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_vote_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote_comment',
            name='up_or_down',
        ),
        migrations.AddField(
            model_name='vote_comment',
            name='up_or_down_or_flag',
            field=models.CharField(choices=[('U', 'up'), ('D', 'down'), ('F', 'flag')], max_length=1, null=True),
        ),
    ]
