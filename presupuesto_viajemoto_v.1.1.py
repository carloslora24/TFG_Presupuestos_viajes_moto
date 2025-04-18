###############################################
###   PRESUPUESTOS DE VIAJES EN MOTO v.1.1  ###
###############################################
"""
# Autor: Carlos Lora Espinosa
# Fecha: 18/04/2025
# Novedades de la versión: Se incluyen las funciones de validación de números, texto, fechas y respuestas (s/n) 
# para dar más robustez a la hora de introducir los datos. También se incluye la función mostrar_menu().
"""
# Importar módulos necesarios
from datetime import datetime

# Función para validar entrada de números en formato válido.
def validar_numero(mensaje):
     while True:
        entrada = input(mensaje)
        if not entrada:  # Si la entrada está vacía, devuelve 0.
            return 0.0
        try:
            return float(entrada) # Si no, muestra el mensaje de error hasta que se introducza un número válido.
        except ValueError:
            print("Error: Debes introducir un número válido")

# Función para validar entrada de texto.
def validar_texto(mensaje):
    while True:
        entrada = input(mensaje).strip()  # Entrada del texto. Elimina los espacios en blanco al principio y al final de la cadena de texto.
        if entrada:
            return entrada      # Si el texto es válido, lo devuelve como salida.
        print("Error: Debes introducir un texto válido")  # Si no es correcto muestra el mensaje de error y solicita un texto válido.

# Función para validar fecha
def validar_fecha(mensaje):
    while True:
        fecha = input(mensaje) 
        try:
            datetime.strptime(fecha, "%d/%m/%Y")        # Si la fecha tiene el formato correcto, la devuelve como salida.
            return fecha
        except ValueError:
            print("Formato de fecha incorrecto. Usa el formato DD/MM/AAAA")     # Si no, muestra el mensaje de error y solicita nueva fecha indicando el formato correcto.

# Función para validar respuesta sí/no
def validar_si_no(mensaje):
    while True:
        respuesta = input(mensaje).lower()      # Entrada de la respuesta. Se pasa a minúscula para procesarla.
        if respuesta in ['s', 'n']:             # Si la respuesta es "s" o "n" entonces la devuelve como salida.
            return respuesta == 's'            
        print("Por favor, responde con 's' o 'n'")  # Si no, muestra el mensaje solicitando una respuesta válida.

# Función para mostrar un menú y obtener una opción válida
def mostrar_menu(titulo, opciones):
    print(f"\n##### {titulo} #####")            # Muestra el título del menú 
    print("-" * 60)
    for i, opcion in enumerate(opciones, 1):    # Muestra las opciones del menú
        print(f"{i}. {opcion}")
    while True:                                 
        try:
            eleccion = int(input("\nSelecciona una opción: "))
            if 1 <= eleccion <= len(opciones):
                return eleccion                 # Si la opción introducida está dentro del rango válido, la devuelve como salida.
            print(f"Opción no válida. Debe ser un número entre 1 y {len(opciones)}")    # Si no, muestra un mensaje con el rango de opciones válido.
        except ValueError:
            print("Error: Debes introducir un número válido")   # Si el valor introducido sigue siendo incorrecto muestra el mensaje de error.

# Función para crear una etapa del viaje
def crear_etapa():
    print("\nDatos de la etapa:")
    
    etapa = {
        'origen_etapa': validar_texto("Origen de la etapa: "),
        'destino_etapa': validar_texto("Destino de la etapa: "),
        'kms_etapa': validar_numero("Kilómetros de la etapa: "),
        'fecha': validar_fecha("Fecha prevista de la etapa (DD/MM/AAAA): "),
        'velocidad_media_etapa': validar_numero("Velocidad media estimada de la etapa (km/h): "),
        'alojamiento_etapa': validar_numero("Coste alojamiento: "),
        'alimentación_etapa': { 
            'alimentacion_desayuno': validar_numero("Coste desayuno: "),
            'alimentacion_almuerzo': validar_numero("Coste almuerzo: "),
            'alimentacion_comida': validar_numero("Coste comida: "),
            'alimentacion_merienda': validar_numero("Coste merienda: "),
            'alimentacion_cena': validar_numero("Coste cena: "),
            'alimentacion_otros': validar_numero("Algún otro gasto más en alimentación o bebida? ")
        },
        'aparcamiento_etapa': validar_numero("Gasto en aparcamiento: "),
        'peaje_etapa': validar_numero("Gasto en peajes: "),
        'actividad_etapa': validar_numero("Previsión de gastos en actividades culturales y de ocio: "),
        'transporte_etapa': validar_numero("Gastos de transporte como transporte público o transporte para la moto: "),
        'extra_etapa': validar_numero("Previsión de gastos extra: ")
    }
    return etapa

