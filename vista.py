from modelo import *

class Vista:
	def __init__(self):
		self.op1 = 'Ver todos los contactos'
		self.op2 = 'Buscar contacto'
		self.op3 = 'Modificar'
		self.op4 = 'Elimnar'
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
		print("--------------Ingreso----------------")
		id = int(input('Ingrese su clave:\t'))#MODIFICAR POR EMAIL
		return id

	def VerTodos(self):
		contactos = Contacto.Todos()
		contador = 0
		for i in contactos:
			print('\n--------')
			print('DNI:',i[0])
			print('Clave:',i[1])
			print('NOMBRE:',i[2])