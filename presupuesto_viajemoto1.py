###############################################
###   PRESUPUESTOS DE VIAJES EN MOTO v.1.0  ###
###############################################

# Autor: Carlos Lora Espinosa
# Fecha: 12/04/2025

# Importar el módulo datetime para utilizar fechas
from datetime import datetime 

# Función para crear las etapas del viaje:
def crear_etapa():
    print("\nDatos de la etapa:")
    # Crear un diccionario con todos los datos de la etapa
    etapa = {
        # Solicitar y guardar el origen de la etapa
        'origen_etapa': input("Origen de la etapa: "),
        # Solicitar y guardar el destino de la etapa
        'destino_etapa': input("Destino de la etapa: "),
        # Solicitar los kilómetros y convertir a float, si no se ingresa nada usar 0
        'kms_etapa': float(input("Kilómetros de la etapa: ") or "0"),
        # Solicitar la fecha prevista
        'fecha': input("Fecha prevista de la etapa: "),
        # Solicitar la velocidad media y convertir a float
        'velocidad_media_etapa': float(input("Velocidad media estimada de la etapa: ") or "0"),
        # Solicitar el coste de alojamiento y convertir a float
        'alojamiento_etapa': float(input("Coste alojamiento: ") or "0"),
        # Crear diccionario anidado para los gastos de alimentación
        'alimentación_etapa': { 
            # Solicitar y convertir cada tipo de gasto en alimentación
            'alimentacion_desayuno': float(input("Coste desayuno: ") or "0"),
            'alimentacion_almuerzo': float(input("Coste almuerzo: ") or "0"),
            'alimentacion_comida': float(input("Coste comida: ") or "0"),
            'alimentacion_merienda': float(input("Coste merienda: ") or "0"),
            'alimentacion_cena': float(input("Coste cena: ") or "0"),
            'alimentacion_otros': float(input("Algún otro gasto más en alimentación o bebida? ") or "0")
        },
        # Solicitar y convertir otros gastos de la etapa
        'aparcamiento_etapa': float(input("Gasto en aparcamiento: ") or "0"),
        'peaje_etapa': float(input("Gasto en peajes: ") or "0"),
        'actividad_etapa': float(input("Previsión de gastos en actividades culturales y de ocio: ") or "0"),
        'transporte_etapa': float(input("Gastos de transporte como tranporte público o transporte para la moto: ") or "0"),
        'extra_etapa': float(input("Previsión de gastos extra: ") or "0")
    }
    # Devolver el diccionario con todos los datos de la etapa
    return etapa

# Función para obtener otros gastos relacionados con el viaje
def otros_gastos():
    print("Indica otros costes relacionados con el viaje.")
    # Crear y devolver diccionario con otros gastos
    return{
        # Solicitar y convertir gastos en compras
        'gastos_compras': float(input("Indica la previsión de gastos en compras como regalos o souvenirs: ") or "0"),
        # Solicitar y convertir gastos de acampada
        'gastos_acampada': float(input("¿Tienes pensado acampar?. Indica el coste previsto para el equipo de acampada: ") or "0"),
        # Crear diccionario anidado para tasas
        'otras_tasas': {
            'tasas_visados': float(input("Indica el coste de los visados necesarios según los países que visites: ") or "0"),
            'tasas_pases': float(input("Indica el coste de los pases o permisos de circulación por carreteras y autovías que necesites en cada país: ") or "0"),
            'tasas_otros': float(input("Indica los costes de otras tasas o impuestos que puedas necesitar en el viaje: ") or "0")
        },
        # Crear diccionario anidado para seguros
        'gastos_seguros': {
            'seguro_moto': float(input("¿Necesitas alguna cobertura adicional?. Indica los costes del seguro de la moto si necesitas contratar alguna cobertura adicional: ") or "0"),
            'seguro_viaje': float(input("¿Vas a contratar un seguro de viaje?. Introduce su precio en caso afirmativo: ") or "0"),
            'seguro_salud': float(input("¿Vas a viajar al extranjero?. Quizás vendría bien contratar un seguro de salud: ") or "0"),
            'seguro_otros': float(input("¿Necesitas algún otro seguro?. Indica el coste previsto: ") or "0")
        }
    }

