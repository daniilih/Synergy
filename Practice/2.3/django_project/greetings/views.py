
from django.shortcuts import render, redirect
from .models import UserGreeting
from django.views.decorators.http import require_POST

def index(request):
    last_name = None
    all_names = []

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        
        if not name:
            return redirect('greetings:index') 

        try:
            UserGreeting.objects.create(name=name)
            last_name = name
            return redirect('greetings:index') 
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
            return redirect('greetings:index')

    all_names = UserGreeting.objects.all().order_by('-created_at')[:10]

    context = {
        'last_name': last_name,
        'all_names': all_names,
    }
    return render(request, 'greetings/index.html', context)
