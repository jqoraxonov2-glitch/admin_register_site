from django import forms
from .models import *


class FacultyForm(forms.ModelForm):
    class Meta: # nimaga Faculty da () qavs yo'q
        model = Faculty #=> models dagi Faculty classini modelga tengladik
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }
# widget bu TextInput ni o'zgartirish kiritish uchun kk
# form-control bu css dagi class

class KafedraForm(forms.ModelForm):
    class Meta:
        model = Kafedra
# Django ModelForm ga model ko'rsatilmasa, u qaysi modelning maydonlarini __all__ qilishini
        # bilmaydi va quyidagi xatoni beradi:
        fields = "__all__"
        # fields = "__all__" degani "barcha maydonlarni ol"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }
# Agar siz ma'lumotlar bazasidagi modelga bog'lanmagan, faqat foydalanuvchidan ma('lumot'
#  yig')ish kerak bo'lsa (masalan: login, kontakt forma, qidiruv), unda ModelForm emas,
# oddiy forms.Form ishlatiladi:


class SubjactForm(forms.ModelForm):
    class Meta:
        model = Subjact
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = "__all__"
        widget = {
            "name": forms.TextInput(attrs={'class':"form-control"})
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = "__all__"
        widget = {
            "name":forms.TextInput(attrs={'class':"form-control"})
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
        widget = {
            "name":forms.TextInput(attrs={'class':"form-control"})
        }






















