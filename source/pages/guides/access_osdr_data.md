# Access Data in the Open Science Data Repository (OSDR)  

## Searching for data within the OSDR  

The [OSDR repository landing page](https://osdr.nasa.gov/bio/repo) has several different search features as shown below.  

```{image} ../../_static/images/osdr_search/osdr-landing-page-features.png
:alt: OSDR landing page features
:width: 800px
```

1. **The OSDR Toolbar:** Links out to the "OSDR Home page", "Data & Tools", "Research & Resources", "Working Groups" and "Help" menus.  

2. **Keyword Search:** Allows users to search using keywords (e.g., Leaf) and Boolean operators such as "AND", "OR", and "NOT" (e.g., Leaf AND Arabidopsis).  

3. **Search Filters:** Users can select specific Data Source, Data Type, and/or Study Metadata search filters to help target specific datasets. *Described in more detail below.*  

4. **Sort Results:** Search queries are sorted by "Release Date" by default, but can be adjusted to reflect "Relevance", "Accession ID", or "Title".  

5. **Results Display:** Shows the number of search results. The default number of results per page is 25, but this can be increased to 50 or 100.  

6. **Results Icon:** Each search result displays an icon reflecting the associated organism.  

7. **Title:** Search result titles are shown. Users can click on a result title to navigate to that Study page.
   Note: The result titles could link to other Data Types (e.g., Experiment, Subject, Payload, etc.) depending on what was selected in the "Data Type" search filter.  

## General Search Filters  

### Data Source  

Users can specify one or more data sources to search from. Sources include OSDR and federated repositories.  

```{image} ../../_static/images/osdr_search/osdr-data-source-search-filter.png
:alt: OSDR data source search filter
:width: 300px
:align: right
```

OSDR Data Sources (by default these are both selected):  

- **GeneLab:** Search for omics datasets hosted on OSDR  
- **ALSDA:** Search for physiological and phenotypic datasets hosted on OSDR  

Federated Data Sources:  

- **NIH GEO:** Queries datasets hosted on [The National Institutes of Health (NIH) Gene Expression Omnibus (GEO)](https://www.ncbi.nlm.nih.gov/geo/)  
- **EBI PRIDE:** Queries datasets hosted on [The European Bioinformatics Institute (EBI) Proteomics Identification (PRIDE)](https://www.ebi.ac.uk/pride/archive/)  
- **ANL MG-RAST:** Queries datasets hosted on [The Argonne National Laboratory (ANL) Metagenomics Rapid Annotations using Subsystems Technology (MG-RAST)](http://metagenomics.anl.gov/)  

### Data Type  

Users can specify one or more data types to search from.   

```{image} ../../_static/images/osdr_search/osdr-data-type-search-filter.png
:alt: OSDR data type search filter
:width: 300px
:align: right
```

Options include:  

- **Study:** Contains omics (GeneLab) and/or physiological/phenotypic (ALSDA) data and associated metadata derived from one tissue type of an organism (non-plants) or from one organism (plants) of an experiment.  
- **Experiment:** Contains one or more studies and associated reference data including Subject, Biospecimen, Payload, Mission, Hardware, and Vehicle.  
- **Subject:** An individual model organism used in an experiment (e.g., Mouse 1 from Rodent Research 4).  
- **Biospecimen:** A sample derived from a subject (e.g., leaf).  
- **Payload:** Identifier for cargo that carried an experiment to a spacecraft.  
- **Mission:** Spaceflight mission carrying one or more experiments.  
- **Hardware:** Equipment/instruments used in an experiment.  
- **Vehicle:** Vessel that carries payloads to a spacecraft.  

### Study Search Filters  

<div style="overflow: auto; margin-bottom: 20px;">

Users can specify one or more types of study metadata to search from.  

```{image} ../../_static/images/osdr_search/osdr-study-search-filters.png
:alt: OSDR study search filters
:width: 300px
:align: right
```

Options include:  

- **Project Type:** Spaceflight (e.g., ISS, STS), High Altitude (e.g., Parabolic flight, hot air balloon), or Ground (e.g., ground-based cosmic radiation exposure).  
- **Assay Type:** Select from several omics (e.g., RNA sequencing, bisulfite sequencing, mass spectrometry) and physiological/phenotypic (e.g., microscopy, histomorphometry, ultrasonography) assays.  
- **Organism:** Select one or more types of organisms (e.g., Rodent, Human, Plant).  
- **Tissue:** Select one or more tissue types (e.g., liver, seedlings, whole organism).  
- **Factor:** Select from several different experimental factors (e.g., spaceflight, ionizing radiation, light cycle).  

<div style="clear:both"></div>

## Example Search  

The example below shows the results from a multiple-term search that applied the GeneLab and ALSDA "Data Source" filters, the Study "Data Type" filter, and the Spaceflight "Study Search Filter", along with a keyword search of "genome ecotype".  

```{image} ../../_static/images/osdr_search/osdr-example-search.png
:alt: OSDR example search
:width: 800px
```