# Función para obtener otros gastos relacionados con el viaje
def otros_gastos():
    print("Indica otros costes relacionados con el viaje.")
    return{
        'gastos_compras': validar_numero("Indica la previsión de gastos en compras como regalos o souvenirs: "),
        'gastos_acampada': validar_numero("¿Tienes pensado acampar?. Indica el coste previsto para el equipo de acampada: "),
        'otras_tasas': {
            'tasas_visados': validar_numero("Indica el coste de los visados necesarios según los países que visites: "),
            'tasas_pases': validar_numero("Indica el coste de los pases o permisos de circulación por carreteras y autovías que necesites en cada país: "),
            'tasas_otros': validar_numero("Indica los costes de otras tasas o impuestos que puedas necesitar en el viaje: ")
        },
        'gastos_seguros': {
            'seguro_moto': validar_numero("¿Necesitas alguna cobertura adicional?. Indica los costes del seguro de la moto si necesitas contratar alguna cobertura adicional: "),
            'seguro_viaje': validar_numero("¿Vas a contratar un seguro de viaje?. Introduce su precio en caso afirmativo: "),
            'seguro_salud': validar_numero("¿Vas a viajar al extranjero?. Quizás vendría bien contratar un seguro de salud: "),
            'seguro_otros': validar_numero("¿Necesitas algún otro seguro?. Indica el coste previsto: ")
        }
    }

# Función para obtener los costes de equipación para piloto y pasajero
def equipar_moteros():
    print("Indica los costes de la equipación que necesites adquirir para el piloto y/o pasajero. Si no lo necesitas indica un 0.")
    return{
        'equipo_casco': validar_numero("¿Casco?: "),
        'equipo_guantes_inv': validar_numero("¿Guantes de invierno?: "),
        'equipo_guantes_ver': validar_numero("¿Guantes de verano?: "),
        'equipo_botas_inv': validar_numero("¿Botas de invierno?: "),
        'equipo_botas_ver': validar_numero("¿Botas de verano?: "),
        'equipo_chaqueta_inv': validar_numero("¿Chaqueta de invierno?: "),
        'equipo_chaqueta_ver': validar_numero("¿Chaqueta de verano?: "),
        'equipo_pantalon_inv': validar_numero("¿Pantalón de invierno?: "),
        'equipo_pantalon_ver': validar_numero("¿Pantalón de verano?: "),
        'equipo_ropa_termica': validar_numero("¿Ropa térmica?: "),
        'equipo_traje_agua': validar_numero("¿Traje de agua?: "),
        'equipo_airbag': validar_numero("¿Chaleco o chaqueta airbag?: "),
        'equipo_protecciones': validar_numero("¿Protecciones adicionales?: "),
        'equipo_auxilio': validar_numero("¿Kit de primeros auxilios?: "),
        'equipo_intercom': validar_numero("¿Intercomunicadores o manos libres?: "),
        'equipo_otros': validar_numero("¿Algún otro elemento de equipación para el piloto o el pasajero?: ")
    }

# Función para obtener los costes de equipación para la moto
def equipar_moto():
    print("Indica los costes del equipamiento necesario para tu moto.")
    return{
        'equipacion_navegador': validar_numero("Navegador o dispositivo de navegación GPS y soportes: "),
        'equipacion_equipaje': validar_numero("¿Necesitas maletas, bolsas o soportes para tu equipaje?. Indica los costes previstos: "),
        'equipacion_funda': validar_numero("Si quieres proteger tu moto y te queda sitio en la maleta puedes contar con una funda: "),
        'equipacion_extintor': validar_numero("Extintor. Nunca se sabe: ")
    }

