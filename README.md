# DMM Affiliate API Client for Python

* **This SDK is unofficial**
* API Guide is [here](https://affiliate.dmm.com/api/guide/).

## Install

```sh
pip install dmm-api
```

## Usage

* [Examples](https://github.com/takelushi/dmm-api-py/tree/master/examples)

```py
import os

from dmm_api import DMMApiClient

API_ID = os.environ.get('DMM_API_ID', '')
AFFILIATE_ID = os.environ.get('DMM_AFFILIATE_ID', '')

client = DMMApiClient(API_ID, AFFILIATE_ID)
res = client.get_floor()
print(res.json())
```

## Supported API list

### v3

* 商品情報 API (ItemList)
* フロア API (FloorList)
* 女優検索 API (ActressSearch)
* ジャンル検索 API (GenreSearch)
* メーカー検索 API (MakerSearch)
* シリーズ検索 API (SeriesSearch)
* 作者検索 API (AuthorSearch)

## For developers

* Setup

   **Require: poetry**

   ```sh
   git clone git@github.com:takelushi/dmm-api-py.git
   cd dmm-api-py
   poetry install
   ```

* Lint and Test

   ```sh
   flake8 src/ tests/
   export API_ID='...'
   export AFFILIATE_ID='...'
   pytestz
   ```

* Build

   ```sh
   poetry build
   ```

* Register PyPI and install.

   ```sh
   poetry publish
   pip --no-cache-dir install --upgrade dmm-api
   ```
