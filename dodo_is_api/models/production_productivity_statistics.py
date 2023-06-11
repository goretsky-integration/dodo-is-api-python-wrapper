from uuid import UUID

from pydantic import BaseModel

__all__ = ('UnitProductionProductivityStatistics',)


class UnitProductionProductivityStatistics(BaseModel):
    unit_id: UUID
    unit_name: str
    labor_hours: float
    sales: float
    sales_per_labor_hour: float
    products_per_labor_hour: float
    average_heated_shelf_time: int
    orders_per_courier_labour_hour: float
    kitchen_speed_percentage: float
