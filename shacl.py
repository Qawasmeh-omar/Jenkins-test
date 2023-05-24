from pyshacl import validate
import rdflib

# Load the RDF data graph
data_graph = rdflib.Graph()
data_graph.parse('ontology.ttl', format='turtle')

# Load the SHACL shape graph
shape_graph = rdflib.Graph()
shape_graph.parse('test-shape.ttl', format='turtle')

# Validate the data graph against the shape graph
conforms, results_graph, results_text = validate(data_graph, shacl_graph=shape_graph, ont_graph=None,
                                                inference='rdfs', abort_on_error=False)

# Print validation results
if conforms:
    print("Data graph is valid against the shape graph.")
else:
    print("Data graph is not valid against the shape graph. Validation results:")
    for result in results_graph:
        print(result)
