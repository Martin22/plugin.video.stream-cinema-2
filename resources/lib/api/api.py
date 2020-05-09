"""
    Stream Cinema backend API.
"""

import requests

from resources.lib.const import ENDPOINT
from resources.lib.utils.kodiutils import replace_url_params, common_headers


class API(object):
    def __init__(self, plugin_version, uuid, api_url):
        self._api_url = api_url
        self._plugin_version = plugin_version
        self._uuid = uuid

    def media_filter(self, collection, filter_name, value):
        url = replace_url_params(ENDPOINT.FILTER, collection, filter_name, value)
        return self._get(url)

    @staticmethod
    def _build_url(*args):
        return '/'.join(args)

    def get(self, url):
        return self._get(url)

    def _get(self, url_path):
        sanitized_api_path = self._api_url.strip('/')
        sanitized_url_path = url_path.strip('/api')
        return requests.get(
            '{0}/{1}/'.format(sanitized_api_path, sanitized_url_path),
            headers=common_headers(),
        )

    def popular_media(self, collection):
        url = replace_url_params(ENDPOINT.POPULAR, collection)
        return self._get(url)

    def media_played(self, collection, media_id):
        url = replace_url_params(ENDPOINT.MEDIA_PLAYED, collection, media_id)
        return self._get(url)
