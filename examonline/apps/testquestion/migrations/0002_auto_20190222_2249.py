# Generated by Django 2.1.4 on 2019-02-22 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('testquestion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='testquestioninfo',
            name='creat_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='교수'),
        ),
        migrations.AddField(
            model_name='testquestioninfo',
            name='subject',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.SubjectInfo', verbose_name='소속 과목'),
        ),
        migrations.AddField(
            model_name='optioninfo',
            name='test_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testquestion.TestQuestionInfo', verbose_name='시험 문제 정보'),
        ),
    ]
