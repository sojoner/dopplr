# vim: set fileencoding=utf-8 :
#
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

from dopplr.es.query.query import Query


class BoolQuery(Query):
    """
    The most simple Solr query: `q`.
    """

    def __init__(self, must=None, must_not=None, should=None,
                 boost=None, minimum_number_should_match=1,
                 disable_coord=None,
                 **kwargs):
        self._must = []
        self._must_not = []
        self._should = []
        self.boost = boost
        self.minimum_number_should_match = minimum_number_should_match
        self.disable_coord = disable_coord

        if must:
            self.add_must(must)

        if must_not:
            self.add_must_not(must_not)

        if should:
            self.add_should(should)

    def add_must(self, query):
        if not isinstance(query, Query):
            raise TypeError
        self._must.append(query)

    def add_should(self, query):
        if not isinstance(query, Query):
            raise TypeError
        self._should.append(query)

    def add_must_not(self, query):
        if not isinstance(query, Query):
            raise TypeError
        self._must_not.append(query)

    def get_params(self):
        filters = {}
        if self._must:
            filters['must'] = [f.get_params() for f in self._must]
        if self._must_not:
            filters['must_not'] = [f.get_params() for f in self._must_not]
        if self._should:
            filters['should'] = [f.get_params() for f in self._should]
            filters['minimum_number_should_match'] = self.minimum_number_should_match
        if self.boost:
            filters['boost'] = self.boost
        if self.disable_coord is not None:
            filters['disable_coord'] = self.disable_coord
        if not filters:
            raise RuntimeError("A least a filter must be declared")
        return {"bool": filters}
