import httpx
import pytest

from dodo_is_api.connection.synchronous import DodoISAPIConnection
from dodo_is_api.models import raw as raw_models


@pytest.fixture
def http_client() -> httpx.Client:
    with httpx.Client(base_url='http://test.url') as http_client:
        yield http_client


@pytest.fixture
def dodo_is_api_connection(http_client) -> DodoISAPIConnection:
    return DodoISAPIConnection(http_client=http_client)


@pytest.mark.parametrize(
    'vouchers',
    [
        [],
        [{'hello': 'world'}],
        [{}],
    ]
)
def test_get_delivery_vouchers_ok(httpx_mock, faker,
                                  dodo_is_api_connection: DodoISAPIConnection,
                                  vouchers: list[dict]):
    httpx_mock.add_response(status_code=200, json={
        'isEndOfListReached': True, 'vouchers': vouchers
    })
    response_iterator = dodo_is_api_connection.iter_late_delivery_vouchers(
        from_date=faker.date_time(),
        to_date=faker.date_time(),
        units=[],
    )
    assert tuple(response_iterator)[0] == vouchers


def test_get_delivery_vouchers_multiple_pages(httpx_mock, faker,
                                              dodo_is_api_connection):
    is_end_of_list_reached = False

    def get_response(request: httpx.Request):
        nonlocal is_end_of_list_reached
        if is_end_of_list_reached:
            return httpx.Response(status_code=200, json={
                'isEndOfListReached': True,
                'vouchers': [{'the': 'end'}],
            })
        is_end_of_list_reached = True
        return httpx.Response(status_code=200, json={
            'isEndOfListReached': False,
            'vouchers': [{'hello': 'world'}],
        })

    httpx_mock.add_callback(get_response)

    response_iterator = dodo_is_api_connection.iter_late_delivery_vouchers(
        from_date=faker.date_time(),
        to_date=faker.date_time(),
        units=[],
    )

    assert next(response_iterator) == [{'hello': 'world'}]
    assert next(response_iterator) == [{'the': 'end'}]


@pytest.mark.parametrize(
    'response_json',
    [
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
    ]
)
def test_get_stop_sales_by_sales_channels(
        httpx_mock,
        faker,
        dodo_is_api_connection,
        response_json: raw_models.StopSaleBySalesChannelTypedDict,
):
    httpx_mock.add_response(json={'stopSalesBySalesChannels': [response_json]})
    assert dodo_is_api_connection.get_stop_sales_by_sales_channels(
        from_date=faker.date_time(),
        to_date=faker.date_time(),
        units=[],
    ) == [response_json]


@pytest.mark.parametrize(
    'response_json',
    [
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
    ]
)
def test_get_stop_sales_by_ingredients(
        httpx_mock,
        faker,
        dodo_is_api_connection,
        response_json: raw_models.StopSaleByIngredientTypedDict,
):
    httpx_mock.add_response(json={'stopSalesByIngredients': [response_json]})
    assert dodo_is_api_connection.get_stop_sales_by_ingredients(
        from_date=faker.date_time(),
        to_date=faker.date_time(),
        units=[],
    ) == [response_json]


@pytest.mark.parametrize(
    'response_json',
    [
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
    ]
)
def test_get_stop_sales_by_products(
        httpx_mock,
        faker,
        dodo_is_api_connection,
        response_json: raw_models.StopSaleByIngredientTypedDict,
):
    httpx_mock.add_response(json={'stopSalesByProducts': [response_json]})
    assert dodo_is_api_connection.get_stop_sales_by_products(
        from_date=faker.date_time(),
        to_date=faker.date_time(),
        units=[],
    ) == [response_json]


@pytest.mark.parametrize(
    'response_json',
    [
        {
            'unitId': '000d3a23b0dc80d911e6b24f4a188a9f',
            'unitName': 'Москва 4-1',
            'deliverySales': 4541294,
            'deliveryOrdersCount': 3578,
            'avgDeliveryOrderFulfillmentTime': 1799,
            'avgCookingTime': 696,
            'avgHeatedShelfTime': 167,
            'avgOrderTripTime': 936,
            'lateOrdersCount': 1,
            'ordersWithCourierAppCount': 3425,
            'tripsCount': 3200,
            'tripsDuration': 5305266,
            'couriersShiftsDuration': 7908714,
        },
    ],
)
def test_get_delivery_statistics(
        httpx_mock,
        faker,
        dodo_is_api_connection,
        response_json: raw_models.UnitDeliveryStatisticsTypedDict,
):
    httpx_mock.add_response(json={'unitsStatistics': [response_json]})
    assert dodo_is_api_connection.get_delivery_statistics(
        from_date=faker.date_time(),
        to_date=faker.date_time(),
        units=[],
    ) == [response_json]
