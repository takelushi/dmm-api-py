"""DMM WebAPI client.

https://affiliate.dmm.com/api/guide/
"""

from typing import Any, Dict

import requests

API_BASE_URL = 'https://api.dmm.com/affiliate/'


class DMMApiClient:
    """DMM WebAPI client class.

    Attributes:
        api_id (str): API ID.
        affiliate_id (str): Affiliate ID.
        api_version: (str): API version (default is 'v3').
        default_req_args (dict): Request arguments. Defaults to {}.
    """

    api_id: str
    affiliate_id: str
    api_version: str
    default_req_args: dict

    def __init__(self,
                 api_id: str,
                 affiliate_id: str,
                 default_req_args: dict = None) -> None:
        """Init.

        Args:
            api_id (str): API ID.
            affiliate_id (str): Affiliate ID.
            default_req_args (dict, optional): Request arguments.
                                               Defaults to {}.
        """
        self.api_id = api_id
        self.affiliate_id = affiliate_id
        self.api_version = 'v3'
        self.default_req_args = default_req_args if default_req_args else {}

    def _get_common_params(self) -> dict:
        """Get common parameters for request.

        Returns:
            dict: Common parameters.
        """
        return {
            'api_id': self.api_id,
            'affiliate_id': self.affiliate_id,
        }

    def _get_url(self, path: str) -> str:
        """Get API URL.

        Args:
            path (str): API path.

        Returns:
            str: API URL.
        """
        return f'{API_BASE_URL}{self.api_version}/{path}'

    def _request_get(self,
                     path: str,
                     params: Dict[str, Any] = None,
                     req_args: Dict[str, Any] = None) -> requests.Response:
        """Request with GET method.

        Args:
            path (str): API path.
            params (dict, optional): Request body.

        Returns:
            requests.Response: HTTP response.
        """
        args = self.default_req_args
        req_params = self._get_common_params()

        if req_args:
            args.update(req_args)

        if params:
            req_params.update(params)

        return requests.get(self._get_url(path), params=req_params, **args)

    def get_item_list(self,
                      site: str,
                      service: str = None,
                      floor: str = None,
                      hits: int = 20,
                      offset: int = 1,
                      sort: str = None,
                      keyword: str = None,
                      cid: str = None,
                      article: str = None,
                      article_id: str = None,
                      gte_date: str = None,
                      lte_date: str = None,
                      mono_stock: str = None,
                      output: str = 'json',
                      req_args: Dict[str, Any] = None) -> requests.Response:
        """Search actress API."""
        params = {
            'site': site,
            'service': service,
            'floor': floor,
            'hits': hits,
            'offset': offset,
            'sort': sort,
            'keyword': keyword,
            'cid': cid,
            'article': article,
            'article_id': article_id,
            'gte_date': gte_date,
            'lte_date': lte_date,
            'mono_stock': mono_stock,
            'output': output,
        }

        return self._request_get('ItemList', params=params, req_args=req_args)

    def get_floor(self,
                  output: str = 'json',
                  req_args: Dict[str, Any] = None) -> requests.Response:
        """Get floor list API."""
        params = {'output': output}
        return self._request_get('FloorList', params=params, req_args=req_args)

    def search_actress(self,
                       initial: str = None,
                       actress_id: str = None,
                       keyword: str = None,
                       gte_bust: int = None,
                       lte_bust: int = None,
                       gte_waist: int = None,
                       lte_waist: int = None,
                       gte_hip: int = None,
                       lte_hip: int = None,
                       gte_height: int = None,
                       lte_height: int = None,
                       gte_birthday: str = None,
                       lte_birthday: str = None,
                       hits: int = 20,
                       offset: int = 1,
                       sort: str = None,
                       output: str = 'json',
                       req_args: Dict[str, Any] = None) -> requests.Response:
        """Search actress API."""
        params = {
            'initial': initial,
            'actress_id': actress_id,
            'keyword': keyword,
            'gte_bust': gte_bust,
            'lte_bust': lte_bust,
            'gte_waist': gte_waist,
            'lte_waist': lte_waist,
            'gte_hip': gte_hip,
            'lte_hip': lte_hip,
            'gte_height': gte_height,
            'lte_height': lte_height,
            'gte_birthday': gte_birthday,
            'lte_birthday': lte_birthday,
            'hits': hits,
            'offset': offset,
            'sort': sort,
            'output': output,
        }

        return self._request_get('ActressSearch',
                                 params=params,
                                 req_args=req_args)

    def search_genre(self,
                     floor_id: str,
                     initial: str = None,
                     hits: int = 20,
                     offset: int = 1,
                     output: str = 'json',
                     genre_id: str = None,
                     req_args: Dict[str, Any] = None) -> requests.Response:
        """Search genre API."""
        params = {
            'floor_id': floor_id,
            'initial': initial,
            'hits': hits,
            'offset': offset,
            'output': output,
            'genre_id': genre_id,
        }

        return self._request_get('GenreSearch',
                                 params=params,
                                 req_args=req_args)

    def search_maker(self,
                     floor_id: str,
                     initial: str = None,
                     hits: int = 20,
                     offset: int = 1,
                     output: str = 'json',
                     req_args: Dict[str, Any] = None) -> requests.Response:
        """Search maker API."""
        params = {
            'floor_id': floor_id,
            'initial': initial,
            'hits': hits,
            'offset': offset,
            'output': output,
        }
        return self._request_get('MakerSearch',
                                 params=params,
                                 req_args=req_args)

    def search_series(self,
                      floor_id: str,
                      initial: str = None,
                      hits: int = 20,
                      offset: int = 1,
                      output: str = 'json',
                      req_args: Dict[str, Any] = None) -> requests.Response:
        """Search series API."""
        params = {
            'floor_id': floor_id,
            'initial': initial,
            'hits': hits,
            'offset': offset,
            'output': output,
        }

        return self._request_get('SeriesSearch',
                                 params=params,
                                 req_args=req_args)

    def search_author(self,
                      floor_id: str,
                      initial: str = None,
                      hits: int = 20,
                      offset: int = 1,
                      output: str = 'json',
                      req_args: Dict[str, Any] = None) -> requests.Response:
        """Search author API."""
        params = {
            'floor_id': floor_id,
            'initial': initial,
            'hits': hits,
            'offset': offset,
            'output': output,
        }

        return self._request_get('AuthorSearch',
                                 params=params,
                                 req_args=req_args)
