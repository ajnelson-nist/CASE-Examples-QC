# Status of non-CASE, non-UCO vocabulary usage

This directory contains text files that list terms not known to CASE or UCO, but used in the CASE website examples.  The lists exclude all terms found to be in the CASE and imported UCO ontology version provided by the [pinned version](https://github.com/casework/CASE-Examples/blob/master/requirements.txt) of [`case-utils`](https://pypi.org/project/case-utils/).  The lists also exclude all "Knowledge-base" graph nodes, which represent instance data.

The following table is the count of undefined concepts used in each example file:

```
   8 asgard/undefined_concepts.txt
  11 crossover_wmd/undefined_concepts.txt
  20 owl_trafficking/undefined_concepts.txt
   3 urgent_evidence/undefined_concepts.txt
  33 undefined_concepts.txt
```

The following table is the count of undefined relationship literals used in each example file:

```
  2 asgard/undefined_kindOfRelationships.tsv
  5 crossover_wmd/undefined_kindOfRelationships.tsv
  3 owl_trafficking/undefined_kindOfRelationships.tsv
  1 urgent_evidence/undefined_kindOfRelationships.tsv
  5 undefined_kindOfRelationships.tsv
```
