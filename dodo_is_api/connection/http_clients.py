import contextlib

import httpx

__all__ = ('get_http_client_config',)


def get_http_client_config(*, country_code: str, timeout: int = 60) -> dict:
    """Construct config for httpx.Client or httpx.AsyncClient.

    Args:
        country_code: country code defined in ISO 3166.
        timeout: HTTP timeout.

    Returns:
        Dictionary config.
    """
    return {
        'base_url': f'https://api.dodois.io/dodopizza/{country_code}/',
        'timeout': timeout,
    }
