# vim: set fileencoding=utf-8 :
#
# Copyright (c) 2012 Retresco GmbH
# Copyright (c) 2012 Daniel Truemper <truemped at googlemail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.httputil import HTTPHeaders
from tornado.ioloop import IOLoop


class BaseClient(object):

    def __init__(self, ioloop=None, client_args={}):
        """
        Initialize me.
        """
        self._ioloop = ioloop or IOLoop.instance()
        self._client = AsyncHTTPClient(self._ioloop, **client_args)

    def _get(self, url, headers=None, callback=None):
        """
        A async `GET` request.
        """
        h = HTTPHeaders()
        h.update(self._default_headers)
        if headers:
            h.update(headers)

        req = HTTPRequest(url, headers=headers)
        self._client.fetch(req, callback)

    def _post(self, url, body, headers=None, callback=None):
        """
        A async `POST` request.
        """
        h = headers or HTTPHeaders()
        h.update(self._default_headers)
        h["Content-type"] = "application/json"
        request = HTTPRequest(url, headers=h, method="POST",
            body=json.dumps(body))
        self._client.fetch(request, callback)

    def _put(self, url, body, headers=None, callback=None):
        """
        A async `POST` request.
        """
        h = headers or HTTPHeaders()
        h.update(self._default_headers)
        h["Content-type"] = "application/json"
        request = HTTPRequest(url, headers=h, method="PUT", body=body)
        self._client.fetch(request, callback)

    def _delete(self, url, headers=None, callback=None):
        h = HTTPHeaders()
        h.update(self._default_headers)
        if headers:
            h.update(headers)
        req = HTTPRequest(url, headers=headers, method="DELETE")
        self._client.fetch(req, callback)

    def search(self, querybuilder, callback=None):
        """
        Method to search the index given a configured querybuilder
        """
        raise NotImplementedError('implement in child class')

    def index_document(self, doc, callback=None, commit=False):
        """
        Method to async index the given doc
        """
        raise NotImplementedError('implement in child class')

    def remove_by_id(self, doc_id, callback=None, commit=False):
        """
        Remove any documents matching the given doc_id.
        """
        raise NotImplementedError('implement in child class')

    def remove_by_query(self, query, callback=None):
        """
        Remove any documents matching the given query.
        """
        raise NotImplementedError('implement in child class')

    def commit(self, callback=None):
        """
        Commit any pending changes.
        """
        raise NotImplementedError('implement in child class')

    def handle_indexing_response(self, callback=None):
        """
        Method to edit the indexing response
        """
        def inner_callback(response):
            body = response.body
            if not body or "ERROR" in body:
                callback({'error': 'not_indexed', 'response': response})
            else:
                callback({'ok': True})

        return inner_callback

    def handle_search_response(self, query, callback):
        """
        Method to edit the search response
        """
        raise NotImplementedError('implement in child class')
