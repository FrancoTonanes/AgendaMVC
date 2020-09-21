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
			global id
			id = datos[0]
			try:
				propietario.save()
				self.Menu()
			except:
				self.__vistaAgenda.Mensajes('\nLa clave ya existe')
				self.Home()
		elif seleccion == 2:
			id = self.__vistaAgenda.LoginAgenda()
			user = Agenda.login(id)
			if user:
				self.Menu()
			else:
				self.__vistaAgenda.Mensajes('\nNo se ha encontrado ninguna agenda\t')
				self.Home()


				
	def Menu(self):
		menu_select = self.__vistaAgenda.Mostrame()

		if menu_select == 1:
			lista = Contacto.Todos(id)
			Vista.VerTodos(lista)
			self.Menu()


		elif menu_select == 2:
			op = self.__vistaAgenda.VistaBuscar()
			if op == 1:
				datos = self.__vistaAgenda.PedirDatos('nombre')
				contacto = Contacto.BuscarNombre(datos['nombre'], id)
				if contacto:
					Vista.VerTodos(contacto)
					self.Menu()
				else:
					self.__vistaAgenda.Mensajes('\n---------No se ha encontrado el contacto\n')
					self.Menu()
			elif op == 2:
				datos = self.__vistaAgenda.PedirDatos('telefono')
				contacto = Contacto.BuscarTelefono(int(datos['telefono']), id)
				if contacto:
					Vista.VerTodos(contacto)
					self.Menu()
				else:
					self.__vistaAgenda.Mensajes('\n---------No se ha encontrado el contacto\n')
					self.Menu()
			else:
				self.Menu()


		elif menu_select == 3:
			lista = Contacto.Todos(id)
			datoAModificar = self.__vistaAgenda.VistaModificar(lista)
			contacto = lista[datoAModificar[0] - 1]
			contacto = {'dni': contacto[0], 'nombre':contacto[2], 'telefono':contacto[3], 'email':contacto[4]}


			if datoAModificar[1] == 1:
				NewDato = self.__vistaAgenda.PedirDatos('nombre')
				Contacto.Modificar(contacto['dni'], NewDato['nombre'], contacto['telefono'])
				self.__vistaAgenda.Mensajes('\n-----------Cambios guardados-----------\n')
				self.Menu()

			elif datoAModificar[1] == 2:
				NewDato = self.__vistaAgenda.PedirDatos('telefono')
				Contacto.Modificar(contacto['dni'], contacto['nombre'], NewDato['telefono'])
				self.__vistaAgenda.Mensajes('\n-----------Cambios guardados-----------\n')
				self.Menu()

			elif datoAModificar[1] == 3:
				NewDato = self.__vistaAgenda.PedirDatos('email')
				Contacto.ModificarEmail(contacto['dni'], NewDato['email'])
				self.__vistaAgenda.Mensajes('\n-----------Cambios guardados-----------\n')
				self.Menu()

		elif menu_select == 4:
			lista = self.__vistaAgenda.VistaEliminar(id)

			Contacto.Delete(lista[0])

			self.__vistaAgenda.Mensajes('\n-------- Se eliminó correctamente--------')
			self.Menu()
		elif menu_select == 5:
			self.__vistaAgenda.Agregar()
			datos = self.__vistaAgenda.PedirDatos('dni','nombre', 'telefono', 'email')
			datos['id_agenda'] = id
			
			NewContacto = Contacto(datos['dni'], datos['id_agenda'], datos['nombre'], datos['telefono'], datos['email'])
			
			NewContacto.save()

			self.__vistaAgenda.Mensajes('----------Se ha guardado con éxito')
			self.Menu()

		elif menu_select == 6:
			self.Home()

			





Controlador()
