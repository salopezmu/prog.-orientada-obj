class encuesta:
    #atributos
    def __init__(self,nombre,carrera,numIdeas,ideaProy):
        self.nombre=nombre
        self.carrera=carrera
        self.numIdeas=numIdeas
        self.ideaProy=ideaProy
    
    #metodos
    def respuestas(self):
        nombre=input("ingresa tu nombre\n")
        carrera=input("ingresa tu carrera\n")
        respuestaIdeas=int(input("cuantas ideas tienes para tu proyecto?(ingrese un numero natural para la cantidad)\n"))
        for i in range(0,respuestaIdeas):
            ideasProyecto=[]
            ideasProy=input("cual(es) idea(s) tienes para tu proyecto?\n")
            ideasProyecto.append(ideasProy)
        return nombre, carrera, respuestaIdeas, ideasProyecto
    def imprimir(self,nombre,carrera,respuestaIdeas,ideasProyecto):
        print(f"la persona {nombre} de la carrera {carrera} tiene la(s) siguente(s) {respuestaIdeas} idea(s) de proyecto: {ideasProyecto}")

encuesta.respuestas(encuesta)