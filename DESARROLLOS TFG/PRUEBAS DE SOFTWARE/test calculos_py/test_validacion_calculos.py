# Importación de los módulos necesarios para las pruebas
import unittest  # Módulo de Python para realizar pruebas unitarias
from datetime import datetime  # Módulo para manejar fechas
from calculos import validar_numero, validar_texto, validar_fecha  # Importamos las funciones a probar

class TestValidaciones(unittest.TestCase):
    """
    Clase que contiene todas las pruebas unitarias para las funciones de validación.
    Hereda de unittest.TestCase para tener acceso a los métodos de aserción.
    """
    
    def test_validar_numero(self):
        """
        Prueba la función validar_numero con diferentes tipos de entrada.
        Verifica que la función maneje correctamente:
        - Números enteros y decimales
        - Valores negativos
        - Cero
        - Valores vacíos o None
        - Texto no numérico
        """
        # Prueba con números enteros
        self.assertEqual(validar_numero(5), 5.0)  # Verifica que 5 se convierta a 5.0
        self.assertEqual(validar_numero("10"), 10.0)  # Verifica que "10" se convierta a 10.0
        
        # Prueba con números decimales
        self.assertEqual(validar_numero(3.14), 3.14)  # Verifica que mantenga los decimales
        self.assertEqual(validar_numero("2.5"), 2.5)  # Verifica conversión de string decimal
        
        # Prueba con valores negativos
        self.assertEqual(validar_numero(-5), -5.0)  # Verifica manejo de negativos
        self.assertEqual(validar_numero("-3.14"), -3.14)  # Verifica negativos en string
        
        # Prueba con valor 0
        self.assertEqual(validar_numero(0), 0.0)  # Verifica que 0 se convierta a 0.0
        self.assertEqual(validar_numero("0"), 0.0)  # Verifica que "0" se convierta a 0.0
        
        # Prueba con valor None o vacío
        self.assertEqual(validar_numero(None), 0.0)  # Verifica que None devuelva 0.0
        self.assertEqual(validar_numero(""), 0.0)  # Verifica que string vacío devuelva 0.0
        
        # Prueba con texto no numérico
        with self.assertRaises(ValueError):  # Verifica que se lance ValueError con texto no numérico
            validar_numero("abc")
        with self.assertRaises(ValueError):  # Verifica que se lance ValueError con texto mixto
            validar_numero("12abc")

    def test_validar_texto(self):
        """
        Prueba la función validar_texto con diferentes tipos de entrada.
        Verifica que la función maneje correctamente:
        - Texto normal
        - Texto con espacios
        - Texto vacío
        - None
        - Espacios en blanco
        """
        # Prueba con texto normal
        self.assertEqual(validar_texto("Hola"), "Hola")  # Verifica texto sin espacios
        
        # Prueba con texto con espacios
        self.assertEqual(validar_texto("  Hola Mundo  "), "Hola Mundo")  # Verifica eliminación de espacios
        
        # Prueba con texto vacío
        with self.assertRaises(ValueError):  # Verifica que se lance ValueError con texto vacío
            validar_texto("")
        
        # Prueba con None
        with self.assertRaises(ValueError):  # Verifica que se lance ValueError con None
            validar_texto(None)
        
        # Prueba con espacios en blanco
        with self.assertRaises(ValueError):  # Verifica que se lance ValueError con solo espacios
            validar_texto("   ")

    def test_validar_fecha(self):
        """
        Prueba la función validar_fecha con diferentes tipos de entrada.
        Verifica que la función maneje correctamente:
        - Fechas válidas
        - Fechas inválidas
        - Formatos incorrectos
        - Fechas vacías
        - None
        """
        # Prueba con fecha válida
        fecha_valida = "01/01/2024"
        self.assertIsInstance(validar_fecha(fecha_valida), datetime)  # Verifica que devuelva un objeto datetime
        self.assertEqual(validar_fecha(fecha_valida).strftime("%d/%m/%Y"), fecha_valida)  # Verifica formato correcto
        
        # Prueba con fecha inválida
        with self.assertRaises(ValueError):  # Verifica que se lance ValueError con día inválido
            validar_fecha("32/01/2024")
        with self.assertRaises(ValueError):  # Verifica que se lance ValueError con mes inválido
            validar_fecha("01/13/2024")
        
        # Prueba con formato incorrecto
        with self.assertRaises(ValueError):  # Verifica que se lance ValueError con formato incorrecto
            validar_fecha("2024-01-01")
        with self.assertRaises(ValueError):  # Verifica que se lance ValueError con formato incorrecto
            validar_fecha("01-01-2024")
        
        # Prueba con fecha vacía
        with self.assertRaises(ValueError):  # Verifica que se lance ValueError con fecha vacía
            validar_fecha("")
        
        # Prueba con None
        with self.assertRaises(ValueError):  # Verifica que se lance ValueError con None
            validar_fecha(None)

# Bloque que permite ejecutar las pruebas directamente desde este archivo
if __name__ == '__main__':
    unittest.main() 