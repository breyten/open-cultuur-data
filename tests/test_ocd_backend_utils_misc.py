import os
import sys
import re
from pprint import pprint
from StringIO import StringIO

import mock
from mock import MagicMock
from nose.tools import raises

import ocd_backend
from ocd_backend.utils.misc import load_sources_config


def test_load_sources_config_filename():
    sources = load_sources_config('ocd_backend/sources.json')
    assert isinstance(sources, list)


def test_load_sources_config_open_file():
    with open('ocd_backend/sources.json') as json_file:
        sources = load_sources_config(json_file)
        assert isinstance(sources, list)
