from dataBase import *


class Agenda:
	__DB = BaseDatos(name = 'agendaDB')
	__tableName = 'agenda'

	def __init__(self, id, propietario):
		self.__id = id
		self.__propietario = propietario

	def save(self):
		query = "INSERT INTO " +Agenda.__tableName+ "(id_agenda, propietario) VALUES (?,?)"
		values = (self.__id,self.__propietario)
		x = Agenda.__DB.ejecutar(query,values)
		print('guardado')#BORRAR LUEGO

	@classmethod	
	def login(cls, id):
		query = F"SELECT * FROM {Agenda.__tableName} WHERE id_agenda = {id}"
		return Agenda.__DB.ejecutar(query)


	@classmethod
	def Todas(cls):
		query = "SELECT * FROM " + Agenda.__tableName
		return Agenda.__DB.ejecutar(query)

	def __str__(self):
		return f'''Nombre: {self.__propietario}
					ID: {__id}''' #Poner email 





class Contacto:
	__DB = BaseDatos(name = 'agendaDB')
	__tableName = 'contacto'

	def __init__(self, dni, id, nombre, telefono = None, email=None):
		self.__dni = dni
		self.__id = id
		self.__nombre = nombre
		self.__telefono = telefono
		self.__email = email

	def save(self):
		query = "INSERT INTO " +Contacto.__tableName+ "(dni, id_agenda, nombre, telefono, email) VALUES (?,?,?,?,?)"
		values = (self.__dni, self.__id,self.__nombre,self.__telefono,self.__email)
		x = Contacto.__DB.ejecutar(query,values)

	@classmethod
	def Todos(cls):
		query = "SELECT * FROM " + Contacto.__tableName
		return Contacto.__DB.ejecutar(query)


	@classmethod
	def buscar(cls, dni):
		query = F"SELECT * FROM {Contacto.__tableName} WHERE dni = {dni}"
		return Contacto.__DB.ejecutar(query)

	def __str__(self):
		return f'''DNI:{self.__dni}
				   NOMBRE: {self.__nombre}
				   TELEFONO: {self.__telefono}
				   Email: {self.__email}'''



