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


class TextQuery(Query):
    """
    http://www.elasticsearch.org/guide/reference/query-dsl/text-query.html
    {
     "text" : {
        "message" : "this is a test"
     }
    }
    """
    def __init__(self, field, value, operator='and'):
        """
        Initialize the query value.
        """
        self._field = field
        self._value = value
        self._operator = operator

    def get_params(self):
        """
        Return the list of query params.
        """
        query = dict()
        query['text'] = {self._field: {'query': self._value, 'operator': self._operator}}
        return query


class TextPhraseQuery(Query):
    """
    http://www.elasticsearch.org/guide/reference/query-dsl/text-query.html
    {
        "text" : {
            "message" : {
                "query" : "this is a test",
                "type" : "phrase"
            }
        }
    }
    """
    def __init__(self, field, value, query_type='phrase'):
        """
        Initialize the query value.

        @param query_type one of 'phrase' or 'phrase_prefix'
        """
        self._field = field
        self._value = value
        self._type = query_type

    def get_params(self):
        """
        Return the list of query params.
        """
        query = dict()
        query['text'] = {self._field: {'query': self._value, 'type': self._type}}
        return query
