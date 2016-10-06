from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, QueryDict
from .forms import RegistrationForm, LoginForm
from .models import MyUser
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django import forms


def test(request):
    print(request.session)
    return HttpResponse('ok test')


class Re(CreateView):
    template_name = 'demo/register.html'
    form_class = RegistrationForm
    # success_url = reverse_lazy('register')
    # context_object_name = 'form'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')
        else:
            return super(Re, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        f = form.save()
        # print(type(f))
        login(self.request, f)
        # print('register and login')
        return redirect('/')

    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated():
    #         return redirect('/')
    #     else:
    #         return super(Re, self).post(request, *args, **kwargs)


def _check(field, value):
    user = None
    item = '{}={}'.format(field, value)
    try:
        user = MyUser.objects.get(**QueryDict(item).dict())
        print(user)
    except MyUser.DoesNotExist:
        return user  # None
    return user


def login_view(request):
    lastpath = '/'  # request.path
    if request.user.is_authenticated:
        return redirect(lastpath)
    if request.method == 'POST':
        error_message = False
        form = LoginForm(request.POST)
        # if form.is_valid():
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        username_or_mobile = request.POST.get('username_or_mobile')
        password = request.POST.get('password')
        user = authenticate(username=username_or_mobile, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('success login use username')
        try:
            user = MyUser.objects.get(mobile=username_or_mobile)
        except MyUser.DoesNotExist:
            error_message = True
        else:
            if check_password(password, user.password):
                login(request, user)
                return HttpResponse('success login use mobile')
            else:
                error_message = True
        # if _check('username', username_or_mobile) is None:
        #     error_message = 'wrong user'
        # if error_message is None and _check('mobile', username_or_mobile) is None:
        #     error_message = 'wrong user'
        # if error_message is not None:
        #     if check_password(password, user.password):
        #         login(request, user)
        #         return HttpResponse('success login use mobile')
        #     else:
        #         error_message = 'wrong password'
        # if _check('username', username_or_mobile) is not None or _check('mobile', username_or_mobile) is not None:
        #     if check_password(password, user.password):
        #         login(request, user)
        #         return HttpResponse('success login use mobile')
        #     else:
        #         error_message = 'wrong password'
        # else:
        #     error_message = 'wrong user'
        return render(request, 'demo/login.html', {'form': form, 'error_message': error_message})

    else:
        form = LoginForm()
        return render(request, 'demo/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponse('you have logouted')

# edit on dev4
# asdgds3456
