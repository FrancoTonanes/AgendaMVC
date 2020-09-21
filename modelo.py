from dataBase import *


class Agenda:
	__DB = BaseDatos(name = 'AgendaDB2')
	__tableName = 'agenda'

	def __init__(self, id, propietario):
		self.__id = id
		self.__propietario = propietario

	def save(self):
		query = "INSERT INTO " +Agenda.__tableName+ "(id_agenda, propietario) VALUES (?,?)"
		values = (self.__id,self.__propietario)
		x = Agenda.__DB.ejecutar(query,values)


	@classmethod	
	def login(cls, id):
		query = f"SELECT * FROM {Agenda.__tableName} WHERE id_agenda = '{id}'"
		return Agenda.__DB.ejecutar(query)


	@classmethod
	def Todas(cls):
		query = "SELECT * FROM " + Agenda.__tableName
		return Agenda.__DB.ejecutar(query)

	def __str__(self):
		return f'''Nombre: {self.__propietario} --- Email: {self.__id}'''





class Contacto:
	__DB = BaseDatos(name = 'AgendaDB2')
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
	def Todos(cls, id):
		query = f"SELECT * FROM {Contacto.__tableName} WHERE id_agenda = '{id}'"
		return Contacto.__DB.ejecutar(query)


	@classmethod
	def BuscarTelefono(cls, telefono, id):
		query = F"SELECT * FROM {Contacto.__tableName} WHERE telefono = {telefono} and id_agenda = '{id}'"
		return Contacto.__DB.ejecutar(query)
	@classmethod
	def BuscarNombre(cls, nombre, id):
		query = F"SELECT * FROM {Contacto.__tableName} WHERE nombre = '{nombre}' and id_agenda = '{id}'"
		return Contacto.__DB.ejecutar(query)

	@classmethod
	def Modificar(cls, dni, nombre, telefono): 
		query = f"UPDATE {Contacto.__tableName} SET nombre='{nombre}', telefono = {telefono} WHERE dni = {dni}"
		return Contacto.__DB.ejecutar(query)
	@classmethod
	def ModificarEmail(cls, dni, email):
		query = f"UPDATE {Contacto.__tableName} SET email='{email}' WHERE dni = {dni}"
		return Contacto.__DB.ejecutar(query)
	@classmethod
	def Delete(cls, dni):
		query = f"DELETE FROM {Contacto.__tableName} WHERE dni = {dni}"
		return Contacto.__DB.ejecutar(query)

	def __str__(self):
		return f'''DNI:{self.__dni}
				   NOMBRE: {self.__nombre}
				   TELEFONO: {self.__telefono}
				   Email: {self.__email}'''



				   