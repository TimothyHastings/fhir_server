#
# TODO Order collection command.
#

def order_collection(schema, command_line):
    # Test command
    print("Order Collection")

    # order <collection> on <attribute>
    collection_name = command_line[1]
    print(collection_name)
    collection = schema.get_collection(collection_name)

    if collection is None:
        print("Invalid Collection")
        return

    # Test only
    order = "ACC"
    collection.sort("id", order)



