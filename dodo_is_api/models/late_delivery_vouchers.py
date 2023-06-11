from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

__all__ = ('LateDeliveryVoucher',)


class LateDeliveryVoucher(BaseModel):
    order_id: UUID
    order_number: str
    order_accepted_at_local: datetime
    unit_uuid: UUID
    predicted_delivery_time_local: datetime
    order_fulfilment_flag_at_local: datetime | None
    delivery_deadline_local: datetime
    issuer_name: str | None
    courier_staff_id: UUID | None
