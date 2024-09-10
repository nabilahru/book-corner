from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Nabilah Roslita Utami',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)