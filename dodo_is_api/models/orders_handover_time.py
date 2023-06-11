from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from .order_sources import OrderSource
from .sales_channels import SalesChannel

__all__ = ('OrderHandoverTime',)


class OrderHandoverTime(BaseModel):
    unit_id: UUID
    unit_name: str
    order_id: UUID
    order_number: str
    sales_channel: SalesChannel
    order_tracking_start_at: datetime
    tracking_pending_time: int
    cooking_time: int
    heated_shelf_time: int
    order_source: OrderSource
