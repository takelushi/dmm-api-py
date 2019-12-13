# DMM Affiliate API Client for Python

* **This SDK is unofficial**
* API Guide is [here](https://affiliate.dmm.com/api/guide/).

## Install

```sh
pip install dmm-api
```

## Usage

```py
import os

from dmm_api import DMMApiClient

API_ID = os.environ.get('DMM_API_ID')
AFFILIATE_ID = os.environ.get('DMM_AFFILIATE_ID')

client = DMMApiClient(API_ID, AFFILIATE_ID)
res = client.get_floor()
print(res.json())

```

## Supported API list

v3

* 商品情報 API (ItemList)
* フロア API (FloorList)
* 女優検索 API (ActressSearch)
* ジャンル検索 API (GenreSearch)
* メーカー検索 API (MakerSearch)
* シリーズ検索 API (SeriesSearch)
* 作者検索 API (AuthorSearch)

## For developers

* Setup

   **Require: pipenv**

   ```she
   git clone git@github.com:takelushi/dmm-api-py.git
   cd dmm-api-py
   pipenv install --dev
   ```

* Build

   ```sh
   python setup.py sdist bdist_wheel
   ```

* Install for development.

   ```sh
   pip install -e .
   ```

* Register PyPI and install.

   ```sh
   # test
   twine upload --repository pypitest dist/*
   pip --no-cache-dir install --upgrade --index-url https://test.pypi.org/simple/ dmm-api

   # production
   twine upload --repository pypi dist/*
   pip --no-cache-dir install --upgrade dmm-api
   ```
