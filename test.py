"""
FHIR Server Proof of Concept
Author: Tim Hastings, 2023
"""
import json

import query
from collection import Collection
from resource import Resource
from schema import Schema

#
# Low level unit tests only.
#
#
# Patients
#
patients = Collection("Patient")
patients.load()
#
# Observations
#
observations = Collection("Observation")
observations.load()

print("Get a Resource attribute value")
r1 = Resource("Patient")
r1.load_file("Patient1.fhir", "")
x = r1.get_attribute_value("id")
print(x)

o1 = Resource("Observation")
o1.load_file("Observation1.fhir", "")
print(o1.data)
print("Test attribute value")
print(o1.data)
print(o1.test_attribute_value("id", "=", "urn001"))
print("Get the valueQuantity value field which is an Integer")
valueQuantity = o1.get_attribute_value("valueQuantity")
segment = Resource("Temp")
segment.data = str(valueQuantity)
print(segment.data)
value = segment.get_attribute_value("value")
print(value)

print("Using Query and resource Functions")
print(query.get_attribute_value(o1.data, "id"))
print(query.test_attribute_value(o1.data, "id", "=", "urn001"))
print(o1.get_attribute_value("id"))
print(o1.test_attribute_value("id", "=", "urn001"))

print("Get part")
segment = query.get_attribute_value(o1.data, "valueQuantity")
print(segment)
print("Get the integer value")
print(query.get_attribute_value(segment, "value"))
print("Test value range")
print(query.test_attribute_range(segment, "value", 5.0, 8.0))

print("Test getting a segment attribute value")
print(query.get_segment_attribute_value(o1.data, "valueQuantity", "value"))
print(o1.get_segment_attribute_value("valueQuantity", "value"))

print("Test if a segment attribute value = value")
print(query.test_segment_attribute_value(o1.data, "identifier", "value", "=", "6323"))
print(o1.test_segment_attribute_value("identifier", "value", "6323"))

print("Test if a segment attribute value range")
print(query.test_segment_attribute_range(o1.data, "valueQuantity", "value", 1.0, 8.0))
print("Test get records for attribute value range")
results = query.get_resources_by_segment_attribute_range(observations, "valueQuantity", "value", 1.0, 4.0)
for result in results:
    print(result)
exit(0)

print("Test 2 segment attribute value")
print(query.get_2segments_attribute_value(o1.data, "interpretation", "coding", "extension"))

print("Test 2 segment ")
print(query.test_2segments_attribute_value(o1.data, "interpretation", "coding", "code", "H"))

print("Test 2 segment range ")
print(query.test_2segments_attribute_range(o1.data, "interpretation", "coding", "extension", 0, 3))

print("Number of Patients:", len(patients.resources))
"""
for p in patients.resources:
    print(p)
"""

# Test load and save
# patients.save()
# observations.save()
# patients.clear()
# patients.load()
# observations.load()

print("Observations:", len(observations.resources))
"""
for r in observations.resources:
    print(r)
"""
schema = Schema("schema1")
schema.collections.append(patients)
schema.collections.append(observations)

q1 = '"id" : "urn001"'
q2 = '"id" : "urn006"'
q_list = list()
q_list.append(q1)
q_list.append(q2)

print("Simple Patient Collection Search")
results = patients.search(q2)
for result in results:
    print(str(result.uuid), result.data)

print("Complex Patient Collection Search")
results = patients.search_complex(q_list)
for result in results:
    print(str(result.uuid), result.data)

print("Simple Observation Collection Search")
results = observations.search(q2)
for result in results:
    print(str(result.uuid), result.data)

print("Complex Observation Collection Search")
results = observations.search_complex(q_list)
for result in results:
    print(str(result.uuid), result.data)

c_list = list()
c_list.append(observations)
c_list.append(patients)

print("Complex Schema Search")

results = schema.search(c_list, q_list)
for result in results:
    print(result.uuid, result.data)

print("Get a resource")
result = patients.get('1b27e9a3-807b-4f8a-9710-f3eef8a6d4fa')
print(str(result.uuid), result.data)

print("Collection Test")
print("Get Resources by attribute value")
results = list()
results = query.get_resources_by_attribute_value(patients, "id", "urn001")
print("Found", len(results))
for result in results:
    print(result)

print("Get Resources by segment attribute value range")
results = query.get_resources_by_segment_attribute_range(observations, "valueQuantity", "value", 1, 4.0)
print("Found", len(results))
for result in results:
    print(result)
