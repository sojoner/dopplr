# vim: set fileencoding=utf-8 :
#
# Copyright (c) 2012 Retresco GmbH
# Copyright (c) 2012 Hagen Toennies <hagentoennies at googlemail.com>
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
#
#
import logging
import json
from tornado.httputil import HTTPHeaders
from dopplr.baseclient import BaseClient

__all__ = ['EsClient']
log = logging.getLogger('elasticsearch')


class EsClient(BaseClient):
    """
    A Client class to work with an ElasticSearch instance.
    """

    def __init__(self, host='http://localhost:9200', document_verifier=None, ioloop=None, **client_args):
        """
        Initialize me.
        """
        BaseClient.__init__(self, ioloop=ioloop, client_args=client_args)
        self._document_verifier = document_verifier
        self._es_host = host
        self._default_headers = HTTPHeaders()

    def search(self, querybuilder, callback=None):
        """
        Search the ElasticSearch with `querybuilder.get_params()` as query parameter.
        """
        url = '%s/%s/%s/_search' % (self._es_host, querybuilder._index_name, querybuilder._mapping_type)
        query_params = json.dumps(querybuilder.get_params())
        log.debug('Searching elasticsearch with params: %s' % query_params)
        self._post(url, query_params, headers=querybuilder.headers,
                callback=self.handle_search_response(querybuilder, callback))

    def index_document(self, doc, doc_id, index_name, mapping_type, callback=None):
        """
        Index a `doc` into ElasticSearch. The `callback` will be called from within
        `self.handle_indexing_response`.
        """
        url = '%s/%s/%s/%s' % (self._es_host, index_name, mapping_type, doc_id)
        headers = dict()
        headers['Content-Type'] = 'application/json'
        self._post(url, doc, callback=self.handle_indexing_response(callback))

    def create_index(self, index_name, callback=None):
        """
        Creates a new index in the ElasticSearch instance.
        """
        url = '%s/%s/' % (self._es_host, index_name)
        self._put(url, "", callback=callback)

    def delete_index(self, index_name, callback=None):
        """
        Deletes a index in the ElasticSearch instance.
        """
        url = '%s/%s/' % (self._es_host, index_name)
        self._delete(url, callback=callback)

    def create_mapping(self, index_name, mapping_name, mapping, callback):
        """
        Creates a new mapping for an index in the ElasticSearch instance.
        """
        url = '%s/%s/%s/_mapping' % (self._es_host, index_name, mapping_name)
        self._put(url, mapping, callback=callback)

    def delete_mapping(self, index_name, mapping_name, mapping, callback):
        """
        Deletes a mapping from an index in the ElasticSearch instance.
        """
        url = '%s/%s/%s/_mapping' % (self._es_host, index_name, mapping_name)
        self._delete(url, mapping, callback=callback)

    def remove_by_id(self, index_name, doc_id,  mapping_type=None, callback=None):
        """
        Deletes the document with given `doc_id`.
        """
        if mapping_type:
            url = '%s/%s/%s/%s/' % (self._es_host, index_name, mapping_type, doc_id)
        else:
            url = '%s/%s/%s/' % (self._es_host, index_name, doc_id)
        self._delete(url, callback)

    def handle_search_response(self, query, callback):
        """
        Closure for handling the search response.
        """
        def inner_callback(response):
            try:
                result = json.loads(response.body)
            except TypeError:
                log.error('Error searching elasticsearch: %s' % response.body)
                callback({'error': 'no_json', 'result': response.body})
                return
            numFound = result['hits']['total']
            if numFound == 0:
                log.info('Search returned zero results')
                callback({'error': 'not_found'})
            else:
                log.info('Search returned "%s" results' % numFound)
                callback(query.response_mapper(result))

        return inner_callback