# Función para obtener los costes de equipación para piloto y pasajero
def equipar_moteros():
    print("Indica los costes de la equpación que necesites adquirir para el piloto y/o pasajero. Si no lo necesitas indica un 0.")
    # Crear y devolver diccionario con equipación
    return{
        # Solicitar y convertir cada elemento de equipación
        'equipo_casco': float(input("¿Casco?: ") or "0"),
        'equipo_guantes_inv': float(input("¿Guantes de invierno?: ") or "0"),
        'equipo_guantes_ver': float(input("¿Guantes de verano?: ") or "0"),
        'equipo_botas_inv': float(input("¿Botas de invierno?: ") or "0"),
        'equipo_botas_ver': float(input("¿Botas de verano?: ") or "0"),
        'equipo_chaqueta_inv': float(input("¿Chaqueta de invierno?: ") or "0"),
        'equipo_chaqueta_ver': float(input("¿Chaqueta de verano?: ") or "0"),
        'equipo_pantalon_inv': float(input("¿Pantalón de invierno?: ") or "0"),
        'equipo_pantalon_ver': float(input("¿Pantalón de verano?: ") or "0"),
        'equipo_ropa_termica': float(input("¿Ropa térmica?: ") or "0"),
        'equipo_traje_agua': float(input("¿Traje de agua?: ") or "0"),
        'equipo_airbag': float(input("¿Chaleco o chaqueta airbag?: ") or "0"),
        'equipo_protecciones': float(input("¿Protecciones adionales?: ") or "0"),
        'equipo_auxilio': float(input("¿Kit de primeros auxilios?: ") or "0"),
        'equipo_intercom': float(input("¿Intercomunicadores o manos libres?: ") or "0"),
        'equipo_otros': float(input("¿Algún otro elemento de equipación para el piloto o el pasajero?: ") or "0")
    }

# Función para obtener los costes de equipación para la moto
def equipar_moto():
    print("Indica los costes del equipamiento necesario para tu moto. ")
    # Crear y devolver diccionario con equipación de la moto
    return{
        # Solicitar y convertir cada elemento de equipación
        'equipacion_navegador': float(input("Navegador o dispositivo de navegación GPS y soportes: ") or "0"),
        'equipacion_equipaje': float(input("¿Necesitas maletas, bolsas o soportes para tu equipaje?. Indica los costes previstos: ") or "0"),
        'equipacion_funda': float(input("Si quieres proteger tu moto y te queda sitio en la maleta puedes contar con una funda: ") or "0"),
        'equipacion_extintor': float(input("Extintor. Nunca se sabe: ") or "0"),
    }

# Función para obtener los costes de mantenimiento
def mantenimiento():
    print("Indica el coste previsto para el mantenimiento necesario de la moto relacionado con el viaje.")
    # Crear y devolver diccionario con costes de mantenimiento
    return{
        # Solicitar y convertir cada elemento del mantenimiento
        'mto_pinchazos': float(input("Kit de reparación de pinchazos: ") or "0"),
        'mto_herramientas': float(input("Herramientas: ") or "0"),
        'mto_compresor': float(input("Compresor de aire portátil: ") or "0"),
        'mto_arrancador': float(input("Arrancador de batería portátil: ") or "0"),
        'mto_rev_previa': float(input("Revisión previa al viaje:") or "0"),
        'mto_talleres': float(input("Otros costes de mano de obra de mecánico: ") or "0"),
        'mto_neumaticos': float(input("¿Necesitas un cambio de ruedas?. Indica su coste: ") or "0"),
        'mto_frenos': float(input("¿Cómo llevas las pastillas de freno?. Incluye su precio: ") or "0"),
        'mto_transmision': float(input("Indica el coste del mantenimiento de la transmisión. Quizás necesite un ajuste de cadena y un buen engrasado: ") or "0"),
        'mto_otros': float(input("Indica cualquier otro coste asociado con el mantenimiento de la moto de cara al viaje: ") or "0"),
        'mto_rev_post': float(input("Coste revisión posterior al viaje: ") or "0")
    }

# Función para calcular el gasto en combustible
def calcular_gasto_combustible(kilometros, consumo_medio, precio_combustible):
    # Calcular litros necesarios (kilómetros * consumo medio / 100)
    litros = (kilometros * consumo_medio) / 100
    # Calcular costo total (litros * precio por litro)
    costo = litros * precio_combustible
    # Devolver litros y costo
    return litros, costo

# Función para calcular el tiempo de desplazamiento
def calcular_tiempo_desplazamiento(kilometros, velocidad):
    # Calcular horas totales
    horas = kilometros / velocidad
    # Obtener horas enteras
    horas_enteras = int(horas)
    # Calcular minutos restantes
    minutos = int((horas - horas_enteras) * 60)
    # Devolver formato de tiempo
    return f"{horas_enteras}h {minutos}m"

