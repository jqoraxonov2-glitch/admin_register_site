from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None: # agar user avval mavjud bo'lmasa
            login(request, user) #login qil
            return redirect("home_page") # homa _pagega

    return render(request, 'login.html') # aks holda login

@login_required_decorator
def home_page(request):
    # bosh sahifadagi statistika blokiga (masalan:
    # "Bizda 5 ta fakultet va 20 ta kafedra bor") yuborishdir.
    # 1. Bazadan hamma fakultet va kafedralarni olib keladi (List ko'rinishida)
    faculties = services.get_faculties() # servicesdagi sql funcsiya
    kafedras = services.get_kafedra()

    # 2. "ctx" (Context) - bu HTML-ga yuboriladigan ma'lumotlar qopchasi
    ctx = {
        'counts': { # counts orqali htmlda count.faculties deb murojat qilish mumkin
            # Bu yerda len() orqali ro'yxat uzunligini (sonini) olyapmiz
            'faculties': len(faculties), # len bizga list yoki touple kelsa True qaytaradi
            'kafedras': len(kafedras), # aks holda TypeError yani xatolikni tutish uchun kk len()
        }
    }
    # 3. index.html faylini yuklaydi va ctx ichidagi ma'lumotlarni unga joylaydi
    return render(request, 'index.html', ctx)


@login_required_decorator
def faculty_create(request):
    model = Faculty() # modelsdagi name fieldi keladi modelga
    form = FacultyForm(request.POST or None, instance=model) #instance orqali saqlanadi modelga
    if request.POST and form.is_valid(): # FacultyForm input widgeti bor
        form.save()
        return redirect('faculty_list') # yangi yaratilgach yana facultetlar ro'yxatini chiqaramiz
    ctx = {
        # key : value
        "form": form # FacultyForm input widgeti bor
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_edit(request, pk):# primary_key
    model = Faculty.objects.get(pk=pk)  # pk ni htmldagi faculty id siga tenglaymiz
    form = FacultyForm(request.POST or None, instance=model) # FacultyForm inputli widget
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        "model": model, # modelga id(pk) dagi obj
        "form": form    # FacultyForm inputli widget
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()
    return redirect('faculty_list')


@login_required_decorator
def faculty_list(request): # get so'rovi
    faculties = services.get_faculties()
    print(faculties)
    ctx = {
        "faculties": faculties
    }
    return render(request, 'faculty/list.html', ctx)


# KAFEDRA
@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        "form": form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_edit(request, pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_delete(request, pk):
    model = Kafedra.objects.get(pk=pk)
    model.delete()
    return redirect('kafedra_list')


@login_required_decorator
def kafedra_list(request):
    kafedras = services.get_kafedra()
    ctx = {
        "kafedras": kafedras
    }
    return render(request, 'kafedra/list.html', ctx)



@login_required_decorator
def subjact_create(request):
    model = Subjact()
    form = SubjactForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subjact_list')
    ctx = {
        "form" : form
    }
    return render(request, 'subjact/form.html', ctx)


@login_required_decorator
def subjact_edit(request, pk):
    model = Subjact.objects.get(pk=pk)
    form = SubjactForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subjact_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request, 'subjact/form.html', ctx)


@login_required_decorator
def subjact_delete(request, pk):
    model = Subjact.objects.get(pk=pk)
    model.delete()
    return redirect('subjact_list')


@login_required_decorator
def subjact_list(request):
    subjact = services.get_subjact()
    ctx = {
        "subjact":subjact
    }
    return render(request, 'subjact/list.html', ctx)


@login_required_decorator
def teacher_create(request):
    model = Teachers()
    form = TeacherForm(request.POST, instance=model) #model ichida key value lar form kadvalni o'zi
    if request.POST and form.is_valid():
        form.save()
        return redirect('teacher_list')
    ctx = {
        "form":form
    }
    return render(request, 'teachers/form.html', ctx)


@login_required_decorator
def teacher_edit(request, pk):
    model = Teachers.objects.get(pk=pk)
    form = TeacherForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teacher_list')
    ctx ={
        "model":model,
        "form":form
    }
    return render(request, 'teachers/form.html', ctx)


@login_required_decorator
def teacher_delete(request, pk):
    model = Teachers.objects.get(pk=pk)
    model.delete()
    return redirect('teacher_list')


@login_required_decorator
def teacher_list(request):
    teachers = services.get_teachers()
    ctx = {
        "teachers":teachers
    }
    return render(request, 'teachers/list.html', ctx)


@login_required_decorator
def group_create(request):
    model = Groups()
    form = GroupForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('group_list')
    ctx = {
        "form":form
    }
    return render(request, "group/form.html", ctx)


@login_required_decorator
def group_edit(request, pk):
    model = Groups.objects.get(pk=pk)
    form = GroupForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('group_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request, 'group/form.html', ctx)


@login_required_decorator
def group_delete(request, pk):
    model = Groups.objects.get(pk=pk)
    model.delete()
    return redirect('group_list')


@login_required_decorator
def group_list(request):
    group = services.get_groups()
    ctx = {
        "group": group
    }
    return render(request, 'group/list.html', ctx)


@login_required_decorator
def student_create(request):
    model = Students()
    form = StudentForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx = {
        "form":form
    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_edit(request, pk):
    model = Students.objects.get(pk=pk)
    form = StudentForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx = {
    "model":model,
    "form":form
    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_delete(request, pk):
    model = Students.objects.get(pk=pk)
    model.delete()
    return redirect('student_list')


@login_required_decorator
def student_list(request):
    student = services.get_student()
    ctx = {
        "student":student
    }
    return render(request, 'student/list.html', ctx)


