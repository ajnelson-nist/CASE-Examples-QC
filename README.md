# CASE Examples Quality Control

The purpose of this repository is to test sample CASE data for issues such as mis-spelled identifiers, syntax normalization, and CASE/UCO concept coverage gap.

Practices implemented in this repository are not necessarily practices agreed to by the CASE or UCO communities.


## Output generated: ontology coverage

Running just `make` will generate ontology-concept lists:
* [Used ontontology concepts](tests/used_concepts.txt) - This is a list of ontological concepts used in any of the [CASE-Examples](https://github.com/casework/CASE-Examples/tree/master/examples) illustrations or [website examples](https://github.com/casework/casework.github.io/tree/master/examples).  They may or may not be in the current CASE release (and associated UCO release).
* [Used `kindOfRelationship` values](tests/used_kindOfRelationships.tsv) - This is a list of the `kindOfRelationship` values used, whether they are in a vocabulary in the current CASE release (and associated UCO release) or not.
* [Undefined concepts](tests/undefined_concepts.txt) - This is the list of used concepts as above, except all ontology concepts in the current CASE release (and associated UCO release) are removed.
  - Similarly, there is a list of [undefined `kindofRelationship` values](tests/undefined_kindOfRelationships.tsv).


## Tests implemented

* Turtle data is confirmed normalizeable in form with rdf-toolkit.
  - This is confirmed by running `make normalize`.
* JSON-LD data is confirmed normalizeable in form with Python's `json.tool` module.
  - This is also confirmed by running `make normalize`.
* JSON-LD data is confirmed normalized in form with Python's `json.tool` module.
  - This is confirmed by running `make check`.

These tests run against the CASE and UCO ontologies at the commits tracked here as Git submodules.


### Manual testing

The test suite can be run manually by running:

```
make normalize
make check
make
```

Should you need to run the tests offline, after cloning this repository, run `make download` to retrieve resources that require network access.  Network access is only needed until `make download` finishes.  Note that a `.jar` file is downloaded (`rdf-toolkit.jar`).  Its Git-tracked hash is verified before the download reports as successful (and hence before any test runs it).

Tests can run with `make -j`.
