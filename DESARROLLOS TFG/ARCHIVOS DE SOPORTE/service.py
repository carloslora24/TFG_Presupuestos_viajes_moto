from models import (
    PresupuestoRequest, 
    PresupuestoResponse, 
    GastosEtapa,
    Etapa
)

class PresupuestoService:
    @staticmethod
    def calcular_gasto_combustible(kilometros: float, consumo_medio: float, precio_combustible: float) -> float:
        return (kilometros * consumo_medio * precio_combustible) / 100

    @staticmethod
    def calcular_total_alimentacion(gastos_alimentacion) -> float:
        return (gastos_alimentacion.desayuno + 
                gastos_alimentacion.almuerzo + 
                gastos_alimentacion.merienda + 
                gastos_alimentacion.cena + 
                gastos_alimentacion.otros)

    @staticmethod
    def calcular_gastos_etapa(etapa: Etapa, consumo_medio: float, precio_combustible: float) -> GastosEtapa:
        gasto_combustible = PresupuestoService.calcular_gasto_combustible(
            etapa.kilometros, consumo_medio, precio_combustible
        )
        total_alimentacion = PresupuestoService.calcular_total_alimentacion(etapa.gastos_alimentacion)
        
        total_etapa = (
            gasto_combustible +
            etapa.gasto_alojamiento +
            total_alimentacion +
            etapa.gasto_peajes +
            etapa.gastos_actividades +
            etapa.gastos_extra
        )

        return GastosEtapa(
            origen=etapa.origen,
            destino=etapa.destino,
            fecha=etapa.fecha,
            kilometros=etapa.kilometros,
            gasto_combustible=gasto_combustible,
            gasto_alojamiento=etapa.gasto_alojamiento,
            gastos_alimentacion=total_alimentacion,
            gasto_peajes=etapa.gasto_peajes,
            gastos_actividades=etapa.gastos_actividades,
            gastos_extra=etapa.gastos_extra,
            total_etapa=total_etapa
        )

    @staticmethod
    def calcular_total_equipacion(equipacion) -> float:
        return sum(getattr(equipacion, attr) for attr in equipacion.__fields__)

    @staticmethod
    def calcular_total_mantenimiento(mantenimiento) -> float:
        return sum(getattr(mantenimiento, attr) for attr in mantenimiento.__fields__)

    @staticmethod
    def calcular_presupuesto(request: PresupuestoRequest) -> PresupuestoResponse:
        # Calcular gastos por etapa
        desglose_etapas = [
            PresupuestoService.calcular_gastos_etapa(
                etapa, request.consumo_medio, request.precio_combustible
            )
            for etapa in request.etapas
        ]

        # Calcular totales
        total_etapas = sum(etapa.total_etapa for etapa in desglose_etapas)
        total_equipacion = PresupuestoService.calcular_total_equipacion(request.equipacion)
        total_mantenimiento = PresupuestoService.calcular_total_mantenimiento(request.mantenimiento)
        
        total_viaje = total_etapas + total_equipacion + total_mantenimiento

        return PresupuestoResponse(
            nombre_viaje=request.nombre_viaje,
            total_viaje=total_viaje,
            desglose_etapas=desglose_etapas,
            total_equipacion=total_equipacion,
            total_mantenimiento=total_mantenimiento,
            detalle_equipacion=request.equipacion,
            detalle_mantenimiento=request.mantenimiento
        ) 