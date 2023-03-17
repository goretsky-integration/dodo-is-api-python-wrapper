import httpx
import pytest

from dodo_is_api.connection.http_clients import get_http_client_config, closing_http_client, closing_async_httpx_client


@pytest.mark.parametrize(
    'access_token, country_code',
    [
        ('3S8O3SBNQBWCX4FJOT8Y1RND6XUWRFR8ND23XYZMWULJ7B5WC0', 'kg',),
        ('7ESDYRS8CUHGCYM4DQWEWX7CCG75233O1KN01ZAO0V59KBRRA2', 'ru',),
        ('DXHLY76M7GTOXVPK7Z7X65NTAM3H7MFP0H5ZYMVNG5QNYTWK8Y', 'ee',),
        ('O7CI4K6BK2F3SH9HKNIO9FX32RGCCC0ZYLYKQC82LZVMRFJLAP', 'pl',),
        ('LRQ7V8DGQ3SZG9DNHEOVXD7R60UDTRD1AGCF2A0LN42LLIHBK8', 'kz',),
    ]
)
def test_get_http_client_config(access_token: str, country_code: str):
    expected_config = {
        'base_url': f'https://api.dodois.io/dodopizza/{country_code}/',
        'timeout': 30,
        'headers': {
            'Authorization': f'Bearer {access_token}'
        }
    }
    actual_config = get_http_client_config(access_token=access_token, country_code=country_code, timeout=30)
    assert actual_config == expected_config


@pytest.mark.parametrize(
    'access_token, country_code',
    [
        ('3S8O3SBNQBWCX4FJOT8Y1RND6XUWRFR8ND23XYZMWULJ7B5WC0', 'kg',),
        ('7ESDYRS8CUHGCYM4DQWEWX7CCG75233O1KN01ZAO0V59KBRRA2', 'ru',),
        ('DXHLY76M7GTOXVPK7Z7X65NTAM3H7MFP0H5ZYMVNG5QNYTWK8Y', 'ee',),
        ('O7CI4K6BK2F3SH9HKNIO9FX32RGCCC0ZYLYKQC82LZVMRFJLAP', 'pl',),
        ('LRQ7V8DGQ3SZG9DNHEOVXD7R60UDTRD1AGCF2A0LN42LLIHBK8', 'kz',),
    ]
)
def test_closing_http_client(access_token: str, country_code: str):
    expected_http_client = httpx.Client(
        base_url=f'https://api.dodois.io/dodopizza/{country_code}/',
        timeout=77,
        headers={'Authorization': f'Bearer {access_token}'},
    )
    with closing_http_client(
            access_token=access_token,
            country_code=country_code,
            timeout=77,
    ) as actual_http_client:
        assert actual_http_client.base_url == expected_http_client.base_url
        assert actual_http_client.timeout == expected_http_client.timeout
        assert actual_http_client.headers == expected_http_client.headers


@pytest.mark.parametrize(
    'access_token, country_code',
    [
        ('3S8O3SBNQBWCX4FJOT8Y1RND6XUWRFR8ND23XYZMWULJ7B5WC0', 'kg',),
        ('7ESDYRS8CUHGCYM4DQWEWX7CCG75233O1KN01ZAO0V59KBRRA2', 'ru',),
        ('DXHLY76M7GTOXVPK7Z7X65NTAM3H7MFP0H5ZYMVNG5QNYTWK8Y', 'ee',),
        ('O7CI4K6BK2F3SH9HKNIO9FX32RGCCC0ZYLYKQC82LZVMRFJLAP', 'pl',),
        ('LRQ7V8DGQ3SZG9DNHEOVXD7R60UDTRD1AGCF2A0LN42LLIHBK8', 'kz',),
    ]
)
@pytest.mark.asyncio
async def test_closing_async_http_client(access_token: str, country_code: str):
    expected_http_client = httpx.AsyncClient(
        base_url=f'https://api.dodois.io/dodopizza/{country_code}/',
        timeout=77,
        headers={'Authorization': f'Bearer {access_token}'},
    )
    async with closing_async_httpx_client(
            access_token=access_token,
            country_code=country_code,
            timeout=77,
    ) as actual_http_client:
        assert actual_http_client.base_url == expected_http_client.base_url
        assert actual_http_client.timeout == expected_http_client.timeout
        assert actual_http_client.headers == expected_http_client.headers
