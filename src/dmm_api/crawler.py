"""DMM WebAPI crawler."""

from typing import Callable, Optional

from dmm_api.common import get_dict_value


class Crawler:
    """DMM WebAPI crawler."""

    api_func: Callable
    keys: list
    params: dict
    hits: int
    offset: int
    limit: Optional[int]
    records: dict
    records_idx: int

    def __init__(self,
                 api_func: Callable,
                 keys: list,
                 params: dict,
                 hits: int = 100,
                 offset: int = 1,
                 limit: int = None) -> None:
        """Init.

        Args:
            api_func (Callable): Target api.
            keys (list): Records keys.
            params (dict): Request parameters.
            hits (int, optional): Count per fetch. Defaults to 100.
            offset (int, optional): Offset. Defaults to 1.
            limit (int, optional): Count limit. Defaults to None.
        """
        self.api_func = api_func  # type: ignore
        self.keys = keys
        self.params = params
        self.hits = hits
        self.offset = offset
        self.limit = limit

        if self.limit is not None and self.limit < self.hits:
            self.hits = self.limit

        self._update_records()

    def __iter__(self):
        """Iterate."""
        return self

    def __next__(self):
        """Next."""
        if self.records_idx >= len(self.records):
            self.offset += self.hits
            if self.limit < self.offset:
                raise StopIteration()
            self._update_records()

        self.records_idx += 1
        return self.records[self.records_idx - 1]

    def _update_records(self) -> None:
        """Update records."""
        res = self.api_func(**self.params, hits=self.hits, offset=self.offset)
        res.raise_for_status()
        d = res.json()
        status_code = d['result']['status']
        if str(status_code) != '200':
            raise StopIteration(f'Status code is {status_code}')

        # result_count = d['result']['result_count']
        # if result_count == 0:
        #     raise StopIteration()

        if self.limit is None:
            self.limit = int(d['result']['total_count'])

        self.records = get_dict_value(d, self.keys)
        self.records_idx = 0
