from modelo import *

class Vista:
	def __init__(self):
		self.op1 = 'Ver todos los contactos'
		self.op2 = 'Buscar contacto'
		self.op3 = 'Modificar'
		self.op4 = 'Eliminar'
		self.op5 = 'Agregar'
		self.op6 = 'Salir'
		self.op7 = 'Crear agenda'
		self.op8 = 'Ya tengo una agenda'


	def Inicio(self):
		print("--------------BIENVENIDO----------------")
		print(f'1--{self.op7}')
		print(f'2--{self.op8}')
		return int(input('\nIngrese opción:\t'))


	def Mostrame(self):
		print("--------------MENU----------------")
		print(f'1--{self.op1}')
		print(f'2--{self.op2}')
		print(f'3--{self.op3}')
		print(f'4--{self.op4}')
		print(f'5--{self.op5}')
		print(f'6--{self.op6}')
		return int(input('Ingrese opción:\t'))


	def CrearAgenda(Self):
		print("--------------Crear Agenda----------------")
		propietario = input('Ingrese su nombre:\t')
		id = int(input('Ingrese su clave:\t'))#MODIFICAR POR EMAIL
		return (id, propietario)
	def LoginAgenda(self):
		print("--------------Inicie Sesión----------------")
		id = int(input('Ingrese su clave:\t'))#MODIFICAR POR EMAIL
		return id
	@classmethod
	def VerTodos(cls, tuppla): #MODIFICAR A LA NUEVA VERSIÓN
		contador = 1
		for i in tuppla:
			print(f'\n------ ID: {contador} ------')
			print('Numero de DNI:', i[0])
			print('Nombre:', i[2])
			print('Telefono:', i[3])
			print('Email:', i[4])
			contador += 1

	def VistaModificar(self, tupla):
		print('============= Selccione el contacto a modificar ==============')
		Vista.VerTodos(tupla)
		op = int(input('\nIngrese el id contacto que desea modificar:\t'))
		
		print('====== Seleccione los datos a modificar ======\n')
		print('1 - Nombre')
		print('2 - Telefono')
		print('3 - Email')
		op2 = int(input('\n Ingrese la opción:\t'))
	
		return(op, op2)


	def VistaBuscar(self):
		print('=========== BUSCAR CONTACTO ==========')
		print('1 - Buscar por nombre')
		print('2 - Buscar por telefono')

		print('\n0 - Para salir...\n')
		
		return int(input(''))


	def PedirDatos(self,*args):
		print("")
		salida = dict()
		for r in args:
			salida[r] = input(f"Ingrese {r}: ")
		return salida

	def VistaEliminar(self, id):
		print('\n======= ELIMINAR =======\n')
		lista = Contacto.Todos(id)
		Vista.VerTodos(lista)
		op = int(input('\nIngrese el ID del contacto a eliminar:\t'))
		return lista[op - 1]

	def Agregar(self):
		print('\n========== AGREGAR ==========\n')



	def Mensajes(self, sms):
		print(sms)