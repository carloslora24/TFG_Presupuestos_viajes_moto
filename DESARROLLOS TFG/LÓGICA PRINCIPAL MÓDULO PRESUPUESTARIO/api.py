# Importaciones necesarias para la API
# FastAPI: Framework para crear la API
# Query: Para definir parámetros de consulta en la URL
# Body: Para definir el cuerpo de la petición POST
# procesar_presupuestovm: Función principal de cálculos
# Enum: Para crear enumeraciones de valores permitidos
from fastapi import FastAPI, Query, Body
from calculos import procesar_presupuestovm
from enum import Enum

# Inicialización de la aplicación FastAPI
# Crea una instancia de la aplicación y configura el servidor web
app = FastAPI()

# Enumeración de formatos de respuesta permitidos
# Define una clase que hereda de str y Enum
# Restringe los valores posibles para el formato de respuesta
# Cada valor es una cadena de texto válida
class FormatoRespuesta(str, Enum):
    etiqueta = "etiqueta"  # Formato básico con información mínima
    resumen = "resumen"    # Formato intermedio con totales
    completo = "completo"  # Formato detallado con toda la información

# Endpoint de Health Check
# Decorador que define un endpoint GET en la ruta /health
# Función asíncrona que verifica el estado de la API
# Retorna un diccionario con el estado de la API
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Endpoint Principal para procesar presupuestos
# Decorador que define un endpoint POST en la ruta /presupuestovm
# Función asíncrona que procesa los datos del presupuesto
# Parámetros:
#   - datos_presupuesto: Diccionario con todos los datos del viaje (requerido en el cuerpo)
#   - formato: Parámetro opcional en la URL, con valor por defecto "completo"
@app.post("/presupuestovm")
async def crear_presupuesto_completo(
    datos_presupuesto: dict = Body(...),  # Parámetro requerido en el cuerpo de la petición
    formato: FormatoRespuesta = Query(FormatoRespuesta.completo, description="Formato de respuesta deseado")  # Parámetro opcional con valor por defecto
):
    """
    Procesa todos los datos del presupuesto del viaje en moto.
    
    Args:
        datos_presupuesto (dict): Diccionario con todos los datos del viaje:
            - datos_viaje: dict con información general del viaje
            - etapas: list de dict con datos de cada etapa
            - otros_gastos: dict con gastos varios
            - equipamiento_moteros: dict con equipamiento de moteros
            - equipamiento_moto: dict con equipamiento de moto
            - mantenimiento: dict con gastos de mantenimiento
        
        formato (str): Formato de respuesta deseado:
            - etiqueta: Datos básicos del viaje
            - resumen: Información general y totales
            - completo: Todos los detalles del viaje
    
    Returns:
        dict: Diccionario con el presupuesto procesado en el formato solicitado
    """
    # Manejo de errores con try/except
    # Intenta procesar los datos y devuelve el resultado
    # Si hay un error, captura la excepción y devuelve un mensaje de error
    try:
        # Procesa los datos usando la función principal de cálculos
        presupuesto_procesado = procesar_presupuestovm(datos_presupuesto, formato)
        # Retorna un diccionario con estado de éxito y los datos procesados
        return {"status": "success", "data": presupuesto_procesado}
    except Exception as e:
        # Retorna un diccionario con estado de error y el mensaje de la excepción
        return {"status": "error", "data": str(e)}  