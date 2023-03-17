import httpx
import pytest

from dodo_is_api.connection.synchronous import DodoISAPIConnection


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
def test_get_delivery_vouchers_ok(httpx_mock, faker, dodo_is_api_connection: DodoISAPIConnection, vouchers: list[dict]):
    httpx_mock.add_response(status_code=200, json={'isEndOfListReached': True, 'vouchers': vouchers})
    response_iterator = dodo_is_api_connection.iter_late_delivery_vouchers(
        from_date=faker.date_time(),
        to_date=faker.date_time(),
        units=[],
    )
    assert tuple(response_iterator)[0] == vouchers


def test_get_delivery_vouchers_multiple_pages(httpx_mock, faker, dodo_is_api_connection):
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
