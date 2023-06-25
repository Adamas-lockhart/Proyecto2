from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template import loader

def saludo(request):
    return HttpResponse("hola django - equipo coder 1")
def vista2(request):
    return HttpResponse("prueba 2")

def probandoTemplate(self):
    
    nom = "santino"
    ap = "de cicco"
    ListaDeNotas = [1, 2, 3, 4, 5, 6, 7]
    
    diccionario = {"nombre":nom, "apellido":ap, "hoy": datetime.datetime.now, "notas": ListaDeNotas}
    
    #esta forma es mas lenta, abajo se usan cargadores
    #mihtml = open("C:\\Users\\mogli\\Desktop\\PythonProyecto1\\Proyecto1\\Proyecto1\\plantillas\\template1.html")
    #plantilla = Template(mihtml.read())
    #mihtml.close
    #miContexto = Context(diccionario)
    #documento = plantilla.render(micontexto)
    
    plantilla = loader.get_template('template1.html')
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)


