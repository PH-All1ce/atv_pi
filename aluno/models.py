from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla_estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome + " - " + self.sigla_estado 

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome 

class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=150)
    endereco = models.CharField(max_length=250)
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_alunos/', blank=True, null=True)

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    especialidade = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_contratacao = models.DateField()
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome