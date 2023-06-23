from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from cartridge.models import TransferCartridge
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.shortcuts import render

from employees.models import Employee
from ingener1.models import NalichiTehniki
from doc.models import Documentation
from application.models import Application, Tender
from network.models import Transfernetwork, Report
from .models import *
from django.http import HttpResponse
from knuCCiIT.decorator import for_networks
menu = [{'title': "Картридж", 'url_name': 'cartridge'}, ]

@login_required
def cartridge(request):
    cartridges = TransferCartridge.objects.all()
    return render(request, 'pages/cartridge.html', {'cartridges': cartridges})


@login_required
def index(request):
    return render(request, 'pages/index.html')

@login_required
def mainpage(request):
    return render(request, 'pages/mainpage.html')

@login_required
def nalichiTehniki(request):
    if request.user.role.title == 'admin':
        nalichiTehnikie = NalichiTehniki.objects.all()
    else:
        nalichiTehnikie = NalichiTehniki.objects.filter(user=request.user)
    return render(request, 'pages/tehniki.html', {'nalichiTehnikie': nalichiTehnikie})

@login_required
@for_networks
def idview(request, id):
    idviewe = Transfernetwork.objects.filter(Report_id=id)
    print(idviewe)
    return render(request, 'pages/network.html', {'idviewe': idviewe})

@login_required
def list_reports(request):
    reports = Report.objects.all()
    return render(request, 'pages/reports.html', {'reports': reports})

@login_required
def Report_koruu(request, id):
    idviewe = Report.objects.filter(Report=id)
    return render(request, 'pages/network.html', {'id_viewe': idviewe})

@login_required
def kabinet(request):
    if request.user.role.title == 'admin':
         kabinetter = Kabinet.objects.all()
    else:
        campus_ids = request.user.role.campus.all().values_list('id', flat=True)
        print(campus_ids)
        kabinetter = Kabinet.objects.filter(campus_id__in=campus_ids)
    return render(request, 'pages/kabinet.html', {'kabinetter': kabinetter})

@login_required
def kabinet_koruu(request, id):
    if request.user.role.title == 'admin':
        nalichiTehnikie = NalichiTehniki.objects.all()
    else:
        nalichiTehnikie = NalichiTehniki.objects.filter(user_id=request.user.id, kabinet_id=id)
    return render(request, 'pages/tehniki.html', {'nalichiTehnikie': nalichiTehnikie})

@login_required
def category_koruu(request, id):
    if request.user.role.title == 'admin':
        nalichiTehnikie = NalichiTehniki.objects.all()
    else:
        nalichiTehnikie = NalichiTehniki.objects.filter(user_id=request.user.id, category_id=id)
    return render(request, 'pages/tehniki.html', {'nalichiTehnikie': nalichiTehnikie})

@login_required
def Campus_koruu(request, id):
    buiumdar = NalichiTehniki.objects.filter(Campus_id=id)
    return render(request, 'pages/tehniki.html', {'nalichiTehnikie': buiumdar})

@login_required
def category(request):
    categoryler = Category.objects.all()
    return render(request, 'pages/categoty.html', {'categoryler': categoryler})

@login_required
def campus(request):
    campusler = Campus.objects.all()
    return render(request, 'pages/campus.html', {'campusler': campusler})

@login_required
def documentation(request):
    documentationiee = Documentation.objects.all()
    return render(request, 'pages/documentation.html', {'documentationiee': documentationiee})


@login_required
def application(request):
    applications = Application.objects.all()
    return render(request, 'pages/application_documents.html', {'applications': applications})


@login_required
def tender(request):
    tenders = Tender.objects.all()
    return render(request, 'pages/application_documents1.html', {'tenders': tenders})


@login_required
def sostoyanieny_koruu(request, filter):
    if request.user.role.title == 'admin':
        nalichiTehnikie = NalichiTehniki.objects.all()
    else:
        nalichiTehnikie = NalichiTehniki.objects.filter(user_id=request.user.id, sostoyanie=filter)

    return render(request, 'pages/tehniki.html', {'nalichiTehnikie': nalichiTehnikie})


class UserLoginView(LoginView):
    template_name = 'pages/login.html'
    redirect_authenticated_user = True
    form_class = AuthenticationForm


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('index')

        else:
            return render(
                request=request,
                template_name="pages/login.html",
                context={'test': 'test'}  # TODO test
            )

    form = AuthenticationForm()

    return render(
        request=request,
        template_name="pages/login.html",
        context={'form': form}
    )

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
