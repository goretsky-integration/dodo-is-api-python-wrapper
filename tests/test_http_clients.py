import httpx
import pytest

from connection.http_clients import get_http_client_config, closing_http_client, closing_async_httpx_client


@pytest.mark.parametrize(
    'country_code',
    [
        'kg',
        'ru',
        'ee',
        'pl',
        'kz',
    ]
)
def test_get_http_client_config(country_code: str):
    expected_config = {
        'base_url': f'https://api.dodois.io/dodopizza/{country_code}/',
        'timeout': 30,
    }
    actual_config = get_http_client_config(country_code=country_code, timeout=30)
    assert actual_config == expected_config


@pytest.mark.parametrize(
    'country_code',
    [
        'kg',
        'ru',
        'ee',
        'pl',
        'kz',
    ]
)
def test_closing_http_client(country_code: str):
    expected_http_client = httpx.Client(
        base_url=f'https://api.dodois.io/dodopizza/{country_code}/',
        timeout=77,
    )
    with closing_http_client(country_code=country_code, timeout=77) as actual_http_client:
        assert actual_http_client.base_url == expected_http_client.base_url
        assert actual_http_client.timeout == expected_http_client.timeout


@pytest.mark.parametrize(
    'country_code',
    [
        'kg',
        'ru',
        'ee',
        'pl',
        'kz',
    ]
)
@pytest.mark.asyncio
async def test_closing_async_http_client(country_code: str):
    expected_http_client = httpx.AsyncClient(
        base_url=f'https://api.dodois.io/dodopizza/{country_code}/',
        timeout=77,
    )
    async with closing_async_httpx_client(country_code=country_code, timeout=77) as actual_http_client:
        assert actual_http_client.base_url == expected_http_client.base_url
        assert actual_http_client.timeout == expected_http_client.timeout
