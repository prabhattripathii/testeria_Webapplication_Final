from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/student/dashboard')  # redirect to the home page after successful login
        else:
            # Display an error message if authentication fails
            error_message = 'Invalid login credentials. Please try again.'
            return render(request, 'signin.html', {'error_message': error_message})
    else:
        # Display the login form for GET requests
        return render(request, 'signin.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')  # redirect to the home page after successful sign-up
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
#
# def accountsPageFun(request):
#     return render(request, 'signin.html')


# def accountsSignupPageFun(request):
#     return render(request, 'signup.html')
