"""
    # Main routing to go through different menu screens. 
"""
import sys
import uuid

from resources.lib.const import SETTINGS, RENDERER, LANG, STORAGE
from resources.lib.defaults import Defaults
from resources.lib.gui.renderers.dialog_renderer import DialogRenderer
from resources.lib.kodilogging import logger, setup_root_logger
from resources.lib.plugin_url_history import PluginUrlHistory
from resources.lib.settings import settings
from resources.lib.storage.storage import Storage, storage
from resources.lib.stream_cinema import StreamCinema
from resources.lib.utils.kodiutils import get_plugin_url, get_string

provider = Defaults.provider()
api = Defaults.api_cached()
router = Defaults.router()
plugin_url_history = PluginUrlHistory()
stream_cinema = StreamCinema(provider, api, router)


@router.route('/')
def index():
    return stream_cinema.renderers[RENDERER.DIRECTORIES].main_menu()


def run():
    first_run()
    setup_root_logger()
    logger.debug('Entry point ------- ' + str(sys.argv))
    plugin_url_history.add(get_plugin_url())
    return router.run()


def first_run():
    if settings[SETTINGS.UUID] == '':
        settings[SETTINGS.UUID] = uuid.uuid4()
        DialogRenderer.ok(get_string(LANG.NEWS_TITLE), get_string(LANG.NEWS_TEXT))


@router.route('/clear-cache')
def clear_cache():
    del storage[STORAGE.MEDIA_LIST]
    del storage[STORAGE.COLLECTION]
    del storage[STORAGE.PLUGIN_URL_HISTORY]
    del storage[STORAGE.PLUGIN_LAST_URL_ADDED]
    del storage[STORAGE.SERVICE]
