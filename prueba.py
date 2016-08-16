import unittest
#from codigo import Control
#from pasaje import Pasaje
from programa import Bus, Biblioteca


class AddTest(unittest.TestCase):
    def setUp(self):
      #self.codigo = Control()
      #self.pasaje = Pasaje()

      #self.tarjeta = Tarjeta()
      self.codigo2 = Bus()
      self.biblioteca = Biblioteca()
      
      pass
    def tearDown(self):
      pass

    """
    def test_codigoEmpiezaDobleCero(self):
        self.assertEqual(self.codigo.valor_acceso('0012345',1, 1),None)
    def test_codigoNOEmpiezaDobleCero(self):
        self.assertEqual(self.codigo.valor_acceso('1234567',1, 1),None)
    def test_codigoIncorrecto(self):
        self.assertEqual(self.codigo.valor_acceso('12345675',1, 1),None)
    def test_codigoIncorrecto2(self):
        self.assertEqual(self.codigo.valor_acceso('12345',1, 1),None)
    def test_diaTrabajador(self):
        self.assertEqual(self.codigo.valor_acceso('0021234',4, 1),None)
    def test_diaTrabajador2(self):
        self.assertEqual(self.codigo.valor_acceso('0021234',6, 1),None)
    def test_diaEstudiante(self):
        self.assertEqual(self.codigo.valor_acceso('1221234',3, 9),None)
    def test_diaEstudiante2(self):
        self.assertEqual(self.codigo.valor_acceso('1221234',7, 14),None)
    def test_diaEstudiante3(self):
        self.assertEqual(self.codigo.valor_acceso('0021234',6, 14),None)
    def test_cobrarPasajeLunes_Si_saldo(self):
        self.assertEqual(self.pasaje.valor_cobrar(1,0.25,1),1)    
    def test_cobrarPasaje_Martes_NO_Saldo(self):
        self.assertEqual(self.pasaje.valor_cobrar(1,0.25,0),0)
    def test_cobrarPasaje_Viernes(self):
        self.assertEqual(self.pasaje.valor_cobrar(5,0.25,0),1)
    def test_cobrarPasaje_Sabado(self):
        self.assertEqual(self.pasaje.valor_cobrar(6,0.25,0),0)
    """
    def test_cobrar_pasaje_30(self):
        self.assertEqual(self.codigo2.cobrar_pasaje('0012345',1),0b0)
    def test_cobrar_pasaje_30_estudiante(self):
        self.assertEqual(self.codigo2.cobrar_pasaje('1212345',1),0b0)
    def test_cobrar_pasaje_30_dia5(self):
        self.assertEqual(self.codigo2.cobrar_pasaje('1212345',5),0b0)
    def test_cobrar_pasaje_trabajador(self):
        self.assertEqual(self.codigo2.cobrar_pasaje('0023456',2),0b0)
    def test_prestar_libro(self):
        self.assertEqual(self.biblioteca.prestar_libro('CE','1212345',16),None)


if __name__=='__main__':
   unittest.main()