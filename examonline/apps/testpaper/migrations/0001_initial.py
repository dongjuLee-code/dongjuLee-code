# Generated by Django 2.1.4 on 2019-02-22 14:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestPaperInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='试卷名称')),
                ('tp_degree', models.CharField(choices=[('jd', '简单'), ('zd', '中等'), ('kn', '困难')], default='jd', max_length=2, verbose_name='试卷难度')),
                ('total_score', models.IntegerField(default=100, verbose_name='总分')),
                ('passing_score', models.IntegerField(default=60, verbose_name='及格分')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('edit_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '试卷信息',
                'verbose_name_plural': '试卷信息',
            },
        ),
        migrations.CreateModel(
            name='TestPaperTestQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '试卷试题信息',
                'verbose_name_plural': '试卷试题信息',
            },
        ),
        migrations.CreateModel(
            name='TestScores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_score', models.IntegerField(default=0, verbose_name='考试成绩')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('test_paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testpaper.TestPaperInfo', verbose_name='试卷信息')),
            ],
            options={
                'verbose_name': '学生成绩信息',
                'verbose_name_plural': '学生成绩信息',
            },
        ),
    ]
