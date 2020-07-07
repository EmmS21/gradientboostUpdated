from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Quiz(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Student(models.Model):
    day_choices = (
        ('monday','Monday'),
        ('tuesday','Tuesday'),
        ('wednesday','Wednesday'),
        ('thursday','Thursday'),
        ('friday','Friday'),
        ('saturday','Saturday'),
    )

    time_choices = (
        ('morning','Morning'),
        ('afternoon','Afternoon'),
        ('evening','Evening'),
    )
    employed_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    installment_choices = (
        ('upfront', 'Upfront'),
        ('installments', 'Installments'),
    )
    country_choices = (
        ('kenya', 'Kenya'),
        ('nigeria', 'Nigeria'),
        ('south africa', 'South Africa'),
        ('zimbabwe', 'Zimbabwe'),
        ('other', 'Other African Country'),
    )
    # installnum_choices = (
    #     ('2', '2 months'),
    #     ('3', '3 months'),
    #     ('4', '4 months'),
    #     ('5', '5 months'),
    #     ('6', '6 months'),
    #     ('7', '7 months'),
    #     ('8', '8 months'),
    #     ('9', '9 months'),
    #     ('10', '10 months'),
    # )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)

    #more about you fields
    city = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=500, null=True, blank=True)
    current_occupation = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=300, null=True, blank=True)
    # github = models.URLField(max_length=300,null=True,blank=True)
    employed = models.CharField(max_length=100, choices=employed_choices, default='yes')
    installments = models.CharField(max_length=100, choices=installment_choices, default='no')
    # installnum =  models.CharField(max_length=100, choices=installnum_choices, default='2')

    #contact details
    phone_no = models.CharField(max_length=100, null=True, blank=True)
    contact_day = models.CharField(max_length=100, choices=day_choices, default='monday')
    contact_time = models.CharField(max_length=100, choices=time_choices, default='morning')



    def __str__(self):
        return "Profile of user{}".format(self.user)




class Mentor(models.Model):

    day_choices = (
        ('monday','Monday'),
        ('tuesday','Tuesday'),
        ('wednesday','Wednesday'),
        ('thursday','Thursday'),
        ('friday','Friday'),
        ('saturday','Saturday'),
    )

    time_choices = (
        ('morning','Morning'),
        ('afternoon','Afternoon'),
        ('evening','Evening'),
    )


    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    
    #more about you fields
    city = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=500, null=True, blank=True)
    current_occupation = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.URLField(max_length=300,null=True,blank=True)
    github = models.URLField(max_length=300,null=True,blank=True)

    #contact details
    phone_no = models.CharField(max_length=100, null=True, blank=True)
    contact_day = models.CharField(max_length=100, choices=day_choices, default='monday')
    contact_time = models.CharField(max_length=100, choices=time_choices, default='morning')


    photo = models.ImageField(null=True, blank=True, upload_to='media', default='default.jpg')
    address = models.CharField(max_length=500, null=True, blank=True)
    billing_name = models.CharField(max_length=200, null=True, blank=True)
    account_num = models.IntegerField(default=1234, null=True, blank=True)
    bank_name = models.CharField(max_length=50, null=True, blank=True)
    branch_code = models.IntegerField(default=1234, null=True, blank=True)

    def __str__(self):
        return "Profile of user {}".format(self.user)


class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE )
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, )