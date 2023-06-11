from uuid import UUID

from pydantic import BaseModel

__all__ = ('UnitOrdersHandoverStatistics',)


class UnitOrdersHandoverStatistics(BaseModel):
    unit_uuid: UUID
    unit_name: str
    average_tracking_pending_time: int
    average_cooking_time: int
    average_heated_shelf_time: int
    average_order_handover_time: int
    orders_count: int
