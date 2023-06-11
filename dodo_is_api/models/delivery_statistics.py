from uuid import UUID

from pydantic import BaseModel

__all__ = ('UnitDeliveryStatistics',)


class UnitDeliveryStatistics(BaseModel):
    unit_uuid: UUID
    unit_name: str
    delivery_sales: int
    delivery_orders_count: int
    average_delivery_order_fulfillment_time: int
    average_cooking_time: int
    average_heated_shelf_time: int
    average_order_trip_time: int
    late_orders_count: int
    trips_count: int
    trips_duration: int
    couriers_shifts_duration: int
    orders_with_courier_app_count: int
