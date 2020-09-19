from modelo import * 
from vista import *

class Controlador:
	def __init__(self):
		self.__vistaAgenda = Vista()
		self.Home()

	def Home(self):
		seleccion = self.__vistaAgenda.Inicio()
		if seleccion == 1:
			datos = self.__vistaAgenda.CrearAgenda()
			propietario = Agenda(datos[0], datos[1])
			id = datos[0]
			propietario.save()
			self.Menu()
		elif seleccion == 2:
			
			id = self.__vistaAgenda.LoginAgenda()
			user = Agenda.login(id)
			if user:
				self.Menu()
			else:
				entrada = input('No se ha encontrado ninguna agenda... Presione 1 para volver al inicio:\t')
				self.Home()

				
	def Menu(self):
		menu_select = self.__vistaAgenda.Mostrame()
		if menu_select == 1:
			self.__vistaAgenda.VerTodos()





Controlador()
