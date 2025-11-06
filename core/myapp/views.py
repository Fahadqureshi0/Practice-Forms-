from django.shortcuts import render,redirect,get_object_or_404
from .forms import ApplicationForm


# Application view:

def app_view(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_profile")
        return render(request, "myapp/forms.html", {"form":form})
    else:
        form = ApplicationForm()
        return render(request, "myapp/forms.html", {"form":form})
