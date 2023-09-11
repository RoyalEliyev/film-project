from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "signup.html")
    

    def post(self, request, *args, **kwargs):
        if request.method == "POST":

            """
            request.POST = {
            "username" : "royaleliyev"
            "passoword" : "royal12345"
            }

            """
            username = request.POST.get("username")
            password = request.POST.get("password")
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                username=username,
                password=password
            )
            else:
                messages.info(request, "Username artiq movcuddur")
            return redirect("signup")


# def register(request):
#     # return render(request, "signup.html")
#     if request.method == "POST":

#         """
#         request.POST = {
#         "username" : "royaleliyev"
#         "passoword" : "royal12345"
#         }

#         """
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         if not User.objects.filter(username=username).exists():
#             User.objects.create_user(
#                username=username,
#                password=password
#         )
#         else:
#             messages.info(request, "Username artiq movcuddur")
#         return redirect("signup")
#     return render(request, "signup.html")


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.info(request, "Zehmed olmasa, duzgun melumat daxil edin.")
                return redirect("login")

    

# def loginUser(request):
    # if request.method == "POST":
    #     username = request.POST.get("username")
    #     password = request.POST.get("password")

    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         login(request, user)
    #         return redirect("index")
    #     else:
    #         messages.info(request, "Zehmed olmasa, duzgun melumat daxil edin.")
    #         return redirect("login")
    # return render(request, "login.html")


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")
        

# def logoutUser(request):
#     logout(request)
#     return redirect("login")