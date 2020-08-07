from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import Profile

# Create your views here.
def signup(request):
    print(request.POST)

    print(request.user)

    # You can only run the signup script if no user is authenticated

    if request.user.is_authenticated == False:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)

            if form.is_valid():
                new_user = form.save(commit=False)

                new_user.set_password(form.cleaned_data['password'])

                new_user.save()

                # create a profile for the user
                Profile.objects.create(
                    user=new_user,
                    gender='Not Identified'
                )

                # return a seperate template if the form is validated successfully
                return render(request, 'account/signup_done.html', {'new_user':new_user})

        else:
            form = UserRegistrationForm()

    else:
        return redirect('logout')

    return render(request, 'account/signup.html', {'form':form})