# Función para mostrar la etiqueta del viaje
def mostrar_etiqueta_viaje(nombre_viaje, destino_principal, etapas, pasajero, total_viaje):
    print("\n##### ETIQUETA DEL VIAJE #####")
    print("-" * 60)
    # Mostrar información básica del viaje
    print(f"Nombre del viaje: {nombre_viaje}")
    print(f"Destino principal del viaje: {destino_principal}")
    # Calcular y mostrar kilómetros totales
    total_kilometros = sum(etapa['kms_etapa'] for etapa in etapas)
    print(f"Kilómetros totales: {total_kilometros:.2f}km")
    print(f"Número de etapas: {len(etapas)}")
    print(f"Presupuesto total del viaje: {total_viaje:.2f}€")
    # Si hay pasajero, mostrar presupuesto por persona
    if pasajero:
        print(f"Presupuesto por persona: {total_viaje/2:.2f}€")
    print(f"Pasajero: {'Sí' if pasajero else 'No'}")
    # Esperar entrada del usuario para continuar
    input("\nPresiona Enter para continuar...")

# Función para mostrar el resumen del viaje
def mostrar_resumen(nombre_viaje, destino_principal, etapas, pasajero, precio_combustible, consumo_medio, gastos_varios, equipo_moteros, equipo_moto, mto):
    print("\n##### RESUMEN DEL VIAJE #####")
    print("-" *60)
    
    # Calcular estadísticas del viaje
    total_kilometros = sum(etapa['kms_etapa'] for etapa in etapas)
    kms_medio_etapa = total_kilometros / len(etapas)
    velocidad_media = sum(etapa['velocidad_media_etapa'] for etapa in etapas) / len(etapas)
    total_litros = sum(calcular_gasto_combustible(etapa['kms_etapa'], consumo_medio, precio_combustible)[0] for etapa in etapas)
    tiempo_total = sum(etapa['kms_etapa'] / etapa['velocidad_media_etapa'] for etapa in etapas)
    horas_total = int(tiempo_total)
    minutos_total = int((tiempo_total - horas_total) * 60)

    # Mostrar información general del viaje
    print(f"Nombre del viaje: {nombre_viaje}")
    print(f"Destino principal del viaje: {destino_principal}")
    print(f"Kilómetros totales: {total_kilometros:.2f} km")
    print(f"Kilómetros de media por etapa: {kms_medio_etapa:.2f} km")
    print(f"Número de etapas: {len(etapas)}")
    print(f"Pasajero: {'Sí' if pasajero else 'No'}")
    print(f"Fecha de inicio del viaje: {etapas[0]['fecha']}")
    print(f"Fecha de fin del viaje: {etapas[-1]['fecha']}")
    print(f"Precio medio del combustible: {precio_combustible}€/L")
    print(f"Consumo medio de la moto: {consumo_medio} L/100kms")
    print(f"Total litros de combustible: {total_litros:.2f} L")
    print(f"Velocidad media: {velocidad_media:.2f} kms/h")
    print(f"Tiempo total de desplazamiento: {horas_total}h {minutos_total}m")
    
    # Mostrar resumen de gastos
    print("\nResumen de gastos:")
    # Calcular totales por categoría
    total_combustible = sum(calcular_gasto_combustible(etapa['kms_etapa'], consumo_medio, precio_combustible)[1] for etapa in etapas)
    total_alojamiento = sum(etapa['alojamiento_etapa'] for etapa in etapas)
    total_alimentacion = sum(sum(etapa['alimentación_etapa'].values()) for etapa in etapas)
    total_aparcamiento = sum(etapa['aparcamiento_etapa'] for etapa in etapas)
    total_peaje = sum(etapa['peaje_etapa'] for etapa in etapas)
    total_actividades = sum(etapa['actividad_etapa'] for etapa in etapas)
    total_transporte = sum(etapa['transporte_etapa'] for etapa in etapas)
    total_extra = sum(etapa['extra_etapa'] for etapa in etapas)

    # Mostrar gastos por etapas
    print(f"Combustible: {total_combustible:.2f}€")
    print(f"Alojamiento: {total_alojamiento:.2f}€")
    print(f"Alimentación: {total_alimentacion:.2f}€")
    print(f"Aparcamiento: {total_aparcamiento:.2f}€")
    print(f"Peajes: {total_peaje:.2f}€")
    print(f"Actividades culturales y de ocio: {total_actividades:.2f}€")
    print(f"Transporte: {total_transporte:.2f}€")
    print(f"Gastos Extra: {total_extra:.2f}€")

    # Mostrar otros gastos
    print(f"Compras y souvenirs: {gastos_varios['gastos_compras']:.2f}€")
    print(f"Gastos de Acampada: {gastos_varios['gastos_acampada']:.2f}€")
    print(f"Tasas: {sum(gastos_varios['otras_tasas'].values()):.2f}€")
    print(f"Seguros: {sum(gastos_varios['gastos_seguros'].values()):.2f}€")
    print(f"Equipación piloto y/o pasajero: {sum(equipo_moteros.values()):.2f}€")
    print(f"Equipación moto: {sum(equipo_moto.values()):.2f}€")
    print(f"Mantenimiento: {sum(mto.values()):.2f}€")
    
    # Calcular y mostrar total del viaje
    total_viaje = (total_combustible + total_alojamiento + total_alimentacion + total_aparcamiento + total_peaje + total_actividades + total_transporte + 
                   total_extra + gastos_varios['gastos_compras'] + gastos_varios['gastos_acampada'] + sum(gastos_varios['otras_tasas'].values()) + 
                   sum(gastos_varios['gastos_seguros'].values()) + sum(equipo_moteros.values()) + 
                   sum(equipo_moto.values()) + sum(mto.values()))
    
    print(f"\nTOTAL VIAJE: {total_viaje:.2f}€")
    if pasajero:
        print(f"TOTAL POR PERSONA: {total_viaje/2:.2f}€")

    # Esperar entrada del usuario para continuar
    input("\nPresiona Enter para continuar...")
    return total_viaje