# Función para obtener los costes de mantenimiento
def mantenimiento():
    print("Indica el coste previsto para el mantenimiento necesario de la moto relacionado con el viaje.")
    return{
        'mto_pinchazos': validar_numero("Kit de reparación de pinchazos: "),
        'mto_herramientas': validar_numero("Herramientas: "),
        'mto_compresor': validar_numero("Compresor de aire portátil: "),
        'mto_arrancador': validar_numero("Arrancador de batería portátil: "),
        'mto_rev_previa': validar_numero("Revisión previa al viaje: "),
        'mto_talleres': validar_numero("Otros costes de mano de obra de mecánico: "),
        'mto_neumaticos': validar_numero("¿Necesitas un cambio de ruedas?. Indica su coste: "),
        'mto_frenos': validar_numero("¿Cómo llevas las pastillas de freno?. Incluye su precio: "),
        'mto_transmision': validar_numero("Indica el coste del mantenimiento de la transmisión. Quizás necesite un ajuste de cadena y un buen engrasado: "),
        'mto_otros': validar_numero("Indica cualquier otro coste asociado con el mantenimiento de la moto de cara al viaje: "),
        'mto_rev_post': validar_numero("Coste revisión posterior al viaje: ")
    }

# Función para calcular el gasto en combustible
def calcular_gasto_combustible(kilometros, consumo_medio, precio_combustible):
    litros = (kilometros * consumo_medio) / 100
    costo = litros * precio_combustible
    return litros, costo

# Función para calcular el tiempo de desplazamiento
def calcular_tiempo_desplazamiento(kilometros, velocidad):
    if velocidad == 0:
        return "0h 0m"
    horas = kilometros / velocidad
    horas_enteras = int(horas)
    minutos = int((horas - horas_enteras) * 60)
    return f"{horas_enteras}h {minutos}m"

# Función para mostrar la etiqueta del viaje
def mostrar_etiqueta_viaje(nombre_viaje, destino_principal, etapas, pasajero, total_viaje):
    print("\n##### ETIQUETA DEL VIAJE #####")
    print("-" * 60)
    print(f"Nombre del viaje: {nombre_viaje}")
    print(f"Destino principal del viaje: {destino_principal}")
    total_kilometros = sum(etapa['kms_etapa'] for etapa in etapas)
    print(f"Kilómetros totales: {total_kilometros:.2f}km")
    print(f"Número de etapas: {len(etapas)}")
    print(f"Presupuesto total del viaje: {total_viaje:.2f}€")
    if pasajero:
        print(f"Presupuesto por persona: {total_viaje/2:.2f}€")
    print(f"Pasajero: {'Sí' if pasajero else 'No'}")
    input("\nPresiona Enter para continuar...")

