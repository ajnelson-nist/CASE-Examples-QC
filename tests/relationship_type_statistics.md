<!--
GENERATED FILE

To revise file contents, edit:
../relationship_type_statistics_md.py
-->

# Relationship type statistics

This table reports summary statistics of instances of `uco-core:Relationship` and all subclasses, among the CASE example sources (the [CASE website gallery](https://caseontology.org/examples/), [CASE-Examples](https://github.com/casework/CASE-Examples/), and [CASE-Corpora](https://github.com/casework/CASE-Corpora/)).  Each row is a count of `Relationship` instances grouped by the constellation of literal-values and types.  E.g. this `Relationship` instance ...

```turtle
kb:Relationship-a8513237-8a1e-4009-beb1-f85bdae30862
	a uco-observable:ObservableRelationship ;
	uco-core:isDirectional true ;
	uco-core:kindOfRelationship "Resolves_To" ;
	uco-core:source kb:Domain-1a138692-8508-4055-9113-e868ea3f3c6e ;
	uco-core:target kb:IPAddress-fe8f8e4e-8851-4b8a-8a1b-1ba3421b967a ;
	.
kb:Domain-1a138692-8508-4055-9113-e868ea3f3c6e
	a uco-observable:DomainName ;
	.
kb:IPAddress-fe8f8e4e-8851-4b8a-8a1b-1ba3421b967a
	a uco-observable:IPv6Address ;
	.
```

... would supply this row to the table, incrementing that row's count:

`uco-core:kindOfRelationship` | `rdf:type`s of Relationship object | `uco-core:isDirectional` | `rdf:type`s of `uco-core:source` | `rdf:type`s of `uco-core:target` | `uco-core:Facet`s
--- | --- | --- | --- | --- | ---
`Resolves_To` | `uco-observable:ObservableRelationship` | `True` | <ul><li>`uco-observable:DomainName`</li></ul> | <ul><li>`uco-observable:IPv6Address`</li></ul> | <ul></ul>

Each of the type columns is a sorted list of all of the pre-inference types associated with the relationship's source, target, or any `Facet` attached directly to the relationship.

Count | `uco-core:kindOfRelationship` | `rdf:type`s of Relationship object | `uco-core:isDirectional` | `rdf:type`s of `uco-core:source` | `rdf:type`s of `uco-core:target` | `uco-core:Facet`s
--- | --- | --- | --- | --- | --- | ---
1 | `Associated_Account` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-observable:DigitalAccount`</li></ul> | <ul><li>`uco-observable:EmailAccount`</li></ul> | <ul></ul>
1 | `Associated_Account` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:ApplicationAccount`</li></ul> | <ul><li>`uco-observable:PhoneAccount`</li></ul> | <ul></ul>
1 | `Associated_Account` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:DigitalAccount`</li></ul> | <ul><li>`uco-observable:EmailAccount`</li></ul> | <ul></ul>
1 | `Associated_Account` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:DigitalAccount`</li></ul> | <ul><li>`uco-observable:PhoneAccount`</li></ul> | <ul></ul>
1 | `Attachment_Of` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:Message`</li></ul> | <ul></ul>
3 | `Attachment_Of` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:Message`</li></ul> | <ul></ul>
1 | `Connected_To` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:Device`</li></ul> | <ul><li>`uco-observable:CellSite`</li></ul> | <ul></ul>
1 | `Contained-Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:ContentData`</li><li>`uco-observable:RecoveredObject`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul></ul>
2 | `Contained-Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:DiskPartition`</li></ul> | <ul></ul>
3 | `Contained_Within` | <ul><li>`prov:Entity`</li><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`prov:Entity`</li><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:FileSystem`</li></ul> | <ul><li>`uco-observable:PathRelationFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:Device`</li></ul> | <ul><li>`uco-observable:PathRelationFacet`</li></ul>
5 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`prov:Entity`</li><li>`uco-observable:DiskPartition`</li></ul> | <ul><li>`drafting:DiskPartitionSystem`</li><li>`prov:Entity`</li></ul> | <ul></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-location:Location`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul></ul>
2 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:DataRangeFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:SQLiteBlobFacet`</li></ul>
4 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:File`</li><li>`uco-observable:Image`</li></ul> | <ul><li>`uco-observable:DataRangeFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:ContentData`</li><li>`uco-observable:RasterPicture`</li></ul> | <ul><li>`uco-observable:RasterPicture`</li></ul> | <ul><li>`uco-observable:DataRangeFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:ContentData`</li><li>`uco-observable:RecoveredObject`</li></ul> | <ul><li>`uco-observable:File`</li><li>`uco-observable:Image`</li></ul> | <ul><li>`uco-observable:DataRangeFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:DigitalAccount`</li></ul> | <ul><li>`uco-observable:ObservableObject`</li></ul> | <ul><li>`drafting:TableRelationFacet`</li><li>`uco-core:Facet`</li><li>`uco-observable:DataRangeFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:DigitalAccount`</li></ul> | <ul><li>`uco-observable:ObservableObject`</li></ul> | <ul><li>`uco-observable:DataRangeFacet`</li></ul>
7 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:DiskPartition`</li></ul> | <ul><li>`drafting:DiskPartitionSystem`</li></ul> | <ul></ul>
5 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:DiskPartition`</li></ul> | <ul><li>`uco-observable:Disk`</li></ul> | <ul></ul>
2 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:DiskPartition`</li></ul> | <ul><li>`uco-observable:File`</li><li>`uco-observable:Image`</li></ul> | <ul><li>`uco-observable:DataRangeFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:DiskPartition`</li><li>`uco-observable:RecoveredObject`</li></ul> | <ul><li>`drafting:DiskPartitionSystem`</li></ul> | <ul></ul>
2 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:EmailAddress`</li></ul> | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:DataRangeFacet`</li></ul>
2 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:EmailAddress`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:DataRangeFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:PathRelationFacet`</li></ul>
2 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:DiskPartition`</li></ul> | <ul><li>`uco-observable:PathRelationFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:File`</li><li>`uco-observable:Image`</li></ul> | <ul><li>`uco-observable:PathRelationFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:FileSystem`</li></ul> | <ul><li>`uco-observable:DataRangeFacet`</li><li>`uco-observable:PathRelationFacet`</li></ul>
6 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:FileSystem`</li></ul> | <ul><li>`uco-observable:PathRelationFacet`</li></ul>
3 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:Image`</li></ul> | <ul><li>`uco-observable:PathRelationFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li><li>`uco-observable:Image`</li></ul> | <ul><li>`uco-observable:DiskPartition`</li><li>`uco-observable:RecoveredObject`</li></ul> | <ul><li>`uco-observable:DataRangeFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:FileSystem`</li></ul> | <ul><li>`prov:Entity`</li><li>`uco-observable:DiskPartition`</li></ul> | <ul></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:FileSystem`</li></ul> | <ul><li>`uco-observable:DiskPartition`</li></ul> | <ul></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:FileSystem`</li></ul> | <ul><li>`uco-observable:DiskPartition`</li><li>`uco-observable:RecoveredObject`</li></ul> | <ul></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:FileSystem`</li></ul> | <ul><li>`uco-observable:File`</li><li>`uco-observable:Image`</li></ul> | <ul><li>`uco-observable:DataRangeFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:FileSystem`</li></ul> | <ul><li>`uco-observable:File`</li><li>`uco-observable:Image`</li></ul> | <ul><li>`uco-observable:DiskPartitionFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:Message`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`drafting:TableRelationFacet`</li><li>`uco-core:Facet`</li><li>`uco-observable:DataRangeFacet`</li></ul>
3 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:NetworkConnection`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:SIMCard`</li></ul> | <ul><li>`uco-observable:Device`</li></ul> | <ul></ul>
3 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:SIMCard`</li></ul> | <ul><li>`uco-observable:MobileDevice`</li></ul> | <ul></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:SIMCard`</li></ul> | <ul><li>`uco-observable:MobileDevice`</li></ul> | <ul><li>`uco-core:ConfidenceFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:SIMCard`</li></ul> | <ul><li>`uco-observable:ObservableObject`</li></ul> | <ul><li>`drafting:TableRelationFacet`</li><li>`uco-core:Facet`</li><li>`uco-observable:DataRangeFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:SMSMessage`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`drafting:TableRelationFacet`</li><li>`uco-core:Facet`</li><li>`uco-observable:DataRangeFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:TableField`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:URL`</li></ul> | <ul><li>`uco-observable:EmailMessage`</li></ul> | <ul></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:URL`</li></ul> | <ul><li>`uco-observable:EventLog`</li></ul> | <ul></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:URLHistory`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`drafting:TableRelationFacet`</li><li>`uco-core:Facet`</li><li>`uco-observable:DataRangeFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:URLHistory`</li><li>`uco-observable:URLHistoryFacet`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`drafting:TableRelationFacet`</li><li>`uco-core:Facet`</li><li>`uco-observable:DataRangeFacet`</li></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:Volume`</li></ul> | <ul><li>`uco-observable:DiskPartition`</li><li>`uco-observable:RecoveredObject`</li></ul> | <ul></ul>
1 | `Contained_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:WindowsRegistryKey`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul></ul>
1 | `Corresponds_to` | <ul><li>`uco-core:Relationship`</li></ul> | `False` | <ul><li>`prov:Entity`</li><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul></ul>
1 | `Corresponds_to` | <ul><li>`uco-core:Relationship`</li></ul> | `False` | <ul><li>`uco-observable:DiskPartition`</li></ul> | <ul><li>`prov:Entity`</li><li>`uco-observable:DiskPartition`</li></ul> | <ul></ul>
1 | `Corresponds_to` | <ul><li>`uco-core:Relationship`</li></ul> | `False` | <ul><li>`uco-observable:DiskPartition`</li><li>`uco-observable:RecoveredObject`</li></ul> | <ul><li>`prov:Entity`</li><li>`uco-observable:DiskPartition`</li></ul> | <ul></ul>
1 | `Corresponds_to` | <ul><li>`uco-core:Relationship`</li></ul> | `False` | <ul><li>`uco-observable:FileSystem`</li></ul> | <ul><li>`uco-observable:FileSystem`</li></ul> | <ul></ul>
1 | `Decoded_From` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:EncodedStreamFacet`</li></ul>
2 | `Decompressed_From` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:CompressedStreamFacet`</li></ul>
1 | `Decrypted_From` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:EncryptedStreamFacet`</li></ul>
1 | `Derived_From` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:Message`</li></ul> | <ul><li>`uco-observable:TableField`</li></ul> | <ul></ul>
2 | `Downloadable_From` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`drafting:S3Object`</li><li>`uco-observable:ArchiveFile`</li></ul> | <ul><li>`case-corpora:DownloadableObject`</li></ul> | <ul></ul>
1 | `Downloadable_From` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`drafting:S3Object`</li><li>`uco-observable:PDFFile`</li></ul> | <ul><li>`case-corpora:DownloadableObject`</li></ul> | <ul></ul>
1 | `Employee_Of` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-identity:Person`</li></ul> | <ul><li>`uco-identity:Organization`</li></ul> | <ul></ul>
1 | `Forensic_Image_Of` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li><li>`uco-observable:Image`</li></ul> | <ul><li>`uco-observable:Device`</li></ul> | <ul></ul>
2 | `Has_Account` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-identity:Person`</li></ul> | <ul><li>`uco-observable:DigitalAccount`</li></ul> | <ul></ul>
2 | `Has_Account` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-identity:Person`</li></ul> | <ul><li>`uco-observable:EmailAccount`</li></ul> | <ul></ul>
1 | `Has_Account` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-observable:Device`</li></ul> | <ul><li>`uco-observable:MobileAccount`</li></ul> | <ul></ul>
1 | `Has_Account` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-observable:Device`</li></ul> | <ul><li>`uco-observable:MobileAccount`</li></ul> | <ul><li>`uco-core:ConfidenceFacet`</li></ul>
1 | `Has_Account` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-observable:Device`</li></ul> | <ul><li>`uco-observable:MobileAccount`</li><li>`uco-observable:PhoneAccount`</li></ul> | <ul></ul>
1 | `Has_Account` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-observable:MobileDevice`</li></ul> | <ul><li>`uco-observable:MobileAccount`</li></ul> | <ul></ul>
1 | `Has_Account` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-observable:MobileDevice`</li></ul> | <ul><li>`uco-observable:MobileAccount`</li><li>`uco-observable:PhoneAccount`</li></ul> | <ul></ul>
1 | `Has_Account` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-identity:Identity`</li></ul> | <ul><li>`uco-observable:ApplicationAccount`</li></ul> | <ul></ul>
1 | `Has_Account` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-identity:Identity`</li></ul> | <ul><li>`uco-observable:EmailAccount`</li></ul> | <ul></ul>
1 | `Has_Account` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-identity:Person`</li></ul> | <ul><li>`uco-observable:DigitalAccount`</li></ul> | <ul></ul>
1 | `Has_Account` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-identity:Person`</li></ul> | <ul><li>`uco-observable:EmailAccount`</li></ul> | <ul></ul>
1 | `Has_Account` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:Contact`</li></ul> | <ul><li>`uco-observable:EmailAccount`</li></ul> | <ul></ul>
2 | `Has_Account` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:Contact`</li></ul> | <ul><li>`uco-observable:PhoneAccount`</li></ul> | <ul></ul>
1 | `Has_Device` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-role:Role`</li></ul> | <ul><li>`uco-observable:Device`</li></ul> | <ul></ul>
3 | `Has_Fragment` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:FragmentFacet`</li></ul>
3 | `Has_Fragment` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:ContentData`</li><li>`uco-observable:RecoveredObject`</li></ul> | <ul><li>`uco-observable:ContentData`</li></ul> | <ul><li>`uco-observable:FragmentFacet`</li></ul>
1 | `Has_Role` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-identity:Identity`</li></ul> | <ul><li>`uco-role:Role`</li></ul> | <ul></ul>
3 | `Has_Role` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-identity:Organization`</li></ul> | <ul><li>`uco-role:Role`</li></ul> | <ul></ul>
7 | `Has_Role` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-identity:Person`</li></ul> | <ul><li>`uco-role:Role`</li></ul> | <ul></ul>
2 | `Initiated` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`case-investigation:InvestigativeAction`</li></ul> | <ul><li>`case-investigation:InvestigativeAction`</li></ul> | <ul></ul>
1 | `Located_At` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-observable:Device`</li></ul> | <ul><li>`uco-location:Location`</li></ul> | <ul><li>`uco-core:ConfidenceFacet`</li></ul>
2 | `Located_At` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:CellSite`</li></ul> | <ul><li>`uco-location:Location`</li></ul> | <ul></ul>
5 | `Mapped_Into` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`case-investigation:InvestigativeAction`</li></ul> | <ul><li>`uco-action:Action`</li></ul> | <ul></ul>
1 | `Member_Of` | <ul><li>`uco-core:Relationship`</li></ul> | `True` | <ul><li>`uco-identity:Person`</li></ul> | <ul><li>`uco-identity:Organization`</li></ul> | <ul></ul>
1 | `Referenced-By` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:DiskPartition`</li></ul> | <ul><li>`uco-observable:DiskPartition`</li><li>`uco-observable:RecoveredObject`</li></ul> | <ul></ul>
1 | `Referenced_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul></ul>
1 | `Referenced_Within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:SIMCard`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`drafting:TableRelationFacet`</li><li>`uco-core:Facet`</li><li>`uco-observable:DataRangeFacet`</li></ul>
2 | `Related_To` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `False` | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:File`</li></ul> | <ul></ul>
12 | `Sends` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`case-corpora:DownloadableObject`</li></ul> | <ul><li>`drafting:S3Object`</li></ul> | <ul></ul>
2 | `Sends` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`case-corpora:DownloadableObject`</li></ul> | <ul><li>`drafting:S3Object`</li><li>`uco-observable:ArchiveFile`</li></ul> | <ul></ul>
1 | `Sends` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`case-corpora:DownloadableObject`</li></ul> | <ul><li>`drafting:S3Object`</li><li>`uco-observable:PDFFile`</li></ul> | <ul></ul>
1 | `Sends` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`case-corpora:DownloadableObject`</li><li>`prov:Entity`</li></ul> | <ul><li>`drafting:S3Object`</li></ul> | <ul></ul>
1 | `Stored_On` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li><li>`uco-observable:Image`</li></ul> | <ul><li>`uco-observable:Device`</li></ul> | <ul><li>`uco-observable:PathRelationFacet`</li></ul>
1 | `Used` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:Computer`</li></ul> | <ul><li>`uco-observable:OperatingSystem`</li></ul> | <ul></ul>
1 | `Used_Operating_System` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`prov:Agent`</li><li>`prov:SoftwareAgent`</li><li>`uco-observable:Device`</li><li>`uco-tool:AnalyticTool`</li></ul> | <ul><li>`uco-observable:OperatingSystem`</li></ul> | <ul></ul>
2 | `contained-within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:DiskPartition`</li></ul> | <ul></ul>
3 | `contained-within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:File`</li></ul> | <ul><li>`uco-observable:File`</li><li>`uco-observable:Image`</li></ul> | <ul></ul>
1 | `contained-within` | <ul><li>`uco-observable:ObservableRelationship`</li></ul> | `True` | <ul><li>`uco-observable:URL`</li></ul> | <ul><li>`uco-observable:ObservableObject`</li></ul> | <ul></ul>
