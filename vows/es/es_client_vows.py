# vim: set fileencoding=utf-8 :
#
# Copyright (c) 2012 Retresco GmbH
# Copyright (c) 2011 Hagen Toennies <hagentoennies at googlemail.com>
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
from pyvows.core import Vows, expect
from tornado_pyvows.context import TornadoContext
from dopplr.es.client import EsClient
from dopplr.es.querybuilder import QueryBuilder
from dopplr.es.query.text_query import TextQuery
from dopplr.es.query.mlt_query import MltQuery

import json

''' Integration  Test need a running elasticsearch instance '''

'''
@Vows.batch
class EsVows(Vows.Context):

    class AddIndex(TornadoContext):

        def topic(self):
            self.io_loop = self.get_new_ioloop()
            es = EsClient('http://localhost:9200', ioloop=self.io_loop)
            es.create_index('test', self.stop)
            response = self.wait(timeout=10)
            return response

        def responseShouldNotBeNull(self, topic):
            expect(topic).Not.to_be_null()

    class AddMapping(TornadoContext):

        def topic(self):
            self.io_loop = self.get_new_ioloop()
            es = EsClient('http://localhost:9200', ioloop=self.io_loop)
            mapping = {'test': {'properties': {'item_field': {'boost': 1.0, 'index': 'analyzed', 'store': 'yes', 'type': u'string'}}}}
            es.create_mapping('test', 'test', json.dumps(mapping), self.stop)
            response = self.wait(timeout=10)
            return response

        def responseShouldNotBeNull(self, topic):
            expect(topic).Not.to_be_null()

    class AddDoc(TornadoContext):

        def topic(self):

            self.io_loop = self.get_new_ioloop()
            es = EsClient('http://localhost:9200', ioloop=self.io_loop)
            doc = {'item_field': 'NEU'}
            es.index_document(doc, 1, 'test', 'test', self.stop)
            response = self.wait(timeout=10)
            return response

        def responseShouldNotBeNull(self, topic):
            expect(topic).Not.to_be_null()

    class QueryText(TornadoContext):

        def topic(self):
            self.io_loop = self.get_new_ioloop()
            es = EsClient('http://localhost:9200', ioloop=self.io_loop)
            qb = QueryBuilder(response_mapper=self._response_mapper, index_name='test', mapping_type='test')
            qb.add(TextQuery('item_field', 'NEU'))
            es.search(qb, self.stop)
            response = self.wait(timeout=10)
            return response

        def _response_mapper(self, response):
            return response

        def responseShouldNotBeNull(self, topic):
            expect(topic).Not.to_be_null()

        def shouldHaveHits(self, topic):
            expect('hits' in topic).to_be_true()

    class QueryMoreLikeThis(TornadoContext):

        def topic(self):
            self.io_loop = self.get_new_ioloop()
            es = EsClient('http://localhost:9200', ioloop=self.io_loop)
            qb = QueryBuilder(response_mapper=self._response_mapper, index_name='my_river', mapping_type='page')
            mlt_query = MltQuery(['page.text'], 'testing')
            qb.add(mlt_query)
            es.search(qb, self.stop)
            response = self.wait(timeout=10)
            return response

        def _response_mapper(self, response):
            return response

        def responseShouldNotBeNull(self, topic):
            expect(topic).Not.to_be_null()

        def shouldHaveHits(self, topic):
            expect('hits' in topic).to_be_true()
'''