# Función para mostrar el presupuesto detallado
def mostrar_detalle(nombre_viaje, destino_principal, etapas, pasajero, precio_combustible, consumo_medio, gastos_varios, equipo_moteros, equipo_moto, mto):
    print("\n##### PRESUPUESTO DETALLADO #####")
    print("-" * 60)

    # Mostrar información general del viaje
    print("Información del Viaje:")
    total_kilometros = sum(etapa['kms_etapa'] for etapa in etapas)
    kms_medio_etapa = total_kilometros / len(etapas)
    velocidad_media = sum(etapa['velocidad_media_etapa'] for etapa in etapas) / len(etapas)
    total_litros = sum(calcular_gasto_combustible(etapa['kms_etapa'], consumo_medio, precio_combustible)[0] for etapa in etapas)
    tiempo_total = sum(etapa['kms_etapa'] / etapa['velocidad_media_etapa'] for etapa in etapas)
    horas_total = int(tiempo_total)
    minutos_total = int((tiempo_total - horas_total) * 60)

    print(f"Nombre del viaje: {nombre_viaje}")
    print(f"Destino principal del viaje: {destino_principal}")
    print(f"Kilómetros totales: {total_kilometros:.2f}kms")
    print(f"Fecha de inicio del viaje: {etapas[0]['fecha']}")
    print(f"Fecha de fin del viaje: {etapas[-1]['fecha']}")
    print(f"Precio medio del combustible: {precio_combustible}€/L")
    print(f"Consumo medio de la moto: {consumo_medio} L/100km")
    print(f"Total litros de combustible: {total_litros:.2f} L")
    print(f"Velocidad media: {velocidad_media:.2f} km/h")
    print(f"Tiempo total de desplazamiento: {horas_total}h {minutos_total}m")

    # Mostrar presupuesto detallado por etapas
    print("\nPresupuesto detallado:")
    print("Detalle por etapas:")

    # Iterar sobre cada etapa
    for i, etapa in enumerate(etapas, 1):
        print(f"\nInformación Etapa {i}:")
        print(f"Origen: {etapa['origen_etapa']}")
        print(f"Destino: {etapa['destino_etapa']}")
        print(f"Kilómetros: {etapa['kms_etapa']}")
        print(f"Fecha de la etapa: {etapa['fecha']}")
        print(f"Velocidad media de la etapa: {etapa['velocidad_media_etapa']}")
        print(f"Tiempo de desplazamiento: {calcular_tiempo_desplazamiento(etapa['kms_etapa'], etapa['velocidad_media_etapa'])}")

        # Calcular costos de la etapa
        litros_etapa, costo_combustible = calcular_gasto_combustible(etapa['kms_etapa'], consumo_medio, precio_combustible)
        total_etapa = (costo_combustible + etapa['alojamiento_etapa'] + 
                      sum(etapa['alimentación_etapa'].values()) + 
                      etapa['aparcamiento_etapa'] + etapa['peaje_etapa'] + 
                      etapa['actividad_etapa'] + etapa['transporte_etapa'] + 
                      etapa['extra_etapa'])
        
        # Mostrar presupuesto de la etapa
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
    
    # Mostrar detalle de otros gastos
    print("\nDetalle de los demás gastos del viaje:")
    print(f"Compras y souvenirs: {gastos_varios['gastos_compras']:.2f}€")
    print(f"Gastos de Acampada: {gastos_varios['gastos_acampada']:.2f}€")
    
    # Mostrar tasas
    print("\nTasas:")
    for tasa, costo in gastos_varios['otras_tasas'].items():
        if costo > 0:
            print(f"  {tasa.replace('_', ' ').title()}: {costo:.2f}€")
    
    # Mostrar seguros
    print("\nSeguros:")
    for seguro, costo in gastos_varios['gastos_seguros'].items():
        if costo > 0:
            print(f"  {seguro.replace('_', ' ').title()}: {costo:.2f}€")
    
    # Mostrar equipación del piloto/pasajero
    print("\nEquipación piloto y/o pasajero:")
    for item, costo in equipo_moteros.items():
        if costo > 0:
            print(f"  {item.replace('_', ' ').title()}: {costo:.2f}€")
    
    # Mostrar equipación de la moto
    print("\nEquipación moto:")
    for item, costo in equipo_moto.items():
        if costo > 0:
            print(f"  {item.replace('_', ' ').title()}: {costo:.2f}€")
    
    # Mostrar mantenimiento
    print("\nMantenimiento:")
    for item, costo in mto.items():
        if costo > 0:
            print(f"  {item.replace('_', ' ').title()}: {costo:.2f}€")

    # Calcular y mostrar total del viaje
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
    
    # Esperar entrada del usuario para continuar
    input("\nPresiona Enter para continuar...")


