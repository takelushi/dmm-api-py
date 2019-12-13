"""Print floor list."""

import os

from dmm_api import DMMApiClient

API_ID = os.environ.get('DMM_API_ID')
AFFILIATE_ID = os.environ.get('DMM_AFFILIATE_ID')

client = DMMApiClient(API_ID, AFFILIATE_ID)
res = client.get_floor()
print(res.json())
