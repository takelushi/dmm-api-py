"""DMM WebAPI client.

https://affiliate.dmm.com/api/guide/
"""

from typing import Any, Dict, Optional

import requests

API_BASE_URL = 'https://api.dmm.com/affiliate/'


class DMMApiClient:
    """DMM WebAPI client class."""

    def __init__(self, api_id: str, affiliate_id: str) -> None:
        """Initialize client.

        Args:
            api_id (str): API ID.
            affiliate_id (str): Affiliate ID.
        """
        self.api_id = api_id
        self.affiliate_id = affiliate_id
        self.api_version = 'v3'

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
                     **kwargs: Any) -> requests.Response:
        """Request with GET method.

        Args:
            path (str): API path.
            params (Dict[str, Any], optional): Request body.
            kwargs (Any): Another parameters.

        Returns:
            requests.Response: HTTP response.
        """
        req_params = self._get_common_params()

        if params:
            req_params.update(params)

        return requests.get(self._get_url(path), params=req_params, **kwargs)

    def get_item_list(  # noqaL CFQ002
        self,
        site: str,
        service: Optional[str] = None,
        floor: Optional[str] = None,
        hits: Optional[int] = 20,
        offset: Optional[int] = 1,
        sort: Optional[str] = None,
        keyword: Optional[str] = None,
        cid: Optional[str] = None,
        article: Optional[str] = None,
        article_id: Optional[str] = None,
        gte_date: Optional[str] = None,
        lte_date: Optional[str] = None,
        mono_stock: Optional[str] = None,
        output: Optional[str] = 'json',
        **kwargs: Any,
    ) -> requests.Response:
        """Search actress API.

        Args:
            site (str): 'DMM.com' or 'FANZA'.
            service (str, optional): Service code.
            floor (str, optional): Floor code.
            hits (int, optional): Max result count. Defaults to 20.
            offset (int, optional): Offset. Defaults to 1.
            sort (str, optional): Sort.
            keyword (str, optional): Keyword.
            cid (str, optional): Content ID.
            article (str, optional): Search category.
            article_id (str, optional): Search ID.
            gte_date (str, optional): Release date (greater than).
            lte_date (str, optional): Release date (letter than).
            mono_stock (str, optional): Stock status.
            output (str, optional): Output format. Defaults to 'json'.
            kwargs (Any): Anther parameters.

        Returns:
            requests.Response: Response.
        """
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

        return self._request_get('ItemList', params=params, **kwargs)
