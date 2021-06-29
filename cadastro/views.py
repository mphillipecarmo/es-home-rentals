from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .forms import FormCasa, FormApartamento
from .models import *
import pdb
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html', {})
    
def agendar(request):
    casas = Casa.objects.all()
    apts = Apartamento.objects.all()

    casasExibidas = []
    aptsExibidos = []
    
    bairros = []

    for c in casas:
        bairro = c.endereco.split(', ')[2] 
        if bairro not in bairros:
            bairros.append(bairro)

    for a in apts:
        bairro = a.endereco.split(', ')[2] 
        if bairro not in bairros:
            bairros.append(bairro)

    if 'bairro' in request.GET and request.GET['bairro'] is not '':
        for c in casas:
            bairro = c.endereco.split(', ')[2] 
            if bairro == request.GET['bairro']:
                casasExibidas.append(c)
        for a in apts:
            bairro = a.endereco.split(', ')[2] 
            if bairro == request.GET['bairro']:
                aptsExibidos.append(a)
    else:
        casasExibidas = casas
        aptsExibidos = apts
    context = {
        'casas': casasExibidas,
        'apts': aptsExibidos,
        'bairros': bairros
    }
    return render(request, 'agendar.html', context)
    
def deletar(request):
    id = request.GET['id'] 
    tipoImovel = request.GET['tipoImovel']
    if tipoImovel == 'casa':
        Casa.objects.filter(id=id).delete()
    elif tipoImovel == 'apt':
        Apartamento.objects.filter(id=id).delete()
    return redirect("/listar")
    
def editar(request):
    if request.method == 'POST':     
        form = FormCasa(request.POST)
        # check whether it's valid:
        if form.is_valid():
            qtdeQuartos = form.cleaned_data['qtdeQuartos']
            qtdeSuites = form.cleaned_data['qtdeSuites']
            qtdeSalaEstar = form.cleaned_data['qtdeSalaEstar']
            qtdeVagasGaragem = form.cleaned_data['qtdeVagasGaragem']
            area = form.cleaned_data['area']
            descricao = form.cleaned_data['descricao']
            aluguel = form.cleaned_data['aluguel']
            
            id = request.POST['id']
            
            if request.POST['possuiArmarioEmbutido'] == 'sim':
                possuiArmarioEmbutido = True
            else:
                possuiArmarioEmbutido = False
            
            rua = form.cleaned_data['rua']
            numero = form.cleaned_data['numero']
            bairro = form.cleaned_data['bairro']
            cidade = form.cleaned_data['cidade']
            endereco = rua + ', ' + numero + ', ' + bairro + ', ' + cidade
            
            Casa.objects.filter(id=id).update(qtdeQuartos=qtdeQuartos, qtdeSuites=qtdeSuites, qtdeSalaEstar=qtdeSalaEstar,qtdeVagasGaragem=qtdeVagasGaragem,
            area=area, possuiArmarioEmbutido=possuiArmarioEmbutido, descricao=descricao,endereco=endereco,aluguel=aluguel)
            #casa.save()
            
            return HttpResponseRedirect('/listar')
        else:
            pdb.set_trace()
    else:
    
        id = request.GET['id'] 
        casa = Casa.objects.filter(id=id)
        context = {
            'casa': casa,
            'rua': casa[0].endereco.split(", ")[0],
            'numero': casa[0].endereco.split(", ")[1],
            'bairro': casa[0].endereco.split(", ")[2],
            'cidade': casa[0].endereco.split(", ")[3],
        }
        form = FormCasa()
    #pdb.set_trace()
    return render(request, 'editar.html', context)
    
