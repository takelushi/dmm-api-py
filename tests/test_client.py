"""Test client."""

import os

from dmm_api.client import DMMApiClient

API_ID = os.environ['DMM_API_ID']
AFFILIATE_ID = os.environ['DMM_AFFILIATE_ID']


class TestDMMApiClient:
    """Test DMMApiClient."""

    def test_init(self) -> None:
        """Test __init__()."""
        client = DMMApiClient(API_ID, AFFILIATE_ID)
        assert isinstance(client, DMMApiClient)

    def test_get_item_list(self) -> None:
        """Test get_item_list()."""
        client = DMMApiClient(API_ID, AFFILIATE_ID)
        res = client.get_item_list('DMM.com', hits=1)
        res.raise_for_status()
        res_body = res.json()
        assert res_body['result']['status'] == 200
        assert isinstance(res_body['result']['items'], list)

        res = client.get_item_list('FANZA',
                                   service='digital',
                                   floor='videoa',
                                   hits=1)
        res.raise_for_status()
        res_body = res.json()
        assert res_body['result']['status'] == 200
        assert isinstance(res_body['result']['items'], list)

    def test_get_floor(self) -> None:
        """Test get_floor()."""
        client = DMMApiClient(API_ID, AFFILIATE_ID)
        res = client.get_floor()
        res.raise_for_status()
        res_body = res.json()
        assert isinstance(res_body['result']['site'], list)

    def test_search_actress(self) -> None:
        """Test search_actress()."""
        client = DMMApiClient(API_ID, AFFILIATE_ID)
        res = client.search_actress(hits=1)
        res.raise_for_status()
        res_body = res.json()
        assert res_body['result']['status'] == '200'
        assert isinstance(res_body['result']['actress'], list)

    def test_search_genre(self) -> None:
        """Test search_actress()."""
        client = DMMApiClient(API_ID, AFFILIATE_ID)
        res = client.search_genre(43, hits=1)
        res.raise_for_status()
        res_body = res.json()
        assert res_body['result']['status'] == '200'
        assert isinstance(res_body['result']['genre'], list)

    def test_search_maker(self) -> None:
        """Test search_actress()."""
        client = DMMApiClient(API_ID, AFFILIATE_ID)
        res = client.search_maker(43, hits=1)
        res.raise_for_status()
        res_body = res.json()
        assert res_body['result']['status'] == '200'
        assert isinstance(res_body['result']['maker'], list)

    def test_search_series(self) -> None:
        """Test search_actress()."""
        client = DMMApiClient(API_ID, AFFILIATE_ID)
        res = client.search_series(43, hits=1)
        res.raise_for_status()
        res_body = res.json()
        assert res_body['result']['status'] == '200'
        assert isinstance(res_body['result']['series'], list)

    def test_search_author(self) -> None:
        """Test search_actress()."""
        client = DMMApiClient(API_ID, AFFILIATE_ID)
        res = client.search_author(27, hits=1)
        res.raise_for_status()
        res_body = res.json()
        assert res_body['result']['status'] == '200'
        assert isinstance(res_body['result']['author'], list)
