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

from dopplr.es.query.query import Query


class StringQuery(Query):
    """
    http://www.elasticsearch.org/guide/reference/query-dsl/query-string-query.html
    {
      "query_string" : {
        "default_field" : "content",
        "query" : "this AND that OR thus"
      }
    }
    """

    def __init__(self, field, value):
        """
        Initialize the query value.
        """
        self._field = field
        self._value = value

    def get_params(self):
        """
        Return the list of query params.
        """
        query = dict()

        query['query_string'] = {
        'default_field': self._field,
        'query': self._value
        }
        return query
