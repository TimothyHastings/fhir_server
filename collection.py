"""
FHIR Server Proof of Concept
Author: Tim Hastings, 2023
"""
import random
import uuid
from schema import Schema
from resource import Resource


#
# The Collection class is analogous to a table.
# A collection has:
#   - A unique identifier
#   - A name used to store data
#   - A list of resources
#   - The state of a collection - LOADED | SAVED
#
class Collection:

    def __init__(self, name):
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.resources = list()
        self.state = Schema.LOADED

    def __str__(self):
        return self.uuid + ", " + self.name + ", " + self.state

    # Add a resource to the collection.
    def add_resource(self, resource):
        self.resources.append(resource)

    # Delete a resource form the collection.
    def del_resource(self, id):
        for resource in self.resources:
            if resource.uuid == id:
                self.resources.remove(resource)
                break

    # Update a resource.
    def update_resource(self, id, res):
        for resource in self.resources:
            if resource.uuid == id:
                self.resources = res
                break

    #
    # Get a resource using its id and return the resource.
    #
    def get(self, id):
        for resource in self.resources:
            if str(resource.uuid) == str(id):
                return resource
        return False

    #
    # Search a collection using query()
    # Return a result list of resources.
    #
    def search(self, qry):
        result = list()
        i = 0
        for resource in self.resources:
            if resource.search(qry):
                result.append(resource)
        return result

    #
    # Search a collection using using a query set.
    # Each query in the set must be a match.
    # You need to consider the structure of the collection to form the query.
    # '{', '}', '[' and ']' may be left out.
    #
    def search_complex(self, query_set):
        results = list()
        for qry in query_set:
            results += self.search(qry)
        return results

    #
    # Clear the resources.
    #
    def clear(self):
        self.resources.clear()

    #
    # Load the collection from storage.
    #
    def load(self):
        dir_list = Schema.get_resource_list(self.name)
        self.resources.clear()
        for entry in dir_list:
            if entry[0] == '.':
                # Skip directories.
                continue
            r = Resource(self.name)
            r.uuid = entry
            r.state = Schema.LOADED
            r.load(entry)
            self.resources.append(r)

    #
    # Save the collection to storage.
    #
    def save(self):
        for resource in self.resources:
            print("Collection:save", resource)
            resource.save()

    #
    # Reverse the order of a collection.
    #
    def reverse(self):
        self.resources.reverse()

    #
    # Randomise the order of a collection.
    #
    def randomise(self):
        random.shuffle(self.resources)
