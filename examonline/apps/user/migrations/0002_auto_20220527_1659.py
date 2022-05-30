# Generated by Django 2.1.4 on 2022-05-27 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailverifyrecord',
            options={'verbose_name': '이메일인증 번호', 'verbose_name_plural': '이메일인증 번호'},
        ),
        migrations.AlterModelOptions(
            name='teacherinfo',
            options={'verbose_name': '선생님 정보', 'verbose_name_plural': '선생님 정보'},
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='code',
            field=models.CharField(max_length=100, verbose_name='인증 번호'),
        ),
        migrations.AlterField(
            model_name='studentsinfo',
            name='student_class',
            field=models.CharField(default='', max_length=10, verbose_name='학생 반'),
        ),
        migrations.AlterField(
            model_name='studentsinfo',
            name='student_school',
            field=models.CharField(default='', max_length=100, verbose_name='학생 학교'),
        ),
        migrations.AlterField(
            model_name='subjectinfo',
            name='subject_name',
            field=models.CharField(default='', max_length=20, verbose_name='과목명'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='work_years',
            field=models.IntegerField(default=0, verbose_name='근무연도'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=11, null=True, verbose_name='전화번호'),
        ),
    ]