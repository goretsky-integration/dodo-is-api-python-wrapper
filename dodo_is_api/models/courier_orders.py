from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from .delivery_transport_names import DeliveryTransportName

__all__ = ('CourierOrder',)


class CourierOrder(BaseModel):
    courier_staff_id: UUID
    delivery_time: int
    delivery_transport_name: DeliveryTransportName
    handed_over_to_delivery_at: datetime
    handed_over_to_delivery_at_local: datetime
    heated_shelf_time: int
    is_false_delivery: bool
    is_problematic_delivery: bool
    order_assembly_average_time: int
    order_fulfilment_flag_at: datetime | None
    order_id: UUID
    order_number: str
    predicted_delivery_time: int
    problematic_delivery_reason: str
    trip_orders_count: int
    unit_uuid: UUID
    unit_name: str
    was_late_delivery_voucher_given: bool
