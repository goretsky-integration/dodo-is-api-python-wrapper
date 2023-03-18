import datetime
import uuid
from typing import Any
from uuid import UUID

import pytest

from dodo_is_api import mappers, models
from dodo_is_api.models import raw as raw_models


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


@pytest.mark.parametrize(
    'stop_sale_by_product_raw, stop_sale_by_product_dto',
    [
        (
                {
                    'id': '2ebf62957d0182e411eda0a4d4a34864',
                    'unitId': '000d3a240c719a8711e68abbbc04fd69',
                    'unitName': 'Tallinn-1',
                    'productName': 'Jäätisekokteil "Maasika banaan"',
                    'reason': 'Withdrawal from menu',
                    'startedAt': '2023-01-30T15:48:52',
                    'endedAt': None,
                    'stoppedByUserId': '000d3aaa13e6bb2b11ebde6ad2a8f708',
                    'resumedByUserId': None,
                },
                models.StopSaleByProduct(
                    id=UUID('2ebf62957d0182e411eda0a4d4a34864'),
                    unit_uuid=UUID('000d3a240c719a8711e68abbbc04fd69'),
                    unit_name='Tallinn-1',
                    product_name='Jäätisekokteil "Maasika banaan"',
                    reason='Withdrawal from menu',
                    started_at=datetime.datetime(2023, 1, 30, 15, 48, 52),
                    ended_at=None,
                    stopped_by_user_id=UUID('000d3aaa13e6bb2b11ebde6ad2a8f708'),
                    resumed_by_user_id=None,
                ),
        ),
        (
                {
                    'id': 'fa617e5baecca00e11edbdfe0663c788',
                    'unitId': '000d3a229ab480d111e7ac174322df90',
                    'unitName': 'Tallinn-2',
                    'productName': "Jäätis Hazel-nuttin' but Chocolate Sundae",
                    'reason': 'It run out on defrost',
                    'startedAt': '2023-03-09T00:10:24',
                    'endedAt': '2023-03-13T11:40:20',
                    'stoppedByUserId': '0022487fe9f3bb2811ebc926c8dcd08f',
                    'resumedByUserId': 'a6635fd79244b60c11edc027bf370edf',
                },
                models.StopSaleByProduct(
                    id=UUID('fa617e5baecca00e11edbdfe0663c788'),
                    unit_uuid=UUID('000d3a229ab480d111e7ac174322df90'),
                    unit_name='Tallinn-2',
                    product_name="Jäätis Hazel-nuttin' but Chocolate Sundae",
                    reason='It run out on defrost',
                    started_at=datetime.datetime(2023, 3, 9, 0, 10, 24),
                    ended_at=datetime.datetime(2023, 3, 13, 11, 40, 20),
                    stopped_by_user_id=UUID('0022487fe9f3bb2811ebc926c8dcd08f'),
                    resumed_by_user_id=UUID('a6635fd79244b60c11edc027bf370edf'),
                ),
        ),
        (

                {
                    'id': '8e25311986e8baf811edc40feb55c195',
                    'unitId': '000d3a2bf1aba95511ea00d5a080e033',
                    'unitName': 'Tallinn-3',
                    'productName': 'Jäätis Vanilla Pecan Blondie',
                    'reason': 'It run out at pizzeria',
                    'startedAt': '2023-03-16T17:33:37',
                    'endedAt': None,
                    'stoppedByUserId': '0022487fe9f3bb2c11eca1447bbf3604',
                    'resumedByUserId': None,
                },
                models.StopSaleByProduct(
                    id=UUID('8e25311986e8baf811edc40feb55c195'),
                    unit_uuid=UUID('000d3a2bf1aba95511ea00d5a080e033'),
                    unit_name='Tallinn-3',
                    product_name='Jäätis Vanilla Pecan Blondie',
                    reason='It run out at pizzeria',
                    started_at=datetime.datetime(2023, 3, 16, 17, 33, 37),
                    ended_at=None,
                    stopped_by_user_id=UUID('0022487fe9f3bb2c11eca1447bbf3604'),
                    resumed_by_user_id=None,
                ),
        )
    ]
)
def test_stop_sale_by_product_mapper(
        stop_sale_by_product_raw: raw_models.StopSaleByProductTypedDict,
        stop_sale_by_product_dto: models.StopSaleByProduct,
):
    assert mappers.map_stop_sale_by_product_dto(stop_sale_by_product_raw) == stop_sale_by_product_dto


