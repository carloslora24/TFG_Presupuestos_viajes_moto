# Archivo de prueba global para el cálculo del total general del viaje en calculos.py
import unittest
from calculos import procesar_presupuestovm

class TestCalculosViaje(unittest.TestCase):
    """
    Prueba unitaria global para validar que el cálculo del total general del viaje es correcto.
    Esta prueba comprueba de forma implícita todos los cálculos intermedios (categorías, combustible, equipamiento, mantenimiento y otros gastos),
    ya que el total general es la suma de todos estos conceptos.
    """

    def setUp(self):
        # Este método se ejecuta antes de la prueba. Define los datos de ejemplo que se usarán en la comprobación global.
        
        self.datos_viaje = {
            "nombre_viaje": "Viaje Test",
            "destino_principal": "Destino X",
            "precio_combustible": 1.6,
            "consumo_medio_moto": 5.0,
            "pasajero": True
        }
        self.etapas = [
            {
                "origen_etapa": "Ciudad A",
                "destino_etapa": "Ciudad B",
                "kms_etapa": 100,
                "fecha": "01/08/2025",
                "velocidad_media_etapa": 70,
                "alojamiento_etapa": 120.0,
                "alimentacion_etapa": {"desayuno": 5.0, "comida": 40.0, "cena": 35.50},
                "aparcamiento_etapa": 8.50,
                "peaje_etapa": 10.0,
                "actividad_etapa": 15.0,
                "transporte_etapa": 1.0,
                "extra_etapa": 1.0
            },
            {
                "origen_etapa": "Ciudad B",
                "destino_etapa": "Ciudad C",
                "kms_etapa": 200,
                "fecha": "02/08/2025",
                "velocidad_media_etapa": 100,
                "alojamiento_etapa": 40.0,
                "alimentacion_etapa": {"desayuno": 6.0, "comida": 12.0, "cena": 9.0},
                "aparcamiento_etapa": 3.0,
                "peaje_etapa": 4.0,
                "actividad_etapa": 5.0,
                "transporte_etapa": 2.0,
                "extra_etapa": 2.0
            }
        ]
        self.otros_gastos = {
            "gastos_compras": 20.0,
            "gastos_acampada": 5.0,
            "otras_tasas": {"tasa1": 5.0},
            "gastos_seguros": {"seguro1": 10.0}
        }
        self.equip_moteros = {
            "casco": 50.0,
            "guantes_invierno": 10.0,
            "guantes_verano": 0.0,
            "botas_invierno": 0.0,
            "botas_verano": 0.0,
            "chaqueta_invierno": 0.0,
            "chaqueta_verano": 0.0,
            "pantalon_invierno": 0.0,
            "pantalon_verano": 0.0,
            "ropa_termica": 0.0,
            "traje_agua": 0.0,
            "airbag": 0.0,
            "protecciones_adicionales": 0.0,
            "kit_primeros_auxilios": 0.0,
            "intercomunicadores": 0.0,
            "equipacion_otros": 0.0
        }
        self.equip_moto = {
            "equipacion_navegador": 0.0,
            "equipacion_equipaje": 0.0,
            "equipacion_funda": 0.0,
            "equipacion_extintor": 0.0,
            "equipacion_otros": 0.0
        }
        self.mantenimiento = {
            "mto_pinchazos": 0.0,
            "mto_herramientas": 0.0,
            "mto_compresor": 0.0,
            "mto_arrancador": 0.0,
            "mto_rev_previa": 0.0,
            "mto_talleres": 0.0,
            "mto_neumaticos": 0.0,
            "mto_frenos": 0.0,
            "mto_transmision": 0.0,
            "mto_otros": 0.0,
            "mto_rev_post": 20.0
        }

    def test_total_general_viaje(self):
        """
        Comprueba que el cálculo del total general del viaje (suma de todos los conceptos y combustible) es correcto.
        Si esta prueba pasa, se valida implícitamente que todos los cálculos intermedios son correctos.
        """
        datos = {
            "datos_viaje": self.datos_viaje.copy(),
            "etapas": self.etapas.copy(),
            "otros_gastos": self.otros_gastos.copy(),
            "equipamiento_moteros": self.equip_moteros.copy(),
            "equipamiento_moto": self.equip_moto.copy(),
            "mantenimiento": self.mantenimiento.copy()
        }
        resultado = procesar_presupuestovm(datos, formato_respuesta="resumen")
        # Cálculo manual del total esperado con los nuevos importes
        total_alojamiento = 120.0 + 40.0
        total_alimentacion = (5.0 + 40.0 + 35.50) + (6.0 + 12.0 + 9.0)
        total_aparcamiento = 8.50 + 3.0
        total_peaje = 10.0 + 4.0
        total_actividad = 15.0 + 5.0
        total_transporte = 1.0 + 2.0
        total_extra = 1.0 + 2.0
        total_equip_moteros = 50.0 + 10.0
        total_equip_moto = 0.0
        total_mantenimiento = 20.0
        total_compras = 20.0
        total_acampada = 5.0
        total_tasas = 5.0
        total_seguros = 10.0
        total_otros_gastos = total_compras + total_acampada + total_tasas + total_seguros
        total_gastos = (
            total_alojamiento + total_alimentacion + total_aparcamiento + total_peaje +
            total_actividad + total_transporte + total_extra + total_equip_moteros +
            total_equip_moto + total_mantenimiento + total_otros_gastos
        )
        # Combustible
        total_kms = 100 + 200
        litros = round((total_kms * 5.0) / 100, 2)
        total_combustible = round(litros * 1.6, 2)
        total_general_esperado = round(total_gastos + total_combustible, 2)
        self.assertAlmostEqual(resultado["resumen_gastos"]["total_general"], total_general_esperado)

# Permite ejecutar la prueba desde la terminal con: python -m unittest test_gestion_calculos.py
if __name__ == "__main__":
    unittest.main() 