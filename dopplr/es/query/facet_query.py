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


class StatisticFacetQuery(Query):
    """

    a stats facet
    {
    "query" :{
               "term" : {
                   "fieldname":"test"}
               },
               "facets" : {
                   "stat1"  : {
                   "statistical" : {
                       "field" : "fieldname"
                    }
                }
            }
        }
    """

    def __init__(self, facet_field, query=None):
        """
        Initialize the query value.
        """
        self._facet_field = facet_field
        self._query = query

    def get_params(self):
        params = dict()
        if self._query:
            for k, v in self._query:
                params[k] = v
        params['facets'] = {'stat1': {'statistical':\
        {'field': self._facet_field}}}

        return params


class HistogramFacetQuery(Query):
    """
    a histogram facet
    {
    "query" : {
        "term" : {
            "fieldname":"fieldvalue"
        }
    },
        "facets" : {
            "histo1" : {
                "histogram" : {
                    "field" : "facet_field",
                    "interval" : 100
                    }
                }
            }
    }
    """

    def __init__(self, facet_field, interval=10, query=None):
        """
        Initialize the query value.
        """
        self._facet_field = facet_field
        self._interval = interval
        self._query = query

    def get_params(self):
        params = dict()
        if self._query:
            for k, v in self._query:
                params[k] = v
        params['facets'] = {'histo1': {'histogram':\
        {'field': self._facet_field, 'interval': self._interval}}}

        return params
