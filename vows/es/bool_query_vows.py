from pyvows import Vows, expect
from dopplr.es.query.text_query import TextQuery
from dopplr.es.query.bool_query import BoolQuery


@Vows.batch
class BoolQueries(Vows.Context):

    def topic(self):
        must_text_query = TextQuery('content', 'my value')
        must_not_text_query = TextQuery('body', 'my value')
        should_text_query = TextQuery('title', 'my title')
        bool_query = BoolQuery()
        bool_query.add_must(must_text_query)
        bool_query.add_must_not(must_not_text_query)
        bool_query.add_should(should_text_query)
        return bool_query

    def must_have_must(self, topic):
        bool_query = topic.get_params()
        expect(bool_query['bool']['must'][0]['text']['content']['query']).to_include('my value')

    def must_have_must_not(self, topic):
        bool_query = topic.get_params()
        expect(bool_query['bool']['must_not'][0]['text']['body']['query']).to_include('my value')

    def must_have_should(self, topic):
        bool_query = topic.get_params()
        expect(bool_query['bool']['should'][0]['text']['title']['query']).to_include('my title')
