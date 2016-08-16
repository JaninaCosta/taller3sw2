
from datetime import *

class Tarjeta(object):
    """
    Clase que modela la tarjeta para acceso a edificio y pago de bus
    """
    def __init__(self, nombres=None, apellidos=None, codigo=None, saldo_inicial=0.0):
        """
        Construntor de la clase que recibe parametros para inicializarla
        :param nombres: Nombres de la persona a quien pertenece la tarjeta
        :param apellidos: Apellidos de la persona a quien pertenece la tarjeta
        :param codigo: Codigo de siete digitos numericos para identificar la tarjeta
        :param saldo_inicial: Saldo inicial que contiene la tarjeta
        """
        self.digitos_max = 7
        self.inicio = "00"
        self.nombres = nombres
        self.apellidos = apellidos
        self.codigo = codigo
        self.saldo = saldo_inicial

    def debitar(self, valor=0.0):
        """
        Funcion que debita el valor del pasaje que se pase como parametro
        :param valor: valor del pasaje
        :return:
        """
        self.saldo = self.saldo-valor

class Validador(object):
    """
    Modulo que valida la tarjeta
    """
    @classmethod
    def validar_tarjeta(cls, tarjeta=None):
        """
        Funcion que valida que la tarjeta sea valida o de un tipo estudiante o trabajador
        :param tarjeta: Trajeta que contiene un codigo numerico
        :return: Retirna el tipo de tarjeta o si es invalida
        """
        try:
            if len(tarjeta.codigo) == tarjeta.digitos_max and tarjeta.codigo.isdigit():
                if tarjeta.codigo[:2] == tarjeta.inicio:
                    return "TRABAJADOR"
                else:
                    return "ESTUDIANTE"
            return "INVALIDA"
        except:
            return "INVALIDA"


class Edificio(object):
    """
    Modulo que verifica accesos al edificio
    """
    def conceder_acceso(self, tarjeta=None, dia=0, hora=0):
        """
        Funcion que verifica si el acceso se concedio o no
        :param tarjeta: Tarjeta del usuario a ingresar
        :param dia: dia de la semana en entero lunes=1,martes=2...domingo=7
        :param hora: hora del dia en formato 24, este valor sera solo un entero
        :return: 1 binario si el acceso es concedido, 0 si el acceso es denegado
        """
        if dia > 0 and dia < 8:
            if Validador.validar_tarjeta(tarjeta) == "TRABAJADOR":
                if dia <= 5:
                    return 0b1
                else:
                    if hora >= 10 and hora <= 15:
                        return 0b1
            elif Validador.validar_tarjeta(tarjeta) == "ESTUDIANTE":
                if dia <= 5:
                    if hora >= 8 and hora <= 18:
                        return 0b1
            else:
                return 0b0
        return 0b0


class Bus(object):
    """
    Modulo que verifica el pago del bus
    """
    def __init__(self):
        self.pasaje = 0.30

    def cobrar_pasaje(self, tarjeta=None, dia=0):
        """
        Funcion que verifica que el pasaje haya sido pagado exitosamente
        :param tarjeta: Tarjeta del usuario que paga el pasaje
        :param dia: dia de la senama en el que cobra el pasaje
        :return: 1 en binario si el pasaje es pagado, 0 si este no se pudo cobrar
        """
        if dia > 0 and dia <= 5:
            if Validador.validar_tarjeta(tarjeta) != "INVALIDA":
                if dia == 5:
                    return 0b1
                else:
                    if Validador.validar_tarjeta(tarjeta) == "ESTUDIANTE":
                        if tarjeta.saldo >= self.pasaje:
                            tarjeta.debitar(self.pasaje)
                            return 0b1
                    else:
                        if tarjeta.saldo >= self.pasaje*0.5:
                            tarjeta.debitar(self.pasaje*0.5)
                            return 0b1
        return 0b0


class Libro(object):
    """
    Clase que modela el libro para prestamo en la bibioteca.
    """
    categorias = ["CE", "CN", "CS", "CH"]
    def __init__(self, categoria=None, estado=0):
        """
        Construntor de la clase que recibe parametros para inicializarla
        :param categoria: Categoria del libro
        :param estado: Estado del Libro
        """
        self.categoria = categoria
        self.estado = estado

    def setPrestado(self):
        """
        Funcion que cambia el valor del estado a prestado=1
        :return:
        """
        self.estado = 1
    def setDisponible(self):
        """
        Funcion que cambia el valor del estado a disponible=0
        :return:
        """
        self.estado = 0


class Biblioteca(object):
    """
    Clase que modela la Biblioteca para prestamo de libros.
    """
    @classmethod
    def prestar(cls, libro=None, tarjeta=None, fecha=None):
        if libro.categoria == "CE":
            date1 = datetime.strptime(fecha, "%d/%m/%Y")
            date2 = date1 + timedelta(days=7)
            date = date2.strftime("%d/%m/%Y")
        else:
            date1 = datetime.strptime(fecha, "%d/%m/%Y")
            date2 = date1 + timedelta(days=14)
            date = date2.strftime("%d/%m/%Y")
        return date


t = Tarjeta("Branny", "Chito", "1234567", 0.20)
l = Libro("CE")
l2 = Libro("CN")
# print("validador")
# print(Validador.validar_tarjeta(t))
# bus = Bus()
# print("cobrar luens estudiante")
# print("pasaje")
# print(bus.pasaje)
# print(bus.cobrar_pasaje(t, 1))

print("dia: ")
print(Biblioteca.prestar(l2, t, '01/09/2016'))