# Función principal del programa
def main():
    print("##### CALCULADORA DE PRESUPUESTOS DE VIAJES EN MOTO #####")

    # Solicitar datos generales del viaje
    print("\n### DATOS GENERALES DEL VIAJE ###")
    print("-" * 60)
    nombre_viaje = input("\nIndica el nombre con el que quieres identificar el viaje o la ruta: ")
    destino_principal = input("Indica el destino principal del viaje: ")
    pasajero = input("¿Llevas pasajero/a? (s/n): ").lower() == 's'
    precio_combustible = float(input("Precio medio del combustible por litro: ") or "0")
    consumo_medio = float(input("Consumo medio de la moto (litros/100kms): ") or "0")
    
    # Crear etapas del viaje
    print("\n### DATOS DE LAS ETAPAS ###")
    print("-" * 60)
    etapas = []
    while True:
        print(f"\nEtapa {len(etapas) + 1}:")
        etapa = crear_etapa()
        etapas.append(etapa)
        if input("¿Deseas añadir otra etapa? (s/n): ").lower() != 's':
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
    
    # Calcular total del viaje:
    total_viaje = 0.0   # Inicializa la variable total_viaje como float
    
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
        print("\n### MENÚ DE PRESENTACIÓN DE RESULTADOS ###")
        print("-" * 60)
        print("Selecciona un modo de presentación de los resultados del presupuesto:")
        print("1. Etiqueta del viaje")
        print("2. Resumen del viaje y del presupuesto")
        print("3. Presupuesto detallado")
        print("4. Salir")
        
        opcion = input("\nIndica una opción (1-4): ")
        
        if opcion == "1":
            mostrar_etiqueta_viaje(nombre_viaje, destino_principal, etapas, pasajero, total_viaje)
        elif opcion == "2":
            mostrar_resumen(nombre_viaje, destino_principal, etapas, pasajero, precio_combustible, consumo_medio, gastos_varios, equipo_moteros, equipo_moto, mto)
        elif opcion == "3":
            mostrar_detalle(nombre_viaje, destino_principal, etapas, pasajero, precio_combustible, consumo_medio, gastos_varios, equipo_moteros, equipo_moto, mto)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

# Ejecutar el programa.
if __name__ == "__main__":
    main() 