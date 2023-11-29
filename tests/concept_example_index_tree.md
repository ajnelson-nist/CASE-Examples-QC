__NOTE: Page under design-draft; not yet programmatically generated.__


# Tree index of CDO concepts' usage in examples

This file provides an index mapping all Cyber Domain Ontology (CDO) concepts exercised in one of the CASE example data sources (the CASE website, CASE Examples, or CASE Corpora).  For each concept, example graph files containing a usage of the specific concept are linked.  Draft concepts are at the bottom of the page.

This is a tree index, organizing classes and properties by their subclass/subproperty hierarchy, and then alphabetically.  For an index holding only one hierarchy level of classes and properties, see the [flat index](concept_example_index_flat.md).

__Note__: This is not an exhaustive listing of CDO concepts.  Only concepts that have been used (whether directly, or whether a subclass/subproperty was used directly) in an example appear on this page.

__Note__: Due to multiple-inheritance, some concepts might be indexed repeatedly.


## CASE concepts

* [`case-investigation:Subject`](https://ontology.caseontology.org/case/investigation/Subject)
   * CASE Examples:
      * [`forensic_lifecycle.json`](https://github.com/casework/CASE-Examples/blob/master/examples/illustrations/forensic_lifecycle/forensic_lifecycle.json)


## UCO concepts

* `owl:Thing`
   * Subclasses:
   * [`uco-core:UcoThing`](https://ontology.unifiedcyberontology.org/uco/core/UcoThing)
      * Subclasses:
         * [`uco-core:UcoInherentCharacterizationThing`](https://ontology.unifiedcyberontology.org/uco/core/UcoInherentCharacterizationThing)
            * Subclasses:
               * `drafting:Quality`
                  * Subclasses:
                     * `drafting:FileHashQuality`
                        * CASE Corpora:
                           * [`digitalcorpora-android-7`](https://github.com/casework/CASE-Corpora/tree/main/catalog/datasets/digitalcorpora-android-7#readme)
               * [`uco-types:DictionaryEntry`](https://ontology.unifiedcyberontology.org/uco/types/DictionaryEntry)
                  * Subclasses:
                     * [`uco-types:ControlledDictionaryEntry`](https://ontology.unifiedcyberontology.org/uco/types/ControlledDictionaryEntry)
                        * CASE website:
                           * [`asgard.json`](https://caseontology.org/examples/asgard/asgard.json)
                           * [`urgent_evidence.json`](https://caseontology.org/examples/urgent_evidence/urgent_evidence.json)
                        * CASE Examples:
                           * [`exif_data.json`](https://github.com/casework/CASE-Examples/blob/master/examples/illustrations/exif_data/exif_data.json)
                           * [`network_connection.json`](https://github.com/casework/CASE-Examples/blob/master/examples/illustrations/network_connection/network_connection.json)
         * [`uco-core:UcoObject`](https://ontology.unifiedcyberontology.org/uco/core/UcoObject)
            * Subclasses:
               * [`uco-role:Role`](https://ontology.unifiedcyberontology.org/uco/role/Role)
                  * Usage:
                     * CASE Examples:
                        * [`Oresteia.json`](https://github.com/casework/CASE-Examples/blob/master/examples/illustrations/Oresteia/Oresteia.json)
                        * [`reconstructed_file.json`](https://github.com/casework/CASE-Examples/blob/master/examples/illustrations/reconstructed_file/reconstructed_file.json)
                        * [`spear_phishing.json`](https://github.com/casework/CASE-Examples/blob/master/examples/illustrations/spear_phishing/spear_phishing.json)
                     * CASE website:
                        * [`crossover_heist.json`](https://caseontology.org/examples/crossover_heist/crossover_heist.json)
                        * [`crossover_wmd.json`](https://caseontology.org/examples/crossover_wmd/crossover_wmd.json)
                        * [`hardware_duplicator.json`](https://caseontology.org/examples/hardware_duplicator/hardware_duplicator.json)
                  * Subclasses:
                     * [`case-investigation:Subject`](https://ontology.caseontology.org/case/investigation/Subject)
                        * CASE Examples:
                           * [`forensic_lifecycle.json`](https://github.com/casework/CASE-Examples/blob/master/examples/illustrations/forensic_lifecycle/forensic_lifecycle.json)
                     * [`uco-role:MaliciousRole`](https://ontology.unifiedcyberontology.org/uco/role/MaliciousRole)
                        * Usage:
                           * CASE Examples:
                              * [`spear_phishing.json`](https://github.com/casework/CASE-Examples/blob/master/examples/illustrations/spear_phishing/spear_phishing.json)


## Concepts under draft

* `drafting:Quality`
   * Subclasses:
      * `drafting:FileHashQuality`
         * CASE Corpora:
            * [`digitalcorpora-android-7`](https://github.com/casework/CASE-Corpora/tree/main/catalog/datasets/digitalcorpora-android-7#readme)
* `drafting:USBSerialNumber`
   * CASE website:
      * [`crossover_heist.json`](https://caseontology.org/examples/crossover_heist/crossover_heist.json)
