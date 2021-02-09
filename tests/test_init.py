"""Test __init__."""

import toml

import dmm_api
import dmm_api.client
import dmm_api.crawler


def test_version():
    """Test __version."""
    with open('pyproject.toml', 'r') as f:
        pyproject = toml.load(f)
    assert dmm_api.__version__ == pyproject['tool']['poetry']['version']


def test_import():
    """Test import."""
    from dmm_api import DMMApiClient
    assert DMMApiClient == dmm_api.client.DMMApiClient
    from dmm_api import Crawler
    assert Crawler == dmm_api.crawler.Crawler
