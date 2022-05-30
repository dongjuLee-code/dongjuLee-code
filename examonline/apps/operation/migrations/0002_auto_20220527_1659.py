# Generated by Django 2.1.4 on 2022-05-27 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='examcomments',
            options={'verbose_name': '시험 평가', 'verbose_name_plural': '시험 평가'},
        ),
        migrations.AlterModelOptions(
            name='userfavorite',
            options={'verbose_name': '사용자 선호도', 'verbose_name_plural': '사용자 선호도'},
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_id',
            field=models.IntegerField(default=0, verbose_name='데이터id'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='message',
            field=models.CharField(max_length=500, verbose_name='메시지 내용'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='user',
            field=models.IntegerField(default=0, verbose_name='사용자 접수'),
        ),
    ]
