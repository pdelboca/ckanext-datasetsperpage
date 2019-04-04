import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class DatasetsperpagePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):
        """Add extension templates directory."""
        toolkit.add_template_directory(config, 'templates')

    def update_config_schema(self, schema):
        """Make datasets_per_page editable at runtime."""
        ignore_missing = toolkit.get_validator('ignore_missing')
        is_positive_integer = toolkit.get_validator('is_positive_integer')

        schema.update({
            # This is an existing CKAN core configuration option, we are just
            # making it available to be editable at runtime
            'ckan.datasets_per_page': [ignore_missing, is_positive_integer],
        })

        return schema
