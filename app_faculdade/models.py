from django.contrib.auth.models import User
from django.db import models

class Pessoa(models.Model):
	nome= models.CharField('Nome',max_length=128)
	email= models.EmailField('E-mail', null=True, blank=True)

	def __str__(self):
		return self.nome


class PessoaFisica(models.Model):
	pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE,blank=True,null=True)
	cpf=models.CharField('CPF', max_length=15,
		help_text='Número do cpf no formato 1111111111',null=True,
		blank=True,)

	def __str__(self):
		return self.cpf

class Evento(models.Model):
	nome= models.CharField('Nome',max_length=128)
	sigla= models.CharField('Sigla',max_length=128)
	data_de_inicio= models.DateField('Data de Inicio', blank=True, null=True)
	realizador=models.ForeignKey(Pessoa, on_delete=models.CASCADE,blank=True,null=True)



	def __str__(self):
		return self.sigla


class Ingresso(models.Model):
	discricao=models.CharField('Nome',max_length=128)
	valor=models.FloatField()
	evento=models.ForeignKey(Evento, on_delete=models.CASCADE,blank=True,null=True)


	def __str__(self):
		return self.discricao



class Iscricao(models.Model):
	pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE,blank=True,null=True)
	evento=models.ForeignKey(Evento, on_delete=models.CASCADE,blank=True,null=True)
	ingresso=models.ForeignKey(Ingresso,on_delete=models.CASCADE,blank=True,null=True)