# Función para mostrar el resumen del viaje
def mostrar_resumen(nombre_viaje, destino_principal, etapas, pasajero, precio_combustible, consumo_medio, gastos_varios, equipo_moteros, equipo_moto, mto):
    print("\n##### RESUMEN DEL VIAJE #####")
    print("-" *60)
    
    # Cálculo de estadísticas del viaje
    total_kilometros = sum(etapa['kms_etapa'] for etapa in etapas)
    kms_medio_etapa = total_kilometros / len(etapas) if etapas else 0
    velocidad_media = sum(etapa['velocidad_media_etapa'] for etapa in etapas) / len(etapas) if etapas else 0
    total_litros = sum(calcular_gasto_combustible(etapa['kms_etapa'], consumo_medio, precio_combustible)[0] for etapa in etapas)
    tiempo_total = sum(etapa['kms_etapa'] / etapa['velocidad_media_etapa'] for etapa in etapas) if etapas else 0
    horas_total = int(tiempo_total)
    minutos_total = int((tiempo_total - horas_total) * 60)

    # Mostrar información general del viaje
    print(f"Nombre del viaje: {nombre_viaje}")
    print(f"Destino principal del viaje: {destino_principal}")
    print(f"Kilómetros totales: {total_kilometros:.2f} km")
    print(f"Kilómetros de media por etapa: {kms_medio_etapa:.2f} km")
    print(f"Número de etapas: {len(etapas)}")
    print(f"Pasajero: {'Sí' if pasajero else 'No'}")
    if etapas:
        print(f"Fecha de inicio del viaje: {etapas[0]['fecha']}")
        print(f"Fecha de fin del viaje: {etapas[-1]['fecha']}")
    print(f"Precio medio del combustible: {precio_combustible}€/L")
    print(f"Consumo medio de la moto: {consumo_medio} L/100kms")
    print(f"Total litros de combustible: {total_litros:.2f} L")
    print(f"Velocidad media: {velocidad_media:.2f} kms/h")
    print(f"Tiempo total de desplazamiento: {horas_total}h {minutos_total}m")
    
    # Cálculo y presentación de gastos
    print("\nResumen de gastos:")
    total_combustible = sum(calcular_gasto_combustible(etapa['kms_etapa'], consumo_medio, precio_combustible)[1] for etapa in etapas)
    total_alojamiento = sum(etapa['alojamiento_etapa'] for etapa in etapas)
    total_alimentacion = sum(sum(etapa['alimentación_etapa'].values()) for etapa in etapas)
    total_aparcamiento = sum(etapa['aparcamiento_etapa'] for etapa in etapas)
    total_peaje = sum(etapa['peaje_etapa'] for etapa in etapas)
    total_actividades = sum(etapa['actividad_etapa'] for etapa in etapas)
    total_transporte = sum(etapa['transporte_etapa'] for etapa in etapas)
    total_extra = sum(etapa['extra_etapa'] for etapa in etapas)

    print(f"Combustible: {total_combustible:.2f}€")
    print(f"Alojamiento: {total_alojamiento:.2f}€")
    print(f"Alimentación: {total_alimentacion:.2f}€")
    print(f"Aparcamiento: {total_aparcamiento:.2f}€")
    print(f"Peajes: {total_peaje:.2f}€")
    print(f"Actividades culturales y de ocio: {total_actividades:.2f}€")
    print(f"Transporte: {total_transporte:.2f}€")
    print(f"Gastos Extra: {total_extra:.2f}€")

    print(f"Compras y souvenirs: {gastos_varios['gastos_compras']:.2f}€")
    print(f"Gastos de Acampada: {gastos_varios['gastos_acampada']:.2f}€")
    print(f"Tasas: {sum(gastos_varios['otras_tasas'].values()):.2f}€")
    print(f"Seguros: {sum(gastos_varios['gastos_seguros'].values()):.2f}€")
    print(f"Equipación piloto y/o pasajero: {sum(equipo_moteros.values()):.2f}€")
    print(f"Equipación moto: {sum(equipo_moto.values()):.2f}€")
    print(f"Mantenimiento: {sum(mto.values()):.2f}€")
    
    # Cálculo del total del viaje
    total_viaje = (total_combustible + total_alojamiento + total_alimentacion + total_aparcamiento + total_peaje + total_actividades + total_transporte + 
                   total_extra + gastos_varios['gastos_compras'] + gastos_varios['gastos_acampada'] + sum(gastos_varios['otras_tasas'].values()) + 
                   sum(gastos_varios['gastos_seguros'].values()) + sum(equipo_moteros.values()) + 
                   sum(equipo_moto.values()) + sum(mto.values()))
    
    print(f"\nTOTAL VIAJE: {total_viaje:.2f}€")
    if pasajero:
        print(f"TOTAL POR PERSONA: {total_viaje/2:.2f}€")

    input("\nPresiona Enter para continuar...")
    return total_viaje

