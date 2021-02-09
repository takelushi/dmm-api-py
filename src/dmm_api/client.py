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

    def get_item_list(  # noqa: CFQ002
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

    def get_floor(self,
                  output: Optional[str] = 'json',
                  **kwargs: Any) -> requests.Response:
        """Get floor list API.

        Args:
            output (str, optional): Output format. Defaults to 'json'.
            kwargs (Any): Anther parameters.

        Returns:
            requests.Response: Response.
        """
        params = {'output': output}
        return self._request_get('FloorList', params=params, **kwargs)

    def search_actress(  # noqa: CFQ002
            self,
            initial: Optional[str] = None,
            actress_id: Optional[str] = None,
            keyword: Optional[str] = None,
            gte_bust: Optional[int] = None,
            lte_bust: Optional[int] = None,
            gte_waist: Optional[int] = None,
            lte_waist: Optional[int] = None,
            gte_hip: Optional[int] = None,
            lte_hip: Optional[int] = None,
            gte_height: Optional[int] = None,
            lte_height: Optional[int] = None,
            gte_birthday: Optional[str] = None,
            lte_birthday: Optional[str] = None,
            hits: Optional[int] = 20,
            offset: Optional[int] = 1,
            sort: Optional[str] = None,
            output: Optional[str] = 'json',
            **kwargs: Any) -> requests.Response:
        """Search actress API.

        Args:
            initial (str, optional): Initial.
            actress_id (str, optional): Actress ID.
            keyword (str, optional): Keyword.
            gte_bust (int, optional): Bust filter (greater than).
            lte_bust (int, optional): Bust filter (letter than).
            gte_waist (int, optional): Waist filter (greater than).
            lte_waist (int, optional): Waist filter (letter than).
            gte_hip (int, optional): Hip filter (greater than).
            lte_hip (int, optional): Hip filter (letter than).
            gte_height (int, optional): Height filter (greater than).
            lte_height (int, optional): Height filter (letter than).
            gte_birthday (str, optional): Birthday filter (greater than).
            lte_birthday (str, optional): Birthday filter (letter than).
            hits (int, optional): Max result count. Defaults to 20.
            offset (int, optional): Offset. Defaults to 1.
            sort (str, optional): Sort.
            output (str, optional): Output format. Defaults to 'json'.
            kwargs (Any): Anther parameters.

        Returns:
            requests.Response: Response.
        """
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

        return self._request_get('ActressSearch', params=params, **kwargs)

    def search_genre(  # noqa: CFQ002
            self,
            floor_id: int,
            initial: Optional[str] = None,
            hits: Optional[int] = 20,
            offset: Optional[int] = 1,
            output: Optional[str] = 'json',
            genre_id: Optional[str] = None,
            **kwargs: Any) -> requests.Response:
        """Search genre API.

        Args:
            floor_id (int): Floor ID.
            initial (str, optional): Initial.
            hits (int, optional): Max result count. Defaults to 20.
            offset (int, optional): Offset. Defaults to 1.
            output (str, optional): Output format. Defaults to 'json'.
            genre_id (str, optional): Genre ID.
            kwargs (Any): Anther parameters.

        Returns:
            requests.Response: Response.
        """
        params = {
            'floor_id': floor_id,
            'initial': initial,
            'hits': hits,
            'offset': offset,
            'output': output,
            'genre_id': genre_id,
        }

        return self._request_get('GenreSearch', params=params, **kwargs)

    def search_maker(  # noqa: CFQ002
            self,
            floor_id: int,
            initial: Optional[str] = None,
            hits: Optional[int] = 20,
            offset: Optional[int] = 1,
            output: Optional[str] = 'json',
            **kwargs: Any) -> requests.Response:
        """Search maker API.

        Args:
            floor_id (int): Floor ID.
            initial (str, optional): Initial.
            hits (int, optional): Max result count. Defaults to 20.
            offset (int, optional): Offset. Defaults to 1.
            output (str, optional): Output format. Defaults to 'json'.
            kwargs (Any): Anther parameters.

        Returns:
            requests.Response: Response.
        """
        params = {
            'floor_id': floor_id,
            'initial': initial,
            'hits': hits,
            'offset': offset,
            'output': output,
        }
        return self._request_get('MakerSearch', params=params, **kwargs)

    def search_series(  # noqa: CFQ002
            self,
            floor_id: int,
            initial: Optional[str] = None,
            hits: Optional[int] = 20,
            offset: Optional[int] = 1,
            output: Optional[str] = 'json',
            **kwargs: Any) -> requests.Response:
        """Search series API.

        Args:
            floor_id (int): Floor ID.
            initial (str, optional): Initial.
            hits (int, optional): Max result count. Defaults to 20.
            offset (int, optional): Offset. Defaults to 1.
            output (str, optional): Output format. Defaults to 'json'.
            kwargs (Any): Anther parameters.

        Returns:
            requests.Response: Response.
        """
        params = {
            'floor_id': floor_id,
            'initial': initial,
            'hits': hits,
            'offset': offset,
            'output': output,
        }

        return self._request_get('SeriesSearch', params=params, **kwargs)

    def search_author(  # noqa: CFQ002
            self,
            floor_id: int,
            initial: Optional[str] = None,
            hits: Optional[int] = 20,
            offset: Optional[int] = 1,
            output: Optional[str] = 'json',
            **kwargs: Any) -> requests.Response:
        """Search author API.

        Args:
            floor_id (int): Floor ID.
            initial (str, optional): Initial.
            hits (int, optional): Max result count. Defaults to 20.
            offset (int, optional): Offset. Defaults to 1.
            output (str, optional): Output format. Defaults to 'json'.
            kwargs (Any): Anther parameters.

        Returns:
            requests.Response: Response.
        """
        params = {
            'floor_id': floor_id,
            'initial': initial,
            'hits': hits,
            'offset': offset,
            'output': output,
        }

        return self._request_get('AuthorSearch', params=params, **kwargs)
