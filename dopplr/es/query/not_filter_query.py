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


class NotFilterQuery(object):
    """
    http://www.elasticsearch.org/guide/reference/query-dsl/not-filter.html

    {
    "filtered" : {
        "query" : {
            "term" : { "name.first" : "shay" }
        },
        "filter" : {
            "not" : {
                "range" : {
                    "postDate" : {
                        "from" : "2010-03-01",
                        "to" : "2010-04-01"
                        }
                    }
                }
            }
        }
    }
    """
    def __init__(self, query, filter_expression):
        """
        Initialize the query value.
        """
        self._query = query
        self._filter_exp = filter_expression

    def get_params(self):
        """
        Return the list of query params.
        """
        filtered = dict()
        filtered['filtered']['query'] = self._query.get_params()
        filtered['filtered']['filter']['not'] = self._filter_expression.get_params()
        return filtered
