# Navigate an OSDR Study Page

**Single study:** Use the {doc}`access_osdr_data` tutorial to navigate to a study of interest.

```{image} ../../_static/images/osdr_study/osdr-single-study-page.png
:alt: Single OSD study page
:width: 800px
```

## Navigation panel

To the left of the screen is the navigation panel, which allows users to go directly to a specific section of the study information.
```{image} ../../_static/images/osdr_study/osdr-study-page-navigation-panel.png
:alt: Navigation panel
:width: 300px
```

## Study Overview: OSD ID, Title, GeneLab ID, ALSDA ID and DOI

The top of the page contains the unique study ID (OSD-120, in the example below), followed by the title of the study. If the study contains omics data it will have a unique GeneLab ID (GLDS-120, in the example below), and if the study contains non-omics data (e.g. physiological or phenotypic data) it will have a unique ALSDA ID (LSDS-33, in the example below). The DOI provides a unique identifier for the entire study.

```{image} ../../_static/images/osdr_study/osdr-study-page-study-overview.png
:alt: Study Overview
:width: 800px
```

Clicking on the "Cite this Study" button reveals the reference for the study that should be used when referring to the study in manuscripts, presentations, posters, etc. 

```{image} ../../_static/images/osdr_study/osdr-study-page-cite-study.png
:alt: Cite this Study
:width: 800px
```

## Description: Factor(s), organism, assay(s), project and contact information.

This section provides a description of the experiment, a summary of the factors, the organism used, assays performed and project information.

```{image} ../../_static/images/osdr_study/osdr-study-page-description.png
:alt: Description section
:width: 800px
```

## Experiments

A description and link to the experiment from which the study data was derived.

```{image} ../../_static/images/osdr_study/osdr-study-page-experiments.png
:alt: Experiments section
:width: 800px
```

## Payloads

A description and link to the payload that carried the experiment from which the study data was derived.  

In the example below the payload identifier is CARA, which stands for  "Characterizing Arabidopsis Root Attractions"

```{image} ../../_static/images/osdr_study/osdr-study-page-payloads.png
:alt: Payloads section
:width: 800px
```

## Missions

A description and link to the Mission, including the launch date and vehicle, that the payload was on. In the example below, SpaceX-3 is the Mission associated with this study.

```{image} ../../_static/images/osdr_study/osdr-study-page-missions.png
:alt: Missions section
:width: 800px
```

## Protocols

The protocol section contains all the information related to the procedures and equipment used to process the samples and to perform the assays associated with the study. Click on the Samples or one of the Assay boxes to expand to see the respective details.  

*Note: Each protocol is broken up into subsections describing the protocol used for each sample processing step, or each step of the assay.*

Below is an example of the Samples protocol section:

```{image} ../../_static/images/osdr_study/osdr-study-page-samples-protocol.png
:alt: Samples protocol section
:width: 800px
```

Below is an example of the protocol section for an Image Analysis Assay (associated with a LSDS ID):

```{image} ../../_static/images/osdr_study/osdr-study-page-ia-protocol.png
:alt: Image analysis assay protocol
:width: 800px
```

Below is an example of the protocol section for a RNA Sequencing Assay (associated with a GLDS ID):


*Note: For datasets that contain data processed by the GeneLab team, the processing protocols for those data are available in subsections titled "GeneLab raw data processing protocol" (for raw data QC)  and the "GeneLab <assay_type> data processing protocol" (for processed data and QC) as shown below.* 

```{image} ../../_static/images/osdr_study/osdr-study-page-rnaseq-assay-protocol.png  
:alt: RNA-Seq assay protocol  
:width: 800px
```

```{image} ../../_static/images/osdr_study/osdr-study-page-rnaseq-processing-protocol.png
:alt: RNA-Seq processing protocol   
:width: 800px
```

## Samples

The sample section in the study page contains a sample table detailing the metadata associated with each sample in the study. Information provided includes species, tissue type or organism part, genetic background, age, sex, and treatment group (e.g. Flight or Ground Control). The bottom right-hand corner displays the total number of samples in the study and the number currently shown.

### Selecting sample(s) metadata for export

Use the scroll bar at the bottom of the table to see all the sample metadata columns. Specific columns can be selected for download by clicking on  the "Select Export Columns" button (indicated with the orange dotted line arrow in the screenshot below).

```{image} ../../_static/images/osdr_study/osdr-study-page-exporting-sample-metadata-1.png
:alt: Select samples for metadata export
:width: 800px
```

Once all desired fields are selected, users can click "Export CSV" to download the sample metadata CSV file as shown in the screenshot below. 

```{image} ../../_static/images/osdr_study/osdr-study-page-exporting-sample-metadata-2.png
:alt: Export sample metadata CSV
:width: 800px
```

## Assays

The assay section of the study page contains an assay table, populated with assay-specific metadata, for each assay in the study. Users can click on the "Assay Name" drop-down menu to switch between assays (indicated by the orange arrows in the screenshot below). 

```{image} ../../_static/images/osdr_study/osdr-study-page-assay-selection.png
:alt: Assays section
:width: 800px
```

### Selecting assay metadata for export

Use the scroll bar at the bottom of the table to navigate the assay metadata columns. Specific columns can be selected for download by clicking on  the "Select Export Columns" button (indicated with the orange dotted line arrow in the screenshot below). 

```{image} ../../_static/images/osdr_study/osdr-study-page-exporting-assay-metadata-1.png
:alt: Selecting assays for metadata export
:width: 800px
```

Once all desired fields are selected, users can click the "Export CSV" to download the assay metadata CSV file as shown in the screenshot below. 

```{image} ../../_static/images/osdr_study/osdr-study-page-exporting-assay-metadata-2.png
:alt: Export assay metadata CSV
:width: 800px
```

## Publications

The publication section includes a list of primary publications associated with the study data and their respective links as shown in the screenshot below.

```{image} ../../_static/images/osdr_study/osdr-study-page-publications.png
:alt: Publications section
:width: 800px
```

## Files

The files section allows users to access raw and processed files from each assay in the study. The files are organized into separate folders for each assay, study metadata files, and supplemental materials. Studies that contain GeneLab processed omics data also have a separate folder containing the GeneLab processed data files for the respective omics assay(s) as shown in the screenshot below.

```{image} ../../_static/images/osdr_study/osdr-study-page-files.png
:alt: Files section
:width: 800px
```
 
Click on the top-level folder to expand to view subdirectories and files available for download. Click on the box next to a folder to download all files in that folder, or expand to select individual files for download as shown in the screenshot below. 
 
```{image} ../../_static/images/osdr_study/osdr-study-page-files-dropdown.png
:alt: Files download options
:width: 800px
```
 
## Version History
 
The version history section of the study pages shows the current study version, including the date the version was released and what was changed, including any files added or removed, as shown in the screenshot below. 
 
```{image} ../../_static/images/osdr_study/osdr-study-page-version-history.png
:alt: Version History section
:width: 800px
```
 
To access previous study versions, click on "Show/Hide All Version Information" as shown in the screenshot below. Users can click on the previous version link to navigate to past versions of the study.
 
```{image} ../../_static/images/osdr_study/osdr-study-page-all-version-history.png
:alt: Show/Hide All Version Information
:width: 800px
```
 
## Visualization

Studies that contain GeneLab processed transcriptomics data can view the processed data in a series of interactive tables and plots by navigating to the OSDR visualization portal. See the {doc}`data_visualization_portal` tutorial to learn more. 
