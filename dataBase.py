import pyodbc

class BaseDatos:
	
	def __init__(self, name,server = 'localhost\SQLEXPRESS',
				driver="SQL Server Native Client 11.0"):
		self.__name = name
		self.__server = server
		self.__driver = driver
		self.__conexion = None
		self.__datos = None


	def conectar(self):
		self.__conexion = pyodbc.connect("DRIVER={"+self.__driver+"};"
                                  "Server="+self.__server+";"
                                  "DATABASE="+self.__name+";"
                                  "Trusted_Connection=yes;")

hola = BaseDatos('agendaDB')
try:
	hola.conectar()
	print('Se conectó')

except Exception as e:
	print('No se pudo conectar')

