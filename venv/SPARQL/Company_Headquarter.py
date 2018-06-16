# -*- coding: utf-8 -*-
import io

from SPARQLWrapper import SPARQLWrapper, JSON

endpoint = SPARQLWrapper("http://dbpedia.org/sparql")

endpoint.setQuery("""
select DISTINCT ?x, ?y where {
 ?x a dbo:Company.
 ?y a dbo:City.
 ?x dbo:headquarter ?y.
} order by ?x

""")

endpoint.setReturnFormat(JSON)

results = endpoint.query().convert()

f= open("../Data/Company_Headquarter/Company_headquarter.txt","w+", encoding="utf-8")

for res in results["results"]["bindings"] :
    f.write("%s %s\n" %  (res['x']['value'],  res['y']['value']))

