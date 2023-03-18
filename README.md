# 🍕 Dodo IS API Wrapper

---
<p align="center">
<a href="https://github.com/goretsky-integration/dodo-is-api-python-wrapper/actions/workflows/unittest.yaml">
<img src="https://github.com/goretsky-integration/dodo-is-api-python-wrapper/actions/workflows/unittest.yaml/badge.svg" alt="Test badge">
</a>
<img src="https://img.shields.io/badge/python-3.11-brightgreen" alt="python">
</p>

#### 📝 [Changelog](./CHANGELOG.md) is here.

### 🧪 Usage:

```python
import datetime
from uuid import UUID

from dodo_is_api.connection import DodoISAPIConnection
from dodo_is_api.connection.http_clients import closing_http_client
from dodo_is_api.mappers import map_late_delivery_voucher_dto

access_token = 'my-token'
country_code = 'kg'

units = [UUID('e0ce0423-3064-4e04-ad3e-39906643ef14'), UUID('bd09b0a8-147d-46f7-8908-874f5f59c9a2')]
from_date = datetime.datetime(year=2023, month=3, day=16)
to_date = datetime.datetime(year=2023, month=3, day=17)

with closing_http_client(access_token=access_token, country_code=country_code) as http_client:
    dodo_is_api_connection = DodoISAPIConnection(http_client=http_client)

    # it will handle pagination for you
    for late_delivery_vouchers in dodo_is_api_connection.iter_late_delivery_vouchers(
            from_date=from_date,
            to_date=to_date,
            units=units
    ):
        # map to dataclass DTO if you need
        late_delivery_voucher_dtos = [
            map_late_delivery_voucher_dto(late_delivery_voucher)
            for late_delivery_voucher in late_delivery_vouchers
        ]
        ...
```
