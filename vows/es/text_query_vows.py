from pyvows import Vows, expect
from dopplr.es.query.text_query import TextQuery


@Vows.batch
class SimpleQueries(Vows.Context):

    def topic(self):
        return TextQuery('content', 'my value').get_params()

    def mustMatch(self, topic):
        expect(topic['text']['content']).to_include('my value')
