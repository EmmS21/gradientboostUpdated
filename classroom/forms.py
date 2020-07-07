from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.forms.utils import ValidationError
import datetime
from django.forms import ModelForm, Textarea, TextInput
from django.core.files.images import get_image_dimensions
from allauth.account.views import SignupForm
from classroom.models import Mentor 
from classroom.models import (Answer, Question, Student, StudentAnswer,
                              Subject, Mentor)
from django.contrib.auth import get_user_model
User = get_user_model()


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

class TeacherSignUpForm(SignupForm):
    user_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "Username",}), 
                                required=True)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "First Name",}), 
                                required=True)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "Last Name",}), 
                                required=True)
    
    #contact details
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "City",}), 
                                required=True)
    country = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "Country",}), 
                                required=True)
    current_occupation = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "Current Occupation",}),
                                required=True)
    linkedin = forms.URLField(max_length=200, widget=forms.URLInput(attrs={'placeholder':'Linkedin',}), 
                                required=True)
    github = forms.URLField(max_length=200, widget=forms.URLInput(attrs={'placeholder':'Github',}), 
                                required=True)


    phone_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "Phone Number including country code",}), 
                                required=True)

    contact_day = forms.ChoiceField(widget=forms.Select(attrs={
        "class": "form-control",
    }), required=True, choices=day_choices)

    contact_time = forms.ChoiceField(widget=forms.Select(attrs={
        "class": "form-control",
    }),  required=True, choices=time_choices)

 
    # address = forms.CharField(max_length=500, required=True)
    # billing_name = forms.CharField(max_length=200, required=True)
    # account_num = forms.IntegerField(required=True)
    # bank_name = forms.CharField(max_length=50, required=True)
    # branch_code = forms.IntegerField(required=True)
    def save(self,request, commit=True):
        user = super(TeacherSignUpForm, self).save(request) 
        user.is_teacher = True
        user.is_active = True 
        user.is_allow = False #custom active function. you can play with it or is_active
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        try:
            user_Name = str(user.email).split('@')[0]
            user.username = user_Name
        except:
            user.username = user.first_name

        user.save()
        mentor = Mentor.objects.get_or_create(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],

            city=self.cleaned_data['city'],
            country=self.cleaned_data['country'],
            current_occupation=self.cleaned_data['current_occupation'],
            linkedin=self.cleaned_data['linkedin'],
            github=self.cleaned_data['github'],
            
            phone_no=self.cleaned_data['phone_no'],
            contact_day=self.cleaned_data['contact_day'],
            contact_time=self.cleaned_data['contact_time'],

            # address=self.cleaned_data['address'],
            # billing_name=self.cleaned_data['billing_name'],
            # account_num=self.cleaned_data['account_num'],
            # bank_name=self.cleaned_data['bank_name'],
            # branch_code=self.cleaned_data['branch_code'],
        )
        return user

class StudentSignUpForm(SignupForm):
    user_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "Username",}), 
                                required=True)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "First Name",}), 
                                required=True)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "Last Name",}), 
                                required=True)

    #contact details
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "City",}), 
                                required=True)
    country = forms.ChoiceField(widget=forms.Select(attrs={
        "class":"form-control",
    }), required=True, choices=country_choices)

    current_occupation = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "Current Occupation",}),
                                required=True)
    linkedin = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder':'Linkedin',}),
                                required=True)
    # github = forms.URLField(max_length=200, widget=forms.URLInput(attrs={'placeholder':'Github',}), 
    #                             required=True)
    phone_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "Phone Number including country code",}), 
                                required=True)
    employed = forms.ChoiceField(widget=forms.Select(attrs={
        "class": "form-control",
    }), required=True, choices=employed_choices)

    installments =  forms.ChoiceField(widget=forms.Select(attrs={
        "clas": "form-control",
    }), required=True, choices=installment_choices)

    contact_day = forms.ChoiceField(widget=forms.Select(attrs={
        "class": "form-control",
    }), required=True, choices=day_choices)

    # installnum = forms.ChoiceField(widget=forms.Select(attrs={
    #     "class": "form-control",
    # }), required=False, choices=installnum_choices)

    contact_time = forms.ChoiceField(widget=forms.Select(attrs={
        "class": "form-control",
    }),  required=True, choices=time_choices)


    def save(self,request, commit=True):
        user = super(StudentSignUpForm, self).save(request) 
        user.is_student = True
        user.is_active = True 
        user.is_allow = False
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        try:
            user_Name = str(user.email).split('@')[0]
            user.username = user_Name
        except:
            user.username = user.first_name
        user.save()
        mentor = Student.objects.get_or_create(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],

            city=self.cleaned_data['city'],
            country=self.cleaned_data['country'],
            current_occupation=self.cleaned_data['current_occupation'],
            linkedin=self.cleaned_data['linkedin'],
            # github=self.cleaned_data['github'],
            
            phone_no=self.cleaned_data['phone_no'],
            contact_day=self.cleaned_data['contact_day'],
            contact_time=self.cleaned_data['contact_time'],
            employed=self.cleaned_data['employed'],
            installments=self.cleaned_data['installments'],
            # installnum=self.cleaned_data['installnum'],
        )
        return user



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text',)


class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct', False):
                    has_one_correct_answer = True
                    break
        if not has_one_correct_answer:
            raise ValidationError('Mark at least one answer as correct.', code='no_correct_answer')


class TakeQuizForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None)

    class Meta:
        model = StudentAnswer
        fields = ('answer',)

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answers.order_by('text')


#basic form
class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

# edit mentor payment details
class MentorPaymentForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('address', 'billing_name', 'account_num', 'bank_name', 'branch_code')


# basic form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_student = True
    #     user.save()
    #     student = Student.objects.create(user=user)
    #     # student.email.add(*self.cleaned_data.get('email'))
    #     # student.firstname.add(*self.cleaned_data.get('firstname'))
    #     # student.lastname.add(*self.cleaned_data.get('lastname'))
    #     # student.phone.add(*self.cleaned_data.get('phone'))
    #     student.interests.add(*self.cleaned_data.get('interests'))
    #     return user


# class StudentInterestsForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ('interests', )
#         widgets = {
#             'interests': forms.CheckboxSelectMultiple
#         }
#
#edit mentor payment details
# class MentorPaymentForm(forms.ModelForm):
#     class Meta:
#         model = Mentor
#         fields = ('address', 'country', 'invoice_name', 'account_num', 'bank_name', 'branch_code')