def editarApt(request):
    if request.method == 'POST':       
        form = FormApartamento(request.POST)
                # check whether it's valid:
        if form.is_valid():
            qtdeQuartos = form.cleaned_data['qtdeQuartos']
            qtdeSuites = form.cleaned_data['qtdeSuites']
            qtdeSalaEstar = form.cleaned_data['qtdeSalaEstar']
            qtdeVagasGaragem = form.cleaned_data['qtdeVagasGaragem']
            qtdeSalaJantar = form.cleaned_data['qtdeSalaJantar']
            area = form.cleaned_data['area']
            andar = form.cleaned_data['andar']
            valorCondominio = form.cleaned_data['valorCondominio']
            descricao = form.cleaned_data['descricao']
            aluguel = form.cleaned_data['aluguel']
            id = request.POST['id']
            if request.POST['possuiArmarioEmbutido'] == 'sim':
                possuiArmarioEmbutido = True
            else:
                possuiArmarioEmbutido = False
                
            if request.POST['possuiPortaria'] == 'sim':
                possuiPortaria = True
            else:
                possuiPortaria = False
            
            rua = form.cleaned_data['rua']
            numero = form.cleaned_data['numero']
            bairro = form.cleaned_data['bairro']
            cidade = form.cleaned_data['cidade']
            #pdb.set_trace()
            endereco = rua + ', ' + numero + ', ' + bairro + ', ' + cidade
            
            Apartamento.objects.filter(id=id).update(qtdeQuartos=qtdeQuartos, qtdeSuites=qtdeSuites, qtdeSalaEstar=qtdeSalaEstar,qtdeVagasGaragem=qtdeVagasGaragem,qtdeSalaJantar=qtdeSalaJantar,
            andar=andar,valorCondominio=valorCondominio,possuiPortaria=possuiPortaria,area=area, possuiArmarioEmbutido=possuiArmarioEmbutido, descricao=descricao,endereco=endereco,aluguel=aluguel)
            return HttpResponseRedirect('/listar')
        #pdb.set_trace()
        return HttpResponseRedirect('/falhou')
    else:
    
        id = request.GET['id'] 
        apt = Apartamento.objects.filter(id=id)
        context = {
            'apt': apt,
            'rua': apt[0].endereco.split(", ")[0],
            'numero': apt[0].endereco.split(", ")[1],
            'bairro': apt[0].endereco.split(", ")[2],
            'cidade': apt[0].endereco.split(", ")[3],
        }
        form = FormApartamento()
    #pdb.set_trace()
    return render(request, 'editarApt.html', context)
      

def listar(request):
    casas = Casa.objects.all()
    apts = Apartamento.objects.all()

    context = {
        'casas': casas,
        'apts': apts,
    }
    return render(request, 'listar.html', context)

def agendamento(request):
    if request.method == 'POST':

        data = request.POST['data']
        idImovel = request.POST['id']
        tipoImovel = request.POST['tipoImovel']
        horario = request.POST['horario']
        nomeCliente = request.POST['nomeCliente']
        data = data +' ' + horario + ':0'
        
        novoHorario = HorarioMarcado(idImovel=idImovel, tipoImovel=tipoImovel, data=data, nomeCliente=nomeCliente)
        novoHorario.save()
        messages.success(request, "Horário Agendado com sucesso!")
        return redirect('/')
    else:
        idImovel = request.GET['id']
        if request.GET['tipoImovel'] == 'casa':
            casa = Casa.objects.filter(id=idImovel)
            tipoImovel = 'casa'
            context = {
                'imovel' : casa,
                'tipoImovel': 'casa',
                'rua' : casa[0].endereco.split(', ')[0],
                'numero' : casa[0].endereco.split(', ')[1],
                'bairro' : casa[0].endereco.split(', ')[2],
                'cidade' : casa[0].endereco.split(', ')[3]      
            }
        elif request.GET['tipoImovel'] == 'apt':
            apt = Apartamento.objects.filter(id=idImovel)
            tipoImovel = 'apt'
            context = {
                'imovel' : apt,
                'tipoImovel': 'apt' ,
                'rua' : apt[0].endereco.split(', ')[0] ,
                'numero' : apt[0].endereco.split(', ')[1] ,
                'bairro' : apt[0].endereco.split(', ')[2] ,
                'cidade' : apt[0].endereco.split(', ')[3]
            }
        if 'data' in request.GET:
            data = request.GET['data']
            horariosLivres = []
            horariosOcupados = []
            reservas = HorarioMarcado.objects.filter(idImovel=idImovel,tipoImovel=tipoImovel)
            for r in reservas:
                horariosOcupados.append(r.data.hour)
            
            for i in range(8,18):
                if i not in horariosOcupados:
                    horariosLivres.append(str(i))
            #pdb.set_trace()
            context['data'] = data
            context['horariosLivres'] = horariosLivres
            return render(request, 'agendamento2.html', context)
        else:
            return render(request, 'agendamento.html', context)
    

    
