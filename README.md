= doppler

The doppler project provides asynchronous communication from Python to Apache 
Solr and ElasticSearch.

== Solr
There is a solr module which will enable you to index, search and delete 
documents in a asynchronous way.

== ElasticSearch
There is a es module which will enable you to use ElasticSearch in a REST-full 
way. Be aware that the ElasticSearch implementation is not yet complete, despite 
that fact its possible to do basic stuff, like creating and deleting indicies 
and mappings, index documents and search for them.

== Requirements

doppler has been built against the following software:

* Python 2.6+ <[[http://python.org/]]>
* Tornado 2.2.1 <[[http://www.tornadoweb.org/]]>
* Solr 3.6.1 <[[http://lucene.apache.org/solr/]]>
* ElasticSearch 0.19 <[[http://www.elasticsearch.org/]]>

Earlier versions of these may work but are not guaranteed to do so.

== Installation

You can use the latest code from GitHub within your buildout.cfg

{{{
[doppler]
recipe = zerokspot.recipe.git
repository = https://github.com/truemped/doppler.git
as_egg = True
cache-name = doppler-master
}}}

Or you use the latest code from GitHub directly:

{{{
https://github.com/truemped/doppler.git
}}}

== Getting Started

The following code examples show a possible usage of the solr doppler API:

=== Solr

{{{
    from doppler.solr.solr_client import SolrClient
    from doppler.solr.solr_query_builder import QueryBuilder
    from doppler.solr.query.query import Query

    def callback(response):
		print response

	self.io_loop = IOLoop.instance()
	solr = SolrClient('http://localhost:8983/solr/swp',
                ioloop=self.io_loop)
    doc = dict()
    doc['doc_id'] = 'test_id'
    doc['title'] = 'test title'
    doc['body'] = 'test body ---> boody woogie boogie'
    solr.index_document(doc, callback , commit=True)

    qb = QueryBuilder()
    qb.add(Query('body:test body'))
    solr.search(qb, callback)
}}}

=== ES

{{{
    from doppler.es.client import EsClient
    from doppler.es.querybuilder import QueryBuilder
    from doppler.es.query.text_query import TextQuery
    from doppler.es.query.mlt_query import MltQuery
    import json

    def callback(response):
        print response
    
    # create index
	es = EsClient('http://localhost:9200', ioloop=self.io_loop)
    es.create_index('test', callback)
    
    # create mapping
    mapping = {'test': {'properties': {'item_field': {'boost': 1.0, 'index': 'analyzed', 'store': 'yes', 'type': u'string'}}}}
    es.create_mapping('test', 'test', json.dumps(mapping), callback)

    # index document
    doc = {'item_field': 'NEU'}
    es.index_document(doc, 1, 'test', 'test', callback)

    # search document
    qb = QueryBuilder(response_mapper=self._response_mapper, index_name='test', mapping_type='test')
    qb.add(TextQuery('item_field', 'NEU'))
    es.search(qb, callback)
}}}


For more examples take a look into the vows/ directory where you find some tests.

== License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



