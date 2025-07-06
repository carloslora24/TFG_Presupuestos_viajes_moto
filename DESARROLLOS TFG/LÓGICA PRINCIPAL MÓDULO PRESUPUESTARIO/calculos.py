###################################################
### LÓGICA DE PRESUPUESTACIÓN DE VIAJES EN MOTO ###
###################################################

# Trabajo Fin de Grado: Curso de Adaptación al Grado de Ingeniería Informática. UNIR. 
# Autor:
# Fecha Última Revisión: 17/05/2025


# Importar módulos necesarios
from datetime import datetime

#Funciones de validación de los datos de entrada

def validar_numero(valor):
    """
    Valida que un valor sea un número válido.
    Argumento: valor - Valor a validar.
    Devuelve: valor convertido a float o 0.0 si el valor es nulo.
    Excepción: Si el valor no es un número válido
    """
    if not valor:
        return 0.0
    try:
        return float(valor)
    except (ValueError, TypeError):
        raise ValueError(f"Error: El valor '{valor}' debe ser un número válido")

def validar_texto(texto):
    """
    Valida que un texto no esté vacío.
    Argumento: valor - Texto a validar.
    Devuelve: Texto validado sin espacios.
    Excepción: Si el texto es nulo.
    """
    if not texto or not texto.strip():
        raise ValueError("Error: El texto no puede estar vacío")
    return texto.strip()

def validar_fecha(fecha_str):
    """
    Valida y convierte una fecha en formato string a objeto datetime.
    Argumento: fecha_str - Fecha en formato DD/MM/AAAA
    Devuelve: Objeto datetime si la fecha es válida
    Excepción: Si el formato de la fecha no es válido.
    """
    if not fecha_str:
        raise ValueError("La fecha no puede estar vacía")
    try:
        return datetime.strptime(fecha_str, "%d/%m/%Y")
    except ValueError:
        raise ValueError(f"Formato de fecha inválido: {fecha_str}. Debe ser DD/MM/AAAA")

#Generación de formatos de salida: Etiqueta, Resumen y Completo

def generar_etiqueta_viaje(datos_viaje, etapas, total_viaje):
    """
    Genera un diccionario con los datos básicos del viaje.    
    Argumentos:
        datos_viaje (dict): Diccionario con los datos del viaje
        etapas (list): Lista de etapas del viaje
        total_viaje (float): Total calculado del viaje
    Devuelve: Diccionanrio con los datos de la etiqueta del viaje
    """
    return {
        "nombre_viaje": datos_viaje["nombre_viaje"],
        "destino_principal": datos_viaje["destino_principal"],
        "kilometros_totales": datos_viaje["kilometros_totales"],
        "numero_etapas": len(etapas),
        "presupuesto_total": total_viaje,
        "presupuesto_persona": datos_viaje["presupuesto_persona"],
        "pasajero": datos_viaje["pasajero"]
    }