@pytest.mark.parametrize(
    'stop_sale_by_ingredient_raw, stop_sale_by_ingredient_dto',
    [
        (
                {
                    'id': '8e25311986e8baf711edc40feb50d01b',
                    'unitId': '000d3a2bf1aba95511ea00d5a080e033',
                    'unitName': 'Tallinn-3',
                    'ingredientName': 'Jäätis Vanilla Pecan Blondie ',
                    'reason': 'It run out at pizzeria',
                    'startedAt': '2023-03-16T17:33:37',
                    'endedAt': None,
                    'stoppedByUserId': '0022487fe9f3bb2c11eca1447bbf3604',
                    'resumedByUserId': None,
                },
                models.StopSaleByIngredient(
                    id=UUID('8e25311986e8baf711edc40feb50d01b'),
                    unit_uuid=UUID('000d3a2bf1aba95511ea00d5a080e033'),
                    unit_name='Tallinn-3',
                    ingredient_name='Jäätis Vanilla Pecan Blondie ',
                    reason='It run out at pizzeria',
                    started_at=datetime.datetime(2023, 3, 16, 17, 33, 37),
                    ended_at=None,
                    stopped_by_user_id=UUID('0022487fe9f3bb2c11eca1447bbf3604'),
                    resumed_by_user_id=None,
                ),
        ),
        (
                {
                    'id': 'ca9dc3033f1586be11edb9990930994f',
                    'unitId': '000d3a229ab480d111e7ac174322df90',
                    'unitName': 'Tallinn-2',
                    'ingredientName': 'Siirup postmix Cola Zero / Сироп Кола Зеро',
                    'reason': 'Equipment broke',
                    'startedAt': '2023-03-03T09:57:25',
                    'endedAt': '2023-03-09T21:35:52',
                    'stoppedByUserId': '000d3a23750ca94a11e8041840883175',
                    'resumedByUserId': '000d3a23750ca94a11e8041840883175',
                },
                models.StopSaleByIngredient(
                    id=UUID('ca9dc3033f1586be11edb9990930994f'),
                    unit_uuid=UUID('000d3a229ab480d111e7ac174322df90'),
                    unit_name='Tallinn-2',
                    ingredient_name='Siirup postmix Cola Zero / Сироп Кола Зеро',
                    reason='Equipment broke',
                    started_at=datetime.datetime(2023, 3, 3, 9, 57, 25),
                    ended_at=datetime.datetime(2023, 3, 9, 21, 35, 52),
                    stopped_by_user_id=UUID('000d3a23750ca94a11e8041840883175'),
                    resumed_by_user_id=UUID('000d3a23750ca94a11e8041840883175'),
                ),
        ),
    ]
)
def test_stop_sale_by_ingredient_mapper(
        stop_sale_by_ingredient_raw: raw_models.StopSaleByIngredientTypedDict,
        stop_sale_by_ingredient_dto: models.StopSaleByIngredient,
):
    assert mappers.map_stop_sale_by_ingredient_dto(stop_sale_by_ingredient_raw) == stop_sale_by_ingredient_dto


