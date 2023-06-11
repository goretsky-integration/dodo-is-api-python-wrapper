from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from .channel_stop_types import ChannelStopType
from .sales_channels import SalesChannel

__all__ = (
    'StopSale',
    'StopSaleByProduct',
    'StopSaleByIngredient',
    'StopSaleBySalesChannel',
)


class StopSale(BaseModel):
    id: UUID
    unit_uuid: UUID
    unit_name: str
    reason: str
    started_at: datetime
    ended_at: datetime | None
    stopped_by_user_id: UUID
    resumed_by_user_id: UUID | None


class StopSaleBySalesChannel(StopSale):
    sales_channel_name: SalesChannel
    channel_stop_type: ChannelStopType


class StopSaleByIngredient(StopSale):
    ingredient_name: str


class StopSaleByProduct(StopSale):
    product_name: str
