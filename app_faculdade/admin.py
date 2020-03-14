from django.contrib import admin
from .models import PessoaFisica,Pessoa,Evento,Ingresso,Iscricao

@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
	pass


@admin.register(Pessoa)
class Pessoa(admin.ModelAdmin):
	pass

@admin.register(Evento)
class Evento(admin.ModelAdmin):
	pass

@admin.register(Ingresso)
class Ingresso(admin.ModelAdmin):
	pass


@admin.register(Iscricao)
class Iscricao(admin.ModelAdmin):
	pass