@pytest.mark.parametrize(
    'stop_sale_by_sales_channel_raw, stop_sale_by_sales_channel_dto',
    [
        (
                {
                    'id': 'fa617e5baecc9fa211edbdc41c461c5a',
                    'unitId': '000d3a229ab480d111e7ac174322df90',
                    'unitName': 'Tallinn-2',
                    'salesChannelName': 'Delivery',
                    'reason': 'Нехватка курьеров',
                    'startedAt': '2023-03-08T17:15:50',
                    'endedAt': '2023-03-08T17:32:58',
                    'stoppedByUserId': '0022487fe9f3bb2811ebc926c8dcd08f',
                    'resumedByUserId': '0022487fe9f3bb2811ebc926c8dcd08f',
                    'channelStopType': 'Complete',
                },
                models.StopSaleBySalesChannel(
                    id=UUID('fa617e5baecc9fa211edbdc41c461c5a'),
                    unit_uuid=UUID('000d3a229ab480d111e7ac174322df90'),
                    unit_name='Tallinn-2',
                    sales_channel_name=models.SalesChannel.DELIVERY,
                    reason='Нехватка курьеров',
                    started_at=datetime.datetime(2023, 3, 8, 17, 15, 50),
                    ended_at=datetime.datetime(2023, 3, 8, 17, 32, 58),
                    stopped_by_user_id=UUID('0022487fe9f3bb2811ebc926c8dcd08f'),
                    resumed_by_user_id=UUID('0022487fe9f3bb2811ebc926c8dcd08f'),
                    channel_stop_type=models.ChannelStopType.COMPLETE,
                ),
        ),
        (
                {
                    'id': 'fa617e5baecc9fa211edbdc41c461c5a',
                    'unitId': '000d3a229ab480d111e7ac174322df90',
                    'unitName': 'Tallinn-2',
                    'salesChannelName': 'Takeaway',
                    'reason': 'Нехватка курьеров',
                    'startedAt': '2023-03-08T17:15:50',
                    'endedAt': None,
                    'stoppedByUserId': '0022487fe9f3bb2811ebc926c8dcd08f',
                    'resumedByUserId': None,
                    'channelStopType': 'Redirection',
                },
                models.StopSaleBySalesChannel(
                    id=UUID('fa617e5baecc9fa211edbdc41c461c5a'),
                    unit_uuid=UUID('000d3a229ab480d111e7ac174322df90'),
                    unit_name='Tallinn-2',
                    sales_channel_name=models.SalesChannel.TAKEAWAY,
                    reason='Нехватка курьеров',
                    started_at=datetime.datetime(2023, 3, 8, 17, 15, 50),
                    ended_at=None,
                    stopped_by_user_id=UUID('0022487fe9f3bb2811ebc926c8dcd08f'),
                    resumed_by_user_id=None,
                    channel_stop_type=models.ChannelStopType.REDIRECTION,
                ),
        ),
        (
                {
                    'id': 'fa617e5baecc9fa211edbdc41c461c5a',
                    'unitId': '000d3a229ab480d111e7ac174322df90',
                    'unitName': 'Tallinn-2',
                    'salesChannelName': 'Dine-in',
                    'reason': 'Нехватка курьеров',
                    'startedAt': '2023-03-08T17:15:50',
                    'endedAt': None,
                    'stoppedByUserId': '0022487fe9f3bb2811ebc926c8dcd08f',
                    'resumedByUserId': None,
                    'channelStopType': 'Complete',
                },
                models.StopSaleBySalesChannel(
                    id=UUID('fa617e5baecc9fa211edbdc41c461c5a'),
                    unit_uuid=UUID('000d3a229ab480d111e7ac174322df90'),
                    unit_name='Tallinn-2',
                    sales_channel_name=models.SalesChannel.DINE_IN,
                    reason='Нехватка курьеров',
                    started_at=datetime.datetime(2023, 3, 8, 17, 15, 50),
                    ended_at=None,
                    stopped_by_user_id=UUID('0022487fe9f3bb2811ebc926c8dcd08f'),
                    resumed_by_user_id=None,
                    channel_stop_type=models.ChannelStopType.COMPLETE,
                ),
        ),
    ],
)
def test_stop_sale_by_sales_channel_mapper(
        stop_sale_by_sales_channel_raw: raw_models.StopSaleBySalesChannelTypedDict,
        stop_sale_by_sales_channel_dto: models.StopSaleBySalesChannel,
):
    assert mappers.map_stop_sale_by_sales_channel_dto(stop_sale_by_sales_channel_raw) == stop_sale_by_sales_channel_dto


@pytest.mark.parametrize(
    'value, expected',
    [
        (
                '2023-03-18T23:14:53',
                datetime.datetime(2023, 3, 18, 23, 14, 53),
        ),
        (
                '2022-12-02:12:12:00',
                datetime.datetime(2022, 12, 2, 12, 12),
        ),
        (
                None, None,
        )
    ]
)
def test_parse_datetime_or_none(value: str | None, expected: datetime.datetime | None):
    assert mappers.parse_to_datetime_or_none(value) == expected


@pytest.mark.parametrize(
    'value, expected',
    [
        (
                '04b18117-66ea-43b2-bda1-dce1b45fa8e5',
                UUID('04b18117-66ea-43b2-bda1-dce1b45fa8e5'),
        ),
        (
                '0c68da0a-640a-4910-8bfa-c71208831e72',
                UUID('0c68da0a-640a-4910-8bfa-c71208831e72'),
        ),
        (
                None, None,
        )
    ]
)
def test_parse_uuid_or_none(value: str | None, expected: UUID | None):
    assert mappers.parse_to_uuid_or_none(value) == expected


@pytest.mark.parametrize(
    'value',
    [
        1234,
        4324.54,
        True,
        False,
        {},
        tuple(),
        [],
    ]
)
def test_parse_datetime_passed_invalid_type(value: Any):
    with pytest.raises(ValueError, match='^Invalid type$'):
        mappers.parse_to_datetime_or_none(value)


@pytest.mark.parametrize(
    'value',
    [
        1234,
        4324.54,
        True,
        False,
        {},
        tuple(),
        [],
    ]
)
def test_parse_uuid_passed_invalid_type(value: Any):
    with pytest.raises(ValueError, match='^Invalid type$'):
        mappers.parse_to_uuid_or_none(value)
