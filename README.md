# CASE Examples Quality Control

The purpose of this repository is to test sample CASE data for issues such as mis-spelled identifiers, syntax normalization, and CASE/UCO concept coverage gap.

Practices implemented in this repository are not necessarily practices agreed to by the CASE or UCO communities.


## Output generated: ontology coverage gap

Running just `make` will generate files listing what appear to be non-knowledge-base ontology terms that are not yet covered in CASE or UCO.  These files are tracked in this repository, following the pattern `tests/CASE-Examples/examples/local_ontology_vocabulary-*.txt` (the unknown terms contributed by each example file).  [`undefined_vocabulary.txt`](tests/CASE-Examples/examples/undefined_vocabulary.txt) in that same folder lists the uncovered vocabulary pooled from all the examples.  Examples on the website are tested similarly under [`tests/casework.github.io/examples/`](tests/casework.github.io/examples/).


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

Should you need to run the tests offline, after cloning this repository, run `make download` to retrieve resources that require network access.  Network access is only needed until `make download` finishes.  Note that a `.jar` file is downloaded (`lib/rdf-toolkit.jar`).  Its Git-tracked hash is verified before the download reports as successful (and hence before any test runs it).

Tests can run with `make -j`.