def generar_resumen_viaje(datos_viaje, etapas, otros_gastos, equip_moteros, equip_moto, mantenimiento, totales):
    """
    Genera un diccionario con el resumen del viaje y sus gastos.
    Argumentos:
        datos_viaje (dict): Diccionario con los datos del viaje
        etapas (list): Lista de etapas del viaje
        otros_gastos (dict): Diccionario con otros gastos
        equip_moteros (dict): Diccionario con gastos de equipamiento de moteros
        equip_moto (dict): Diccionario con gastos de equipamiento de moto
        mantenimiento (dict): Diccionario con gastos de mantenimiento
        totales (dict): Diccionario con los totales calculados
    Devuelve: Diccionario con el resumen del viaje
    """
    # Calcular total_otros_gastos
    total_otros_gastos = round(
        otros_gastos['gastos_compras'] + 
        otros_gastos['gastos_acampada'] + 
        sum(otros_gastos['otras_tasas'].values()) + 
        sum(otros_gastos['gastos_seguros'].values()), 
        2
    )
    
    # Calcular total_equipamiento_moteros
    total_equipamiento_moteros = round(sum(equip_moteros.values()), 2)
    
    # Calcular total_equipamiento_moto
    total_equipamiento_moto = round(sum(equip_moto.values()), 2)
    
    # Calcular total_mantenimiento
    total_mantenimiento = round(sum(mantenimiento.values()), 2)
    
    # Calcular total_alojamiento
    total_alojamiento = round(sum(etapa["alojamiento_etapa"] for etapa in etapas), 2)
    
    # Calcular total_alimentacion
    total_alimentacion = round(sum(sum(etapa["alimentacion_etapa"].values()) for etapa in etapas), 2)
    
    # Calcular total_aparcamiento
    total_aparcamiento = round(sum(etapa["aparcamiento_etapa"] for etapa in etapas), 2)
    
    # Calcular total_peaje
    total_peaje = round(sum(etapa["peaje_etapa"] for etapa in etapas), 2)
    
    # Calcular total_actividad
    total_actividad = round(sum(etapa["actividad_etapa"] for etapa in etapas), 2)
    
    # Calcular total_transporte
    total_transporte = round(sum(etapa["transporte_etapa"] for etapa in etapas), 2)
    
    # Calcular total_extra
    total_extra = round(sum(etapa["extra_etapa"] for etapa in etapas), 2)
    
    # Obtener importe de compras
    total_compras = round(otros_gastos['gastos_compras'], 2)
    
    # Obtener coste de acampada
    total_acampada = round(otros_gastos['gastos_acampada'], 2)
    
    # Calcular total de tasas
    total_tasas = round(sum(otros_gastos['otras_tasas'].values()), 2)
    
    # Calcular total de seguros
    total_seguros = round(sum(otros_gastos['gastos_seguros'].values()), 2)
    
    return {
        "informacion_general": {
            "nombre_viaje": datos_viaje['nombre_viaje'],
            "destino_principal": datos_viaje['destino_principal'],
            "kilometros_totales": datos_viaje['kilometros_totales'],
            "kilometros_media_etapa": datos_viaje['kilometros_media_etapa'],
            "numero_etapas": len(etapas),
            "pasajero": datos_viaje['pasajero'],
            "fecha_inicio": datos_viaje['fecha_inicio'],
            "fecha_fin": datos_viaje['fecha_fin'],
            "precio_combustible": datos_viaje['precio_combustible'],
            "consumo_medio_moto": datos_viaje['consumo_medio_moto'],
            "litros_combustible": datos_viaje['litros_combustible'],
            "velocidad_media_total": datos_viaje['velocidad_media_total'],
            "tiempo_total_desplazamiento": datos_viaje['tiempo_total_desplazamiento'],
            "tiempo_desplazamiento_dia": datos_viaje['tiempo_desplazamiento_dia']
        },
        "resumen_gastos": {
            "combustible": datos_viaje['total_combustible'],
            "alojamiento": total_alojamiento,
            "alimentacion": total_alimentacion,
            "aparcamiento": total_aparcamiento,
            "peaje": total_peaje,
            "actividades": total_actividad,
            "transporte": total_transporte,
            "extra": total_extra,
            "compras": total_compras,
            "acampada": total_acampada,
            "tasas": total_tasas,
            "seguros": total_seguros,
            "equipamiento_moteros": total_equipamiento_moteros,
            "equipamiento_moto": total_equipamiento_moto,
            "mantenimiento": total_mantenimiento,
            "total_general": totales['total_general'],
            "presupuesto_persona": totales['presupuesto_persona']
        }
    }

