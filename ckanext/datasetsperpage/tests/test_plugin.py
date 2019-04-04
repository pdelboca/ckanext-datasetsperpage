"""Tests for plugin.py."""
# import ckanext.datasetsperpage.plugin as plugin
import ckan.plugins
from ckan.tests.helpers import call_action
from nose.tools import assert_equal


class TestDataSetPerPagePlugin(object):
    """Tests for datasetperpage plugin."""

    @classmethod
    def setup_class(cls):
        """Nose runs this method once to setup our test class."""
        if not ckan.plugins.plugin_loaded('datasetsperpage'):
            ckan.plugins.load('datasetsperpage')

    @classmethod
    def teardown_class(cls):
        """Nose Runs after all the test methods in our class have been run."""
        ckan.plugins.unload('datasetsperpage')

    def test_datasets_per_page_is_editable_runtime(self):
        """Run."""
        configs = call_action('config_option_list')
        assert_equal('ckan.datasets_per_pagess' in configs, True)
