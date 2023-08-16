FHIR Proof of Concept
Tim Hastings, 2023

cli.py          Command Line Interface - processes SQL-like commands
collection.py   Defines a database collection class.
loader.py       Loads collections from the file system.
main.py         Creates and loads the database.
query.py        Underlying FHIR (json) queries. TODO: extend the number of segments.
resource.py     Defines a basic resource used in the database.
schema.py       Defines a database schema.
test.py         Used only for initial development.

Patient1.FHIR   Sample patient with id = urn001
Patient2.FHIR   Sample patient with id = urn002
Observation1.FHIR   Sample observation with id = urn001
Observation2.FHIR   Sample observation with id = urn002

cli_test.txt    Sample CLI commands - Based on collections and resources being created.


NOTES
Use the help command to get started.
A Collection Directory must exist in the program directory.
Use the create command to create collections.
Use insert file <filename> into <collection> to add resources.
Use load n <filename> into <collection> to add many resources.

Getting started.
Use simple select commands for Patient and Observation collections.
Try a join - no spaces between collections!
Try loading 1000 Patient1.FHIR resources then insert a Patient2.FHIR resource.
Add new PatientX.FHIR and ObservationX.FHIR with modified attributes.

Simple Search example run time
create Test
insert file Patient1.fhir into Test
load 10000 Patient2.fhir into Test
selectDistinct * from Test where id = urn001
# Check the run time
reverse Test
selectDistinct * from Test where id = urn001
# Check the run time


References
https://www.hl7.org/fhir/index.html
For examples go to https://www.hl7.org/fhir/resourcelist.html
FHIR Server POC.pptx