# Función para mostrar el presupuesto detallado
def mostrar_detalle(nombre_viaje, destino_principal, etapas, pasajero, precio_combustible, consumo_medio, gastos_varios, equipo_moteros, equipo_moto, mto):
    print("\n##### PRESUPUESTO DETALLADO #####")
    print("-" * 60)

    # Información general del viaje
    print("Información del Viaje:")
    total_kilometros = sum(etapa['kms_etapa'] for etapa in etapas)
    kms_medio_etapa = total_kilometros / len(etapas) if etapas else 0
    velocidad_media = sum(etapa['velocidad_media_etapa'] for etapa in etapas) / len(etapas) if etapas else 0
    total_litros = sum(calcular_gasto_combustible(etapa['kms_etapa'], consumo_medio, precio_combustible)[0] for etapa in etapas)
    tiempo_total = sum(etapa['kms_etapa'] / etapa['velocidad_media_etapa'] for etapa in etapas) if etapas else 0
    horas_total = int(tiempo_total)
    minutos_total = int((tiempo_total - horas_total) * 60)

    print(f"Nombre del viaje: {nombre_viaje}")
    print(f"Destino principal del viaje: {destino_principal}")
    print(f"Kilómetros totales: {total_kilometros:.2f}kms")
    if etapas:
        print(f"Fecha de inicio del viaje: {etapas[0]['fecha']}")
        print(f"Fecha de fin del viaje: {etapas[-1]['fecha']}")
    print(f"Precio medio del combustible: {precio_combustible}€/L")
    print(f"Consumo medio de la moto: {consumo_medio} L/100km")
    print(f"Total litros de combustible: {total_litros:.2f} L")
    print(f"Velocidad media: {velocidad_media:.2f} km/h")
    print(f"Tiempo total de desplazamiento: {horas_total}h {minutos_total}m")

    # Desglose por etapas
    print("\nPresupuesto detallado:")
    print("Detalle por etapas:")

    for i, etapa in enumerate(etapas, 1):
        print(f"\nInformación Etapa {i}:")
        print(f"Origen: {etapa['origen_etapa']}")
        print(f"Destino: {etapa['destino_etapa']}")
        print(f"Kilómetros: {etapa['kms_etapa']}")
        print(f"Fecha de la etapa: {etapa['fecha']}")
        print(f"Velocidad media de la etapa: {etapa['velocidad_media_etapa']}")
        print(f"Tiempo de desplazamiento: {calcular_tiempo_desplazamiento(etapa['kms_etapa'], etapa['velocidad_media_etapa'])}")

        # Cálculo de costos por etapa
        litros_etapa, costo_combustible = calcular_gasto_combustible(etapa['kms_etapa'], consumo_medio, precio_combustible)
        total_etapa = (costo_combustible + etapa['alojamiento_etapa'] + 
                      sum(etapa['alimentación_etapa'].values()) + 
                      etapa['aparcamiento_etapa'] + etapa['peaje_etapa'] + 
                      etapa['actividad_etapa'] + etapa['transporte_etapa'] + 
                      etapa['extra_etapa'])
        
        print(f"\nPresupuesto Etapa {i}: {total_etapa:.2f}€")
        print(f"Combustible: {costo_combustible:.2f}€ ({litros_etapa:.2f} L)")
        print(f"Alojamiento: {etapa['alojamiento_etapa']:.2f}€")
        total_alimentacion_etapa = sum(etapa['alimentación_etapa'].values())
        print(f"Alimentación: {total_alimentacion_etapa:.2f}€")
        print("  Desglose alimentación:")
        for comida, costo in etapa['alimentación_etapa'].items():
            if costo > 0:
                print(f"    {comida.replace('_', ' ').title()}: {costo:.2f}€")
        print(f"Aparcamiento: {etapa['aparcamiento_etapa']:.2f}€")
        print(f"Peaje: {etapa['peaje_etapa']:.2f}€")
        print(f"Actividades y ocio: {etapa['actividad_etapa']:.2f}€")
        print(f"Transporte: {etapa['transporte_etapa']:.2f}€")
        print(f"Gastos Extra: {etapa['extra_etapa']:.2f}€")
    
    # Desglose de otros gastos
    print("\nDetalle de los demás gastos del viaje:")
    print(f"Compras y souvenirs: {gastos_varios['gastos_compras']:.2f}€")
    print(f"Gastos de Acampada: {gastos_varios['gastos_acampada']:.2f}€")
    
    print("\nTasas:")
    for tasa, costo in gastos_varios['otras_tasas'].items():
        if costo > 0:
            print(f"  {tasa.replace('_', ' ').title()}: {costo:.2f}€")
    
    print("\nSeguros:")
    for seguro, costo in gastos_varios['gastos_seguros'].items():
        if costo > 0:
            print(f"  {seguro.replace('_', ' ').title()}: {costo:.2f}€")
    
    print("\nEquipación piloto y/o pasajero:")
    for item, costo in equipo_moteros.items():
        if costo > 0:
            print(f"  {item.replace('_', ' ').title()}: {costo:.2f}€")
    
    print("\nEquipación moto:")
    for item, costo in equipo_moto.items():
        if costo > 0:
            print(f"  {item.replace('_', ' ').title()}: {costo:.2f}€")
    
    print("\nMantenimiento:")
    for item, costo in mto.items():
        if costo > 0:
            print(f"  {item.replace('_', ' ').title()}: {costo:.2f}€")

    # Cálculo del total del viaje
    total_viaje = (sum(calcular_gasto_combustible(etapa['kms_etapa'], consumo_medio, precio_combustible)[1] for etapa in etapas) +
                sum(etapa['alojamiento_etapa'] for etapa in etapas) +
                sum(sum(etapa['alimentación_etapa'].values()) for etapa in etapas) +
                sum(etapa['aparcamiento_etapa'] for etapa in etapas) +
                sum(etapa['peaje_etapa'] for etapa in etapas) +
                sum(etapa['actividad_etapa'] for etapa in etapas) +
                sum(etapa['transporte_etapa'] for etapa in etapas) +
                sum(etapa['extra_etapa'] for etapa in etapas) +
                gastos_varios['gastos_compras'] +
                gastos_varios['gastos_acampada'] +
                sum(gastos_varios['otras_tasas'].values()) +
                sum(gastos_varios['gastos_seguros'].values()) +
                sum(equipo_moteros.values()) +
                sum(equipo_moto.values()) +
                sum(mto.values()))
    
    print(f"\nTOTAL VIAJE: {total_viaje:.2f}€")
    if pasajero:
        print(f"TOTAL POR PERSONA: {total_viaje/2:.2f}€")
    
    input("\nPresiona Enter para continuar...")

