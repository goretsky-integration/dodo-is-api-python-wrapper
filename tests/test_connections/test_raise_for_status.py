import httpx
import pytest

from dodo_is_api import exceptions
from dodo_is_api.connection.base import raise_for_status

status_code_to_exception_class = {
    400: exceptions.BadRequestError,
    401: exceptions.UnauthorizedError,
    403: exceptions.ForbiddenError,
    429: exceptions.TooManyRequestsError,
}


@pytest.mark.parametrize(
    'status_code',
    range(200, 300),
)
def test_raise_for_status_ok(status_code: int):
    try:
        raise_for_status(httpx.Response(status_code=status_code))
    except exceptions.DodoISAPIError:
        pytest.fail()


@pytest.mark.parametrize(
    'status_code, exception_class',
    status_code_to_exception_class.items(),
)
def test_raise_for_status_defined_status_codes(status_code: int, exception_class: type[exceptions.DodoISAPIError]):
    with pytest.raises(exception_class):
        raise_for_status(httpx.Response(status_code=status_code))


@pytest.mark.parametrize(
    'status_code',
    [i for i in range(300, 600) if i not in status_code_to_exception_class]
)
def test_raise_for_status_undefined_status_codes(status_code: int):
    with pytest.raises(exceptions.DodoISAPIError) as error:
        raise_for_status(httpx.Response(status_code=status_code))
    assert type(error.value) not in status_code_to_exception_class.values()
