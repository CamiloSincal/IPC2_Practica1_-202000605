from graphviz import Digraph
from graphviz import Source

dot = Digraph(
    name='Agenda',
    filename=None,
    directory=None,
    format="png",
    engine=None,
    encoding='utf8',
    graph_attr={'rankdir':'TB'},
    node_attr={'color':'black','fontcolor':'black','fontname':'FangSong','fontsize':'12','style':'rounded','shape':'box'},
    edge_attr={'color':'#999999','fontcolor':'#888888','fontsize':'10','fontname':'FangSong'},
    body=None,
    strict=False
)

def agregarPersona():
    print('Ingrese un nombre')
    nombre = input()
    print('Ingrese un apellido')
    apellido = input()
    print('Ingrese un número de teléfono')
    numero = input()
    lista.agregar(nombre,apellido,numero)
    menu()

def menu():
    global lista
    print('========= Menú Principal ==============')
    print('| 1-. Ingresar nuevo contacto         |')
    print('| 2-. Buscar contacto                 |')
    print('| 3-. Visualizar agenda               |')
    print('=======================================')
    print('Ingrese la opción que desea:')
    opcion = int(input())
    if(opcion == 1):
        agregarPersona()
    elif(opcion == 2):
        numero = input("Digite el numero que desea buscar\n")
        lista.buscar(numero)
    elif(opcion == 3):
        lista.generarGrafico()

class nodo:
    def __init__(self,nombre,apellido,numero):
        self.anterior = None
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.siguiente = None

class listadoble:
    def __init__(self):
        self.Primero = None
        self.Ultimo = None
    
    def agregar(self,nombre,apellido,numero):
        nuevoNodo = nodo(nombre,apellido,numero)

        aux1 = self.Primero

        poderAgregar = True
        auxComprobar = self.Primero
        auxCApellido = self.Primero
        conApellido = True
        
        while(auxCApellido != None):
            if(auxCApellido.apellido == apellido):
                conApellido = False
                break
            auxCApellido = auxCApellido.siguiente

        while(auxComprobar != None):
            if(auxComprobar.numero == numero):
                poderAgregar = False
                break
            auxComprobar = auxComprobar.siguiente

        if(poderAgregar):
            if(conApellido):
                while(aux1 != None and str(aux1.apellido).lower() < str(apellido).lower()):
                    aux2 = aux1
                    aux1 = aux1.siguiente
                    
                if(self.Primero == aux1):
                    self.Primero = nuevoNodo
                    self.Ultimo = nuevoNodo
                else:
                    nuevoNodo.anterior = aux2
                    aux2.siguiente = nuevoNodo
                nuevoNodo.siguiente = aux1
            else:
                while(aux1 != None and str(aux1.nombre).lower() < str(nombre).lower()):
                    aux2 = aux1
                    aux1 = aux1.siguiente
                    
                if(self.Primero == aux1):
                    self.Primero = nuevoNodo
                    self.Ultimo = nuevoNodo
                else:
                    nuevoNodo.anterior = aux2
                    aux2.siguiente = nuevoNodo
                nuevoNodo.siguiente = aux1
        else:
            print("Ya existe un contacto con este número")


    def buscar(self, numero):
        aux = self.Primero
        encontrado = False
        while(aux != None):
            if(aux.numero == numero):
                print("Nombre: ",aux.nombre)
                print("Apellido: ",aux.apellido)
                print("Numero: ",aux.numero)
                encontrado = True
                menu()
                break
            aux = aux.siguiente
        if(encontrado == False):
            opcion = int(input("El número de teléfono no existe, ¿Desea agregarlo? [1 = Si][2 = No]\n"))
            if opcion == 1:
                agregarPersona()
            elif opcion == 2:
                menu()

    def generarGrafico(self):
        aux = self.Primero
        while(aux != None):
            print(aux.apellido)
            dot.node(str(aux),'Nombre: ' + str(aux.nombre)+'\n' +'Apellido: ' +str(aux.apellido)+'\n'+ 'Número: ' +str(aux.numero)+'\n')
            aux = aux.siguiente

        aux = self.Primero
        while(aux.siguiente != None):
            dot.edge(str(aux),str(aux.siguiente),' ', _attributes={'dir':'both'})
            aux = aux.siguiente
            
        dot.view()

lista = listadoble()

#Llamada de métodos
menu()


