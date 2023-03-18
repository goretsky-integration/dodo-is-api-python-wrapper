import datetime
from uuid import UUID

import pytest

from dodo_is_api import mappers, models


@pytest.mark.parametrize(
    'late_delivery_voucher_raw, late_delivery_voucher_dto',
    [
        (
                {
                    'orderId': '1a710d56b084bc0911edbcf829899a1b',
                    'orderNumber': '95',
                    'orderAcceptedAtLocal': '2023-03-07T16:59:45',
                    'unitId': '000d3a240c719a8711e68abbbc04fd69',
                    'predictedDeliveryTimeLocal': '2023-03-07T17:39:45',
                    'orderFulfilmentFlagAtLocal': '2023-03-07T18:15:43',
                    'deliveryDeadlineLocal': '2023-03-07T17:59:45',
                    'issuerName': 'System',
                    'courierStaffId': '4acab5c63de1b2a911ed04f431217e58',
                },
                models.LateDeliveryVoucher(
                    order_id=UUID('1a710d56-b084-bc09-11ed-bcf829899a1b'), order_number='95',
                    order_accepted_at_local=datetime.datetime(2023, 3, 7, 16, 59, 45),
                    unit_uuid=UUID('000d3a24-0c71-9a87-11e6-8abbbc04fd69'),
                    predicted_delivery_time_local=datetime.datetime(2023, 3, 7, 17, 39, 45),
                    order_fulfilment_flag_at_local=datetime.datetime(2023, 3, 7, 18, 15, 43),
                    delivery_deadline_local=datetime.datetime(2023, 3, 7, 17, 59, 45),
                    issuer_name='System',
                    courier_staff_id=UUID('4acab5c6-3de1-b2a9-11ed-04f431217e58'),
                ),
        ),
        (
                {
                    'orderId': '1a710d56b084bc0911edbcf829899a1b',
                    'orderNumber': '95',
                    'orderAcceptedAtLocal': '2023-03-07T16:59:45',
                    'unitId': '000d3a240c719a8711e68abbbc04fd69',
                    'predictedDeliveryTimeLocal': '2023-03-07T17:39:45',
                    'orderFulfilmentFlagAtLocal': '2023-03-07T18:15:43',
                    'deliveryDeadlineLocal': '2023-03-07T17:59:45',
                    'issuerName': None,
                    'courierStaffId': '4acab5c63de1b2a911ed04f431217e58',
                },
                models.LateDeliveryVoucher(
                    order_id=UUID('1a710d56-b084-bc09-11ed-bcf829899a1b'), order_number='95',
                    order_accepted_at_local=datetime.datetime(2023, 3, 7, 16, 59, 45),
                    unit_uuid=UUID('000d3a24-0c71-9a87-11e6-8abbbc04fd69'),
                    predicted_delivery_time_local=datetime.datetime(2023, 3, 7, 17, 39, 45),
                    order_fulfilment_flag_at_local=datetime.datetime(2023, 3, 7, 18, 15, 43),
                    delivery_deadline_local=datetime.datetime(2023, 3, 7, 17, 59, 45),
                    issuer_name=None,
                    courier_staff_id=UUID('4acab5c6-3de1-b2a9-11ed-04f431217e58'),
                ),
        ),
        (
                {
                    'orderId': '1a710d56b084bc0911edbcf829899a1b',
                    'orderNumber': '95',
                    'orderAcceptedAtLocal': '2023-03-07T16:59:45',
                    'unitId': '000d3a240c719a8711e68abbbc04fd69',
                    'predictedDeliveryTimeLocal': '2023-03-07T17:39:45',
                    'orderFulfilmentFlagAtLocal': None,
                    'deliveryDeadlineLocal': '2023-03-07T17:59:45',
                    'issuerName': None,
                    'courierStaffId': None,
                },
                models.LateDeliveryVoucher(
                    order_id=UUID('1a710d56-b084-bc09-11ed-bcf829899a1b'), order_number='95',
                    order_accepted_at_local=datetime.datetime(2023, 3, 7, 16, 59, 45),
                    unit_uuid=UUID('000d3a24-0c71-9a87-11e6-8abbbc04fd69'),
                    predicted_delivery_time_local=datetime.datetime(2023, 3, 7, 17, 39, 45),
                    order_fulfilment_flag_at_local=None,
                    delivery_deadline_local=datetime.datetime(2023, 3, 7, 17, 59, 45),
                    issuer_name=None,
                    courier_staff_id=None,
                ),
        ),
    ]
)
def test_late_delivery_voucher_mapper(
        late_delivery_voucher_raw: dict,
        late_delivery_voucher_dto: models.LateDeliveryVoucher,
):
    assert mappers.map_late_delivery_voucher_dto(late_delivery_voucher_raw) == late_delivery_voucher_dto
