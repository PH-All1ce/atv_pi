from django.shortcuts import render,get_object_or_404,redirect
from .models import Aluno,Curso,Cidade, Professor
from .forms import AlunoForm, CidadeForm, ProfessorForm

def aluno_editar(request,id):
    aluno = get_object_or_404(Aluno,id=id)
   
    if request.method == 'POST':
        form = AlunoForm(request.POST,request.FILES,instance=aluno)

        if form.is_valid():
            form.save()
            return redirect('aluno_listar')
    else:
        form = AlunoForm(instance=aluno)

    return render(request,'aluno/form.html',{'form':form})


def aluno_remover(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('aluno_listar') # procure um url com o nome 'lista_aluno'


def aluno_criar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlunoForm()
            return redirect('aluno_listar')

    else:
        form = AlunoForm()

    return render(request, "aluno/form.html", {'form': form})


def aluno_listar(request):
    alunos = Aluno.objects.all()
    context ={
        'alunos':alunos
    }
    return render(request, "aluno/alunos.html",context)


def index(request):
    total_alunos = Aluno.objects.count()
    total_cidades = Cidade.objects.count()
    total_curso = Curso.objects.count()
    context = {
        'total_alunos' : total_alunos,
        'total_cidades' : total_cidades,
        'total_cursos' : total_curso
    }
    return render(request, "aluno/index.html",context)


def curso_listar(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, "aluno/curso_listar.html", context)

def cidade_criar(request):
    if request.method == 'POST':
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            form = CidadeForm()
            return redirect('cidade_listar')
    else:
        form = CidadeForm()

    context= {
        'form': form
    }
 
    return render(request, "cidade/form.html",context)


def cidade_listar(request):
    cidade = Cidade.objects.all()
    context = {
        'cidade' : cidade
    }
    return render(request, 'cidade/cidade_listar.html', context)

def cidade_remover(request, id):
    cidade = get_object_or_404(Cidade, id=id)
    cidade.delete
    return redirect('cidade_listar')

def listar_professor(request):
    professor = Professor.objects.all()
    context = {
        'professores' : professor
    }
    return render(request, "professor/professor.html", context)

def professor_criar(request):
    form = ProfessorForm(request.POST)


    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        
        if form.is_valid():
            form.save()
            form = ProfessorForm()
            return redirect('listar_professor')

    return render(request, 'professor/form.html', { 'form' : form})

def professor_editar(request, id):
    professor = get_object_or_404(Professor, id=id)

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('listar_professor')
    else:
        form = ProfessorForm(instance=professor)

        return render(request, 'professor/form.html', {'form' : form})
    

def professor_remover(request, id):
    professor = get_object_or_404(Professor, id=id)
    professor.delete()
    return redirect('listar_professor')