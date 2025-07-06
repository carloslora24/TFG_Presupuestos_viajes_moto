from pydantic import BaseModel, Field
from typing import Dict, List
from datetime import datetime

class GastosAlimentacion(BaseModel):
    desayuno: float = Field(default=0, description="Coste del desayuno")
    almuerzo: float = Field(default=0, description="Coste del almuerzo")
    merienda: float = Field(default=0, description="Coste de la merienda")
    cena: float = Field(default=0, description="Coste de la cena")
    otros: float = Field(default=0, description="Otros gastos de alimentación")

class Etapa(BaseModel):
    origen: str = Field(..., description="Ciudad de origen de la etapa")
    destino: str = Field(..., description="Ciudad de destino de la etapa")
    kilometros: float = Field(..., description="Kilómetros de la etapa")
    fecha: datetime = Field(..., description="Fecha de la etapa")
    velocidad_media: float = Field(default=0, description="Velocidad media estimada en km/h")
    gasto_alojamiento: float = Field(default=0, description="Gasto en alojamiento")
    gastos_alimentacion: GastosAlimentacion = Field(default_factory=GastosAlimentacion)
    gasto_peajes: float = Field(default=0, description="Gasto en peajes")
    gastos_actividades: float = Field(default=0, description="Gastos en actividades")
    gastos_extra: float = Field(default=0, description="Gastos extra")

class EquipacionPiloto(BaseModel):
    casco: float = Field(default=0, description="Coste del casco")
    guantes_invierno: float = Field(default=0, description="Coste de los guantes de invierno")
    guantes_verano: float = Field(default=0, description="Coste de los guantes de verano")
    botas_invierno: float = Field(default=0, description="Coste de las botas de invierno")
    botas_verano: float = Field(default=0, description="Coste de las botas de verano")
    chaqueta_invierno: float = Field(default=0, description="Coste de la chaqueta de invierno")
    chaqueta_verano: float = Field(default=0, description="Coste de la chaqueta de verano")
    pantalon_invierno: float = Field(default=0, description="Coste del pantalón de invierno")
    pantalon_verano: float = Field(default=0, description="Coste del pantalón de verano")
    traje_agua: float = Field(default=0, description="Coste del traje de agua")
    airbag: float = Field(default=0, description="Coste del airbag")

class Mantenimiento(BaseModel):
    revision_previa: float = Field(default=0, description="Coste de la revisión previa")
    revision_posterior: float = Field(default=0, description="Coste de la revisión posterior")
    neumaticos: float = Field(default=0, description="Coste de los neumáticos")
    frenos: float = Field(default=0, description="Coste del mantenimiento de frenos")
    cadena: float = Field(default=0, description="Coste del mantenimiento de la cadena")
    taller: float = Field(default=0, description="Coste de otros servicios de taller")
    otros: float = Field(default=0, description="Otros gastos de mantenimiento")

class PresupuestoRequest(BaseModel):
    nombre_viaje: str = Field(..., description="Nombre del viaje")
    pasajero: bool = Field(default=False, description="Indica si lleva pasajero")
    precio_combustible: float = Field(..., description="Precio medio del combustible por litro")
    consumo_medio: float = Field(..., description="Consumo medio de la moto en L/100km")
    etapas: List[Etapa] = Field(..., description="Lista de etapas del viaje")
    equipacion: EquipacionPiloto = Field(default_factory=EquipacionPiloto)
    mantenimiento: Mantenimiento = Field(default_factory=Mantenimiento)

class GastosEtapa(BaseModel):
    origen: str
    destino: str
    fecha: datetime
    kilometros: float
    gasto_combustible: float
    gasto_alojamiento: float
    gastos_alimentacion: float
    gasto_peajes: float
    gastos_actividades: float
    gastos_extra: float
    total_etapa: float

class PresupuestoResponse(BaseModel):
    nombre_viaje: str
    total_viaje: float
    desglose_etapas: List[GastosEtapa]
    total_equipacion: float
    total_mantenimiento: float
    detalle_equipacion: EquipacionPiloto
    detalle_mantenimiento: Mantenimiento 