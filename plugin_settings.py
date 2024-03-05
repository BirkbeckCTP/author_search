from events import logic as events_logic
from utils import plugins
from utils.install import update_settings

PLUGIN_NAME = 'Author Search'
DISPLAY_NAME = 'Author Search'
DESCRIPTION = 'Lets staff search for authors across the press.'
AUTHOR = 'Birkbeck Centre for Technology and Publishing'
VERSION = '0.1'
SHORT_NAME = 'author_search'
MANAGER_URL = 'author_search_manager'
JANEWAY_VERSION = "1.5.0"

# Workflow Settings
IS_WORKFLOW_PLUGIN = False


class AuthorSearchPlugin(plugins.Plugin):
    plugin_name = PLUGIN_NAME
    display_name = DISPLAY_NAME
    description = DESCRIPTION
    author = AUTHOR
    short_name = SHORT_NAME
    manager_url = MANAGER_URL
    version = VERSION
    janeway_version = JANEWAY_VERSION
    is_workflow_plugin = IS_WORKFLOW_PLUGIN
    press_wide = True


def install():
    AuthorSearchPlugin.install()


def hook_registry():
    pass


def register_for_events():
    pass