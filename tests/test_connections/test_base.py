from typing import Iterable
from uuid import UUID

import pytest

from dodo_is_api.connection.base import concatenate_uuids


@pytest.mark.parametrize(
    'uuids',
    [
        [],
        tuple(),
        set(),
        {},
        frozenset(),
    ]
)
def test_concatenate_empty_uuids_collections(uuids: Iterable[UUID]):
    assert concatenate_uuids(uuids) == ''


@pytest.mark.parametrize(
    'uuids, join_symbol, expected',
    [
        (
                (
                        UUID('a657beac-d5a3-45fb-9fd6-f96758ffd7f3'),
                        UUID('75d34bc8-4353-4e80-a8f8-d9bcfa114918'),
                        UUID('5c63287f-a93a-4783-99a1-f709a6e0274f'),
                ),
                ',',
                'a657beacd5a345fb9fd6f96758ffd7f3,75d34bc843534e80a8f8d9bcfa114918,5c63287fa93a478399a1f709a6e0274f',
        ),
        (
                (
                        UUID('60527616-aa66-4a24-9ea0-b74751a082f4'),
                        UUID('ca6b3535-ba23-4da2-b86d-3308ae4a3241'),
                        UUID('96addcd5-c414-4ca6-be82-834aef501a0e'),
                ),
                '-',
                '60527616aa664a249ea0b74751a082f4-ca6b3535ba234da2b86d3308ae4a3241-96addcd5c4144ca6be82834aef501a0e',
        ),
        (
                (
                        UUID('60527616-aa66-4a24-9ea0-b74751a082f4'),
                        UUID('ca6b3535-ba23-4da2-b86d-3308ae4a3241'),
                        UUID('96addcd5-c414-4ca6-be82-834aef501a0e'),
                ),
                ' ',
                '60527616aa664a249ea0b74751a082f4 ca6b3535ba234da2b86d3308ae4a3241 96addcd5c4144ca6be82834aef501a0e',
        ),
    ]
)
def test_concatenate_uuids_with_different_separators(uuids: Iterable[UUID], join_symbol: str, expected: str):
    assert concatenate_uuids(uuids, join_symbol=join_symbol) == expected
