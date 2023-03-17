from typing import Iterable
from uuid import UUID


def concatenate_uuids(uuids: Iterable[UUID], join_symbol: str = ',') -> str:
    """Convert UUIDs collection to UUIDs string suitable for Dodo IS API.

    Examples:
         >>> concatenate_uuids([UUID('6ff7d64d-1457-47f2-a396-1174994c1e20'), UUID('e27b64cf-346f-4f69-817c-c8ccd4814826')])
         '6ff7d64d145747f2a3961174994c1e20,e27b64cf346f4f69817cc8ccd4814826'

    Args:
        uuids: collection of UUIDs.
        join_symbol: UUIDs separator symbol.

    Returns:
        Concatenated string with UUIDs in hex format separated by `join_symbol`.
    """
    return join_symbol.join((uuid.hex for uuid in uuids))
