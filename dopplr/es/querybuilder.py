# vim: set fileencoding=utf-8 :
#
# Copyright (c) 2012 Retresco GmbH
# Copyright (c) 2011 Daniel Truemper <truemped at googlemail.com>
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

from dopplr.basequery import BaseQuery
from dopplr.es.query.query import Query
from dopplr.basequerybuilder import BaseQueryBuilder


class QueryBuilder(BaseQueryBuilder):
    """
    The `QueryBuilder` creating ElasticSearch queries.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize me.
        """
        self.__params = {'query': {}}
        self.headers = kwargs.get('headers', None)
        self.response_mapper = kwargs.get('response_mapper', None)
        self._index_name = kwargs.get('index_name', 'test')
        self._mapping_type = kwargs.get('mapping_type', 'test')

    def add(self, query):
        """
        Add a query objet to the `QueryBuilder`.
        """
        if not isinstance(query, BaseQuery):
            raise TypeError
        if isinstance(query, Query):
            self.__params['query'] = query.get_params()

    def get_params(self):
        """
        Compute and return a list of all query values.
        """
        return self.__params
