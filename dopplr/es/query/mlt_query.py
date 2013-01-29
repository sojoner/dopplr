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


class MltQuery(Query):
    """
    http://www.elasticsearch.org/guide/reference/query-dsl/mlt-query.html
    {
     "more_like_this" : {
        "fields" : ["name.first", "name.last"],
        "like_text" : "text like this one",
        "min_term_freq" : 1,
        "max_query_terms" : 12
        }
    }
    """
    def __init__(self,
        fields,
        like_text,
        percent_terms_to_match=0.3,
        min_term_freq=1,
        max_query_terms=25,
        stop_words=[],
        min_doc_freq=1,
        max_doc_freq=1000000,
        min_word_len=0,
        max_word_len=1000000,
        boost_terms=1,
        boost=1.0,
        analyzer='default'
        ):
        """
        Initialize the mlt values value.
        """
        self._fields = fields
        self._like_text = like_text
        self._percent_terms_to_match = percent_terms_to_match
        self._min_term_freq = min_term_freq
        self._max_query_terms = max_query_terms
        self._stop_words = stop_words
        self._min_doc_freq = min_doc_freq
        self._max_doc_freq = max_doc_freq
        self._min_word_len = min_word_len
        self._max_word_len = max_word_len
        self._boost_terms = boost_terms
        self._boost = boost
        self._analyzer = analyzer

    def get_params(self):
        """
        Return the list of query params.
        """
        query = dict()
        query['more_like_this'] = {'fields': self._fields,
                                  'like_text': self._like_text,
                                  'percent_terms_to_match': self._percent_terms_to_match,
                                  'min_term_freq': self._min_term_freq,
                                  'max_query_terms': self._max_query_terms,
                                  'stop_words': self._stop_words,
                                  'min_doc_freq': self._min_doc_freq,
                                  'max_doc_freq': self._max_doc_freq,
                                  'min_word_len': self._min_word_len,
                                  'max_word_len': self._max_word_len,
                                  'boost_terms': self._boost_terms,
                                  'boost': self._boost,
                                  'analyzer': self._analyzer
                                  }
        return query
