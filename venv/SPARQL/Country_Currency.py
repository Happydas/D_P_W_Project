# -*- coding: utf-8 -*-
import io

from SPARQLWrapper import SPARQLWrapper, JSON

# wrap the dbpedia SPARQL end-point
endpoint = SPARQLWrapper("http://dbpedia.org/sparql")

# set the query string
endpoint.setQuery("""
SELECT DISTINCT ?country ?currency
 WHERE { 
?city rdf:type dbo:City ; 
rdfs:label ?label ; 
dbo:country ?country .
?country dbo:currency  ?currency .
} order by ?country

""")

# select the retur format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)

# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results = endpoint.query().convert()

f= open("../Data/Currency_Country/Country_Currency.txt","w+", encoding="utf-8")

# interpret the results:
for res in results["results"]["bindings"] :
    f.write("%s %s\n" %  (res['country']['value'],  res['currency']['value']))

