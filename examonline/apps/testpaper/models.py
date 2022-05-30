from django.db import models
from datetime import datetime

from testquestion.models import TestQuestionInfo
from user.models import UserProfile, StudentsInfo, SubjectInfo


# 시험지 정보
class TestPaperInfo(models.Model):
    name = models.CharField(max_length=50, default='', verbose_name='시험지 이름')
    subject = models.ForeignKey(SubjectInfo, on_delete=models.CASCADE, verbose_name='시험지 과목', default='')
    tp_degree = models.CharField(
        choices=(('jd', '쉬움'), ('zd', '중간'), ('kn', '어려움')), max_length=2, verbose_name='시험지 난이도', default='jd'
    )
    total_score = models.IntegerField(default=100, verbose_name='총점')
    passing_score = models.IntegerField(default=60, verbose_name='합격점')
    create_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='교수')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='생성 시간')
    edit_time = models.DateTimeField(auto_now=True, verbose_name='수정 시간')

    class Meta:
        verbose_name = '시험지 정보'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 시험지시험 문제
class TestPaperTestQ(models.Model):
    test_paper = models.ForeignKey(TestPaperInfo, on_delete=models.CASCADE, verbose_name='시험지')
    test_question = models.ForeignKey(TestQuestionInfo, on_delete=models.CASCADE, verbose_name='시험 문제')

    class Meta:
        verbose_name = '시험 문제 정보'
        verbose_name_plural = verbose_name


# 학생 성적 정보
class TestScores(models.Model):
    user = models.ForeignKey(StudentsInfo, on_delete=models.Model, verbose_name='학생 정보')
    test_paper = models.ForeignKey(TestPaperInfo, on_delete=models.CASCADE, verbose_name='시험지 정보')
    test_score = models.IntegerField(default=0, verbose_name='시험 성적')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='생성 시간')

    class Meta:
        verbose_name = '학생 성적 정보'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.student_name