def cadastro(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        if request.POST['tipoImovel'] == 'casa':
            form = FormCasa(request.POST)
            # check whether it's valid:
            if form.is_valid():
                qtdeQuartos = form.cleaned_data['qtdeQuartos']
                qtdeSuites = form.cleaned_data['qtdeSuites']
                qtdeSalaEstar = form.cleaned_data['qtdeSalaEstar']
                qtdeVagasGaragem = form.cleaned_data['qtdeVagasGaragem']
                area = form.cleaned_data['area']
                descricao = form.cleaned_data['descricao']
                aluguel = form.cleaned_data['aluguel']
                
                if request.POST['possuiArmarioEmbutido'] == 'sim':
                    possuiArmarioEmbutido = True
                else:
                    possuiArmarioEmbutido = False
                
                rua = form.cleaned_data['rua']
                numero = form.cleaned_data['numero']
                bairro = form.cleaned_data['bairro']
                cidade = form.cleaned_data['cidade']
                #pdb.set_trace()
                endereco = rua + ', ' + numero + ', ' + bairro + ', ' + cidade
                
                casa = Casa(qtdeQuartos=qtdeQuartos, qtdeSuites=qtdeSuites, qtdeSalaEstar=qtdeSalaEstar,qtdeVagasGaragem=qtdeVagasGaragem,
                area=area, possuiArmarioEmbutido=possuiArmarioEmbutido, descricao=descricao,endereco=endereco,aluguel=aluguel)
                casa.save()
                messages.success(request, "Imóvel cadastrado com sucesso!")
                return HttpResponseRedirect('/')
            else:
                pdb.set_trace()
        elif request.POST['tipoImovel'] == 'apartamento':
            form = FormApartamento(request.POST)
            # check whether it's valid:
            if form.is_valid():
                qtdeQuartos = form.cleaned_data['qtdeQuartos']
                qtdeSuites = form.cleaned_data['qtdeSuites']
                qtdeSalaEstar = form.cleaned_data['qtdeSalaEstar']
                qtdeVagasGaragem = form.cleaned_data['qtdeVagasGaragem']
                qtdeSalaJantar = form.cleaned_data['qtdeSalaJantar']
                area = form.cleaned_data['area']
                andar = form.cleaned_data['andar']
                valorCondominio = form.cleaned_data['valorCondominio']
                descricao = form.cleaned_data['descricao']
                aluguel = form.cleaned_data['aluguel']
                
                if request.POST['possuiArmarioEmbutido'] == 'sim':
                    possuiArmarioEmbutido = True
                else:
                    possuiArmarioEmbutido = False
                    
                if request.POST['possuiPortaria'] == 'sim':
                    possuiPortaria = True
                else:
                    possuiPortaria = False
                
                rua = form.cleaned_data['rua']
                numero = form.cleaned_data['numero']
                bairro = form.cleaned_data['bairro']
                cidade = form.cleaned_data['cidade']
                #pdb.set_trace()
                endereco = rua + ', ' + numero + ', ' + bairro + ', ' + cidade
                
                apt = Apartamento(qtdeQuartos=qtdeQuartos, qtdeSuites=qtdeSuites, qtdeSalaEstar=qtdeSalaEstar,qtdeVagasGaragem=qtdeVagasGaragem,qtdeSalaJantar=qtdeSalaJantar,
                andar=andar,valorCondominio=valorCondominio,possuiPortaria=possuiPortaria,area=area, possuiArmarioEmbutido=possuiArmarioEmbutido, descricao=descricao,endereco=endereco,aluguel=aluguel)
                apt.save()
                
                return HttpResponseRedirect('/listar')
            else:
                pdb.set_trace()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormCasa()

    return render(request, 'cadastro.html', {'form': form})
    