def generar_detalle_viaje(datos_viaje, etapas, otros_gastos, equip_moteros, equip_moto, mantenimiento, totales):
    """
    Genera un diccionario con el detalle completo del viaje y todos sus gastos.
    Argumentos:
        datos_viaje (dict): Diccionario con los datos del viaje
        etapas (list): Lista de etapas del viaje
        otros_gastos (dict): Diccionario con otros gastos
        equip_moteros (dict): Diccionario con gastos de equipamiento de moteros
        equip_moto (dict): Diccionario con gastos de equipamiento de moto
        mantenimiento (dict): Diccionario con gastos de mantenimiento
        totales (dict): Diccionario con los totales calculados
    Devuelve: Diccionario con el detalle completo del viaje
    """
    # Procesar detalles de cada etapa
    etapas_detalladas = []
    i = 1  # Inicializamos el contador en 1
    for etapa in etapas:
        # Convertir tiempo de desplazamiento a formato HH:MM
        tiempo_desplazamiento = etapa['tiempo_desplazamiento_etapa']
        horas = int(tiempo_desplazamiento)
        minutos = int((tiempo_desplazamiento - horas) * 60)
        tiempo_formateado = f"{horas:02d}:{minutos:02d}"
        
        etapa_detalle = {
            "informacion_etapa": {
                "numero_etapa": i,  # Usamos el contador
                "origen": etapa['origen_etapa'],
                "destino": etapa['destino_etapa'],
                "kilometros": etapa['kms_etapa'],
                "fecha": etapa['fecha'],
                "velocidad_media": etapa['velocidad_media_etapa'],
                "tiempo_desplazamiento_etapa": tiempo_formateado
            },
            "gastos_etapa": {
                "presupuesto_etapa": etapa['presupuesto_etapa'],
                "combustible_etapa": etapa['combustible_etapa'],
                "litros_etapa": etapa['litros_etapa'],
                "alojamiento": etapa['alojamiento_etapa'],
                "total_alimentacion": etapa['total_alimentacion_etapa'],
                "alimentacion": etapa['alimentacion_etapa'],
                "aparcamiento": etapa['aparcamiento_etapa'],
                "peaje": etapa['peaje_etapa'],
                "actividades": etapa['actividad_etapa'],
                "transporte": etapa['transporte_etapa'],
                "extra": etapa['extra_etapa']
            }
        }
        etapas_detalladas.append(etapa_detalle)
        i += 1  # Incrementamos el contador manualmente

    return {
        "informacion_general": {
            "nombre_viaje": datos_viaje['nombre_viaje'],
            "destino_principal": datos_viaje['destino_principal'],
            "kilometros_totales": datos_viaje['kilometros_totales'],
            "kilometros_media_etapa": datos_viaje['kilometros_media_etapa'],
            "numero_etapas": datos_viaje['numero_etapas'],
            "fecha_inicio": datos_viaje['fecha_inicio'],
            "fecha_fin": datos_viaje['fecha_fin'],
            "pasajero": datos_viaje['pasajero'],
            "precio_combustible": datos_viaje['precio_combustible'],
            "consumo_medio_moto": datos_viaje['consumo_medio_moto'],
            "litros_combustible": datos_viaje['litros_combustible'],
            "total_combustible": datos_viaje['total_combustible'],
            "velocidad_media_total": datos_viaje['velocidad_media_total'],
            "tiempo_total_desplazamiento": datos_viaje['tiempo_total_desplazamiento'],
            "tiempo_desplazamiento_dia": datos_viaje['tiempo_desplazamiento_dia']
        },
        "etapas": etapas_detalladas,
        "otros_gastos": {
            "total_otros_gastos": round(
                otros_gastos['gastos_compras'] + 
                otros_gastos['gastos_acampada'] + 
                sum(otros_gastos['otras_tasas'].values()) + 
                sum(otros_gastos['gastos_seguros'].values()), 
                2
            ),
            "compras": otros_gastos['gastos_compras'],
            "acampada": otros_gastos['gastos_acampada'],
            "tasas": otros_gastos['otras_tasas'],
            "seguros": otros_gastos['gastos_seguros']
        },
        "equipamiento": {
            "moteros": {
                "total_equipamiento_moteros": round(sum(equip_moteros.values()), 2),
                "casco": equip_moteros['casco'],
                "guantes_invierno": equip_moteros['guantes_invierno'],
                "guantes_verano": equip_moteros['guantes_verano'],
                "botas_invierno": equip_moteros['botas_invierno'],
                "botas_verano": equip_moteros['botas_verano'],
                "chaqueta_invierno": equip_moteros['chaqueta_invierno'],
                "chaqueta_verano": equip_moteros['chaqueta_verano'],
                "pantalon_invierno": equip_moteros['pantalon_invierno'],
                "pantalon_verano": equip_moteros['pantalon_verano'],
                "ropa_termica": equip_moteros['ropa_termica'],
                "traje_agua": equip_moteros['traje_agua'],
                "airbag": equip_moteros['airbag'],
                "protecciones_adicionales": equip_moteros['protecciones_adicionales'],
                "kit_primeros_auxilios": equip_moteros['kit_primeros_auxilios'],
                "intercomunicadores": equip_moteros['intercomunicadores'],
                "equipacion_otros": equip_moteros['equipacion_otros']
            },
            "moto": {
                "total_equipamiento_moto": round(sum(equip_moto.values()), 2),
                "equipacion_navegador": equip_moto['equipacion_navegador'],
                "equipacion_equipaje": equip_moto['equipacion_equipaje'],
                "equipacion_funda": equip_moto['equipacion_funda'],
                "equipacion_extintor": equip_moto['equipacion_extintor'],
                "equipacion_otros": equip_moto['equipacion_otros']
            }
        },
        "mantenimiento": {
            "total_mantenimiento": round(sum(mantenimiento.values()), 2),
            "mto_pinchazos": mantenimiento['mto_pinchazos'],
            "mto_herramientas": mantenimiento['mto_herramientas'],
            "mto_compresor": mantenimiento['mto_compresor'],
            "mto_arrancador": mantenimiento['mto_arrancador'],
            "mto_rev_previa": mantenimiento['mto_rev_previa'],
            "mto_talleres": mantenimiento['mto_talleres'],
            "mto_neumaticos": mantenimiento['mto_neumaticos'],
            "mto_frenos": mantenimiento['mto_frenos'],
            "mto_transmision": mantenimiento['mto_transmision'],
            "mto_otros": mantenimiento['mto_otros'],
            "mto_rev_post": mantenimiento['mto_rev_post']
        },
        "totales": {
            "total_general": totales['total_general'],
            "presupuesto_persona": totales['presupuesto_persona']
        }
    }

# Función principal

def procesar_presupuestovm(datos_presupuesto, formato_respuesta="completo"):
    """
    Procesa el presupuesto del viaje en moto y devuelve la información en el formato solicitado.
    Argumentos: 
        datos_presupuesto (dict): Diccionario con todos los datos del viaje
        formato_respuesta (str): Formato de respuesta deseado ("etiqueta", "resumen" o "completo")
    Devuelve: Diccionario con la información procesada en el formato solicitado
    """
    # Validar formato de respuesta
    if formato_respuesta not in ["etiqueta", "resumen", "completo"]:
        raise ValueError("Formato de respuesta no válido. Debe ser 'etiqueta', 'resumen' o 'completo'")
    
    # Extraer datos del presupuesto
    datos_viaje = datos_presupuesto["datos_viaje"]
    etapas = datos_presupuesto["etapas"]
    otros_gastos = datos_presupuesto["otros_gastos"]
    equipamiento_moteros = datos_presupuesto["equipamiento_moteros"]
    equipamiento_moto = datos_presupuesto["equipamiento_moto"]
    mantenimiento = datos_presupuesto["mantenimiento"]
    
    # Validar datos de texto
    datos_viaje["nombre_viaje"] = validar_texto(datos_viaje["nombre_viaje"])
    datos_viaje["destino_principal"] = validar_texto(datos_viaje["destino_principal"])
    
    # Validar datos numéricos básicos
    datos_viaje["precio_combustible"] = validar_numero(datos_viaje["precio_combustible"])
    datos_viaje["consumo_medio_moto"] = validar_numero(datos_viaje["consumo_medio_moto"])
    
    # Validar y procesar cada etapa
    for etapa in etapas:
        etapa["origen_etapa"] = validar_texto(etapa["origen_etapa"])
        etapa["destino_etapa"] = validar_texto(etapa["destino_etapa"])
        etapa["fecha"] = validar_fecha(etapa["fecha"]).strftime("%d/%m/%Y")
    
    # Calcular fechas de inicio y fin
    if etapas:
        fechas = [etapa["fecha"] for etapa in etapas]
        fechas_ordenadas = sorted(fechas)
        datos_viaje["fecha_inicio"] = validar_fecha(fechas_ordenadas[0]).strftime("%d/%m/%Y")
        datos_viaje["fecha_fin"] = validar_fecha(fechas_ordenadas[-1]).strftime("%d/%m/%Y")
    
    # Calcular kilómetros totales
    total_etapas = round(sum(validar_numero(etapa["kms_etapa"]) for etapa in etapas), 2)
    datos_viaje["kilometros_totales"] = total_etapas
    
    # Calcular totales
    total_alojamiento = round(sum(validar_numero(etapa["alojamiento_etapa"]) for etapa in etapas), 2)
    total_alimentacion = round(sum(sum(validar_numero(valor) for valor in etapa["alimentacion_etapa"].values()) for etapa in etapas), 2)
    total_aparcamiento = round(sum(validar_numero(etapa["aparcamiento_etapa"]) for etapa in etapas), 2)
    total_peaje = round(sum(validar_numero(etapa["peaje_etapa"]) for etapa in etapas), 2)
    total_actividad = round(sum(validar_numero(etapa["actividad_etapa"]) for etapa in etapas), 2)
    total_transporte = round(sum(validar_numero(etapa["transporte_etapa"]) for etapa in etapas), 2)
    total_extra = round(sum(validar_numero(etapa["extra_etapa"]) for etapa in etapas), 2)
    
    # Calcular totales de equipamiento
    total_equipamiento_moteros = round(sum(validar_numero(valor) for valor in equipamiento_moteros.values()), 2)
    total_equipamiento_moto = round(sum(validar_numero(valor) for valor in equipamiento_moto.values()), 2)
    total_mantenimiento = round(sum(validar_numero(valor) for valor in mantenimiento.values()), 2)
    
    # Calcular totales de otros gastos
    total_compras = round(validar_numero(otros_gastos["gastos_compras"]), 2)
    total_acampada = round(validar_numero(otros_gastos["gastos_acampada"]), 2)
    total_tasas = round(sum(validar_numero(valor) for valor in otros_gastos["otras_tasas"].values()), 2)
    total_seguros = round(sum(validar_numero(valor) for valor in otros_gastos["gastos_seguros"].values()), 2)
    total_otros_gastos = round(total_compras + total_acampada + total_tasas + total_seguros, 2)
    
    # Calcular total general
    total_general = round(
        total_alojamiento + total_alimentacion + total_aparcamiento + 
        total_peaje + total_actividad + total_transporte + total_extra +
        total_equipamiento_moteros + total_equipamiento_moto + 
        total_mantenimiento + total_otros_gastos, 2
    )
    
    # Calcular total combustible
    precio_combustible = datos_viaje["precio_combustible"]
    consumo_medio = datos_viaje["consumo_medio_moto"]
    total_litros = round((total_etapas * consumo_medio) / 100, 2)
    total_combustible = round(total_litros * precio_combustible, 2)
    
    # Asignar valores calculados a datos_viaje
    datos_viaje["litros_combustible"] = total_litros
    datos_viaje["total_combustible"] = total_combustible
    
    # Calcular total general con combustible
    total_general_con_combustible = round(total_general + total_combustible, 2)
    
    # Calcular presupuesto por persona
    pasajero = datos_viaje["pasajero"]
    presupuesto_persona = round(total_general_con_combustible / 2 if pasajero else total_general_con_combustible, 2)
    datos_viaje["presupuesto_persona"] = presupuesto_persona
    
    # Calcular totales por etapa
    tiempo_total_desplazamiento = 0
    for etapa in etapas:
        kms_etapa = validar_numero(etapa["kms_etapa"])
        litros_etapa = round((kms_etapa * consumo_medio) / 100, 2)
        combustible_etapa = round(litros_etapa * precio_combustible, 2)
        
        # Calcular suma de gastos de alimentación por etapa
        total_alimentacion_etapa = round(sum(validar_numero(valor) for valor in etapa["alimentacion_etapa"].values()), 2)
        etapa["total_alimentacion_etapa"] = total_alimentacion_etapa
        
        # Calcular presupuesto por etapa
        presupuesto_etapa = round(
            validar_numero(etapa["alojamiento_etapa"]) +
            total_alimentacion_etapa +
            validar_numero(etapa["aparcamiento_etapa"]) +
            validar_numero(etapa["peaje_etapa"]) +
            validar_numero(etapa["actividad_etapa"]) +
            validar_numero(etapa["transporte_etapa"]) +
            validar_numero(etapa["extra_etapa"]) +
            combustible_etapa, 2
        )
        
        # Calcular tiempo de desplazamiento por etapa
        velocidad_media = validar_numero(etapa["velocidad_media_etapa"])
        tiempo_desplazamiento = kms_etapa / velocidad_media if velocidad_media > 0 else 0
        tiempo_total_desplazamiento += tiempo_desplazamiento
        
        # Añadir campos calculados a la etapa
        etapa["tiempo_desplazamiento_etapa"] = tiempo_desplazamiento
        etapa["presupuesto_etapa"] = presupuesto_etapa
        etapa["combustible_etapa"] = combustible_etapa
        etapa["litros_etapa"] = litros_etapa
    
    # Calcular kilómetros media por etapa
    kilometros_media_etapa = round(total_etapas / len(etapas), 2) if etapas else 0
    datos_viaje["kilometros_media_etapa"] = kilometros_media_etapa
    
    # Calcular velocidad media total
    velocidad_media_total = round(sum(validar_numero(etapa["velocidad_media_etapa"]) for etapa in etapas) / len(etapas)) if etapas else 0
    datos_viaje["velocidad_media_total"] = velocidad_media_total
    
    # Calcular tiempo de desplazamiento por día
    tiempo_desplazamiento_dia = tiempo_total_desplazamiento / len(etapas) if etapas else 0
    horas_dia = int(tiempo_desplazamiento_dia)
    minutos_dia = int((tiempo_desplazamiento_dia - horas_dia) * 60)
    datos_viaje["tiempo_desplazamiento_dia"] = f"{horas_dia:02d}:{minutos_dia:02d}"
    
    # Añadir tiempo total de desplazamiento
    horas_total = int(tiempo_total_desplazamiento)
    minutos_total = int((tiempo_total_desplazamiento - horas_total) * 60)
    datos_viaje["tiempo_total_desplazamiento"] = f"{horas_total:02d}:{minutos_total:02d}"
    
    # Añadir número de etapas
    datos_viaje["numero_etapas"] = len(etapas)
    
    # Crear diccionario con los totales
    totales = {
        "total_general": total_general_con_combustible,
        "presupuesto_persona": presupuesto_persona
    }
    
    # Generar respuesta según el formato solicitado
    if formato_respuesta == "etiqueta":
        return generar_etiqueta_viaje(
            datos_viaje,
            etapas,
            total_general_con_combustible
        )
    elif formato_respuesta == "resumen":
        return generar_resumen_viaje(
            datos_viaje,
            etapas,
            otros_gastos,
            equipamiento_moteros,
            equipamiento_moto,
            mantenimiento,
            totales
        )
    else:  # formato_respuesta == "completo"
        return generar_detalle_viaje(
            datos_viaje,
            etapas,
            otros_gastos,
            equipamiento_moteros,
            equipamiento_moto,
            mantenimiento,
            totales
        ) 