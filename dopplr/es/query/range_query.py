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
    {
    "range": {
        "field":{
            "from": "%s",
            "to": "%s"
            }
        }
    }
    """
    def __init__(self, field, start, end):
        """
        Initialize the query value.
        """
        self._field = field
        self._from = start
        self._to = end

    def get_params(self):
        """
        Return the list of query params.
        """
        query = dict()
        query['range'] = {'field': {self._field: {
        'from': self._from, 'to': self._to}}}
        return query
