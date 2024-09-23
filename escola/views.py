from django.shortcuts import render,redirect
from .forms import AlunoForm
# Create your views here.

def cadastro(request):
    form = AlunoForm()

    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')
    
    contexto = {
        'form': form
    }
    return render(request, 'escola/cadastro.html', contexto)