# Función principal del programa
def main():
    print("##### CALCULADORA DE PRESUPUESTOS DE VIAJES EN MOTO #####")

    # Solicitar datos generales del viaje
    print("\n### DATOS GENERALES DEL VIAJE ###")
    print("-" * 60)
    nombre_viaje = validar_texto("\nIndica el nombre con el que quieres identificar el viaje o la ruta: ")
    destino_principal = validar_texto("Indica el destino principal del viaje: ")
    pasajero = validar_si_no("¿Llevas pasajero/a? (s/n): ")
    precio_combustible = validar_numero("Precio medio del combustible por litro: ")
    consumo_medio = validar_numero("Consumo medio de la moto (litros/100kms): ")
    
    # Crear etapas del viaje
    print("\n### DATOS DE LAS ETAPAS ###")
    print("-" * 60)
    etapas = []
    while True:
        print(f"\nEtapa {len(etapas) + 1}:")
        etapa = crear_etapa()
        etapas.append(etapa)
        if not validar_si_no("¿Deseas añadir otra etapa? (s/n): "):
            break

    # Recoger otros gastos del viaje
    print("\n### OTROS GASTOS DEL VIAJE ###")
    print("-" * 60)
    gastos_varios = otros_gastos()

    # Recoger equipación del piloto/pasajero
    print("\n### EQUIPACIÓN DEL PILOTO Y/O PASAJERO ###")
    print("-" * 60)
    equipo_moteros = equipar_moteros()

    # Recoger equipación de la moto
    print("\n### EQUIPACIÓN DE LA MOTO ###")
    print("-" * 60)
    equipo_moto = equipar_moto()

    # Recoger costes de mantenimiento
    print("\n### MANTENIMIENTO DE LA MOTO ###")
    print("-" * 60)
    mto = mantenimiento()
    
    # Calcular total del viaje
    total_viaje = 0.0
    
    # Sumar gastos de combustible
    for etapa in etapas:
        litros, costo = calcular_gasto_combustible(etapa['kms_etapa'], consumo_medio, precio_combustible)
        total_viaje += costo
    
    # Sumar otros gastos de las etapas
    for etapa in etapas:
        total_viaje += etapa['alojamiento_etapa']
        total_viaje += sum(etapa['alimentación_etapa'].values())
        total_viaje += etapa['aparcamiento_etapa']
        total_viaje += etapa['peaje_etapa']
        total_viaje += etapa['actividad_etapa']
        total_viaje += etapa['transporte_etapa']
        total_viaje += etapa['extra_etapa']
    
    # Sumar gastos varios
    total_viaje += gastos_varios['gastos_compras']
    total_viaje += gastos_varios['gastos_acampada']
    total_viaje += sum(gastos_varios['otras_tasas'].values())
    total_viaje += sum(gastos_varios['gastos_seguros'].values())
    
    # Sumar equipación y mantenimiento
    total_viaje += sum(equipo_moteros.values())
    total_viaje += sum(equipo_moto.values())
    total_viaje += sum(mto.values())

    # Menú de presentación de resultados
    while True:
        opcion = mostrar_menu("MENÚ DE PRESENTACIÓN DE RESULTADOS", [
            "Etiqueta del viaje",
            "Resumen del viaje y del presupuesto",
            "Presupuesto detallado",
            "Salir"
        ])
        
        if opcion == 1:
            mostrar_etiqueta_viaje(nombre_viaje, destino_principal, etapas, pasajero, total_viaje)
        elif opcion == 2:
            mostrar_resumen(nombre_viaje, destino_principal, etapas, pasajero, precio_combustible, consumo_medio, gastos_varios, equipo_moteros, equipo_moto, mto)
        elif opcion == 3:
            mostrar_detalle(nombre_viaje, destino_principal, etapas, pasajero, precio_combustible, consumo_medio, gastos_varios, equipo_moteros, equipo_moto, mto)
        elif opcion == 4:
            print("\nGracias por usar la calculadora de presupuestos. ¡V'ss!")
            break

# Ejecutar el programa si se ejecuta directamente
if __name__ == "__main__":
    main() 