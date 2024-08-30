# Explore Data Visualizations

(data-visualization-portal)=
[Link to Data Visualization Portal](https://visualization.genelab.nasa.gov/data/)

## About Data Visualization

GeneLab has a Data Visualization portal that provides users the ability to interact with the 'omics processed data from space-related studies within GeneLab's database. The portal encompasses various visualization types, including Gene Expression query tables, Dendrograms, Heatmaps, Gene Set Enrichment Analysis and a range of interactive plots including Principal Component Analysis (PCA) plots, Pair plots, and Volcano plots. Each tool offers researchers the flexibility to adjust parameters and explore specific aspects of the data effectively.

## Metadata Dashboard

(metadata-dashboard)=
[Link to Metadata Dashboard](https://visualization.genelab.nasa.gov/data/)

### Filters

The metadata dashboard is designed to help users narrow search results for experimental data. It provides various tools for filtering and displaying results. The main tools for filtering the studies table's results are the pie charts and the filters on the left side of the dashboard. Each section of the pie chart acts as a separate section of filters, and when a filter from the pie chart is selected the results containing that category will automatically populate in the studies table below. A user can make one selection on each pie chart to narrow results in the studies table further.


```{image} ../../_static/images/data_viz/data-visualization-portal-metadata-dashboard.png
:alt: Metadata dashboard overview
:width: 800px
```

In addition to the pie charts, there are specific filters on the left side of the dashboard that can be selected to narrow down results. When selecting filters on the pie charts, both sections will be updated to show the selected filters and the studies table will be updated to show the relevant studies. When selecting filters on the sidebar, sections will be updated after clicking on the "Apply filters" button, this allows the user to select multiple filters.

By default, the "Show only studies with processed data" filter is selected. Studies with processed data have the necessary data to display the visualization plots or combine multiple studies. The user can remove this filter to display information about all available studies in the repository.

```{image} ../../_static/images/data_viz/data-visualization-portal-processed-data-filter.png
:alt: Show only studies with processed data filter
:width: 300px
```

Another tool that is provided with each individual pie chart is the crosshair icon located on the bottom-left of the chart. When you select the crosshair icon a bar graph displaying the different categories listed within the Pie chart will appear.

```{image} ../../_static/images/data_viz/data-visualization-portal-studies-by-factor.png
:alt: Bar graph display of pie chart categories
:width: 800px
```

Hovering the mouse over the graph will cause the plotly options to appear in the top right corner, and allows you to zoom, select, expand, and export the graph.

```{image} ../../_static/images/data_viz/data-visualization-portal-studies-by-factor-plot.png
:alt: Plotly options for graph interaction
:width: 800px
```

The bar graph is an additional way to display the number of results each category has, and when a bar is selected from the bar graph a new graph will be displayed with the subcategories included in the selected value. The below example shows the breakdown of choosing "Time" from the bar graph selection.

```{image} ../../_static/images/data_viz/data-visualization-portal-studies-by-factor-level.png
:alt: Breakdown of Time category in bar graph
:width: 800px
```

After selecting the desired filter from the bar graph, the user can press the "Apply filter" button to update the results within the studies table.

When a filter is selected, a red "X" will also appear next to the crosshair of the associated pie chart. Pressing the red "X" button will clear the selected filters.

```{image} ../../_static/images/data_viz/data-visualization-portal-results-factors.png
:alt: Clear filter option
:width: 800px
```

The "Clear all filters" button at the top left can be used to remove all selected filters at once.

### Studies Table

Below the pie charts is a table that lists the studies resulting from the selected filters from above. The table includes the following information for each study: OSD, Title, Assay, Organism, Tissue, and Factor.

```{image} ../../_static/images/data_viz/data-visualization-portal-studies-tables.png
:alt: Studies table
:width: 800px
```

By default, the studies will be listed in order of OSD-# from smallest to largest, but the order can be flipped based on each information category (i.e. column header) by clicking the title of the category twice.

```{image} ../../_static/images/data_viz/data-visualization-portal-studies-tables-sort.png
:alt: Sorted studies table
:width: 800px
```

Finally, once a user has selected a study or multiple studies, they can press the "Visualize Study" button to be directed to the data visualization tools. A user may also select multiple studies to visualize simultaneously in which case a user will be directed to a Multi-Study preview page before being directed to the data visualization tools.

## Single Study Visualization Portal

When a user has selected one study to visualize, they will be directed to the data visualization portal. The following plots are available for each study:

- PCA plot
- Pair plots
- Volcano plot
- Heatmap
- Interactive Differential Gene Expression (DGE) table
- Gene Set Enrichment Analysis (GSEA) plots:
  - Normalized Enrichment Score (NES) Table
  - Enrichment Score Plot
  - Normalized Enrichment Score (NES) Plot
  - Dot Plot
  - Ridge Plot
  - Network Plot
- Ideogram

```{image} ../../_static/images/data_viz/data-visualization-portal-single-study.png
:alt: Single study visualization portal overview
:width: 800px
```

### Sidebar Functions

A sidebar of helpful tools is provided on the left side of the screen.

```{image} ../../_static/images/data_viz/data-visualization-portal-single-study-sidebar.png
:alt: Sidebar functions
:width: 800px
```

The "Study details" button is located at the top of the sidebar. This button pulls up a display with the study information including a small description.

```{image} ../../_static/images/data_viz/data-visualization-portal-single-study-details.png
:alt: Study details display
:width: 800px
```

The display also includes a tab labeled "Samples" that a user can press to see the individual samples and additional information for the study.

```{image} ../../_static/images/data_viz/data-visualization-portal-single-study-sample-info.png
:alt: Samples tab in study details
:width: 800px
```

Below the study details button is a label for each plot provided for a user within the data visualization tool. Clicking these labels will automatically direct the user to the plot associated with the label.

```{image} ../../_static/images/data_viz/data-visualization-portal-single-study-sidebar-labels.png
:alt: Plot labels in sidebar
:width: 800px
```

At the bottom of the sidebar is the default Group selection that is utilized for each plot. These groups represent the factor values used on the pairwise comparisons plots, or used to filter the Volcano plot, Pair plots, Heatmap, DGE table, GSEA, and Ideogram.

```{image} ../../_static/images/data_viz/data-visualization-portal-single-study-sidebar-group-selection.png
:alt: Default group selection
:width: 200px
```

For example, if Group 1 is Ground Control and Group 2 is Space Flight:

- PCA will not change based on group selection because it is calculated using data from all samples.
- Volcano plot will display the Log2 Fold Change and P value between Ground Control samples and Space Flight samples.
- Pair Plot Group 1 will only display Ground Control samples.
- Pair Plot Group 2 will only display Space Flight samples.
- Heatmap will use Log2 Fold Change and Adjusted P value between Ground Control samples and Space Flight samples to filter genes.
- DGE table will display Log2 Fold Change, P value, and Adjusted P value between Ground Control samples and Space Flight samples.
- GSEA will be performed using only Ground Control and Space Flight samples.
- Ideogram will display the Log2 Fold Change and P value between Ground Control samples and Space Flight samples.

A user can modify the groups that are selected by pressing the "Modify Groups" button. This button will open a modal displaying the options for the first group.

```{image} ../../_static/images/data_viz/data-visualization-portal-single-study-modify-groups.png
:alt: Modify groups modal - first group
:width: 800px
```

After the user has selected an option, valid options for the second group will be displayed.

```{image} ../../_static/images/data_viz/data-visualization-portal-single-study-group-selection.png
:alt: Modify groups modal - second group
:width: 800px
```

Once the user has selected an option for both groups, the Update group selection button can be used to update the plots.

```{image} ../../_static/images/data_viz/data-visualization-portal-single-study-update-groups.png
:alt: Update group selection
:width: 800px
```

A feature exclusive to multi-study visualization is the option to download the combined Differential Gene Expression (DGE) table.

DGE refers to the difference in abundance of gene transcripts expressed between two groups. DGE is calculated pairwise for each group in the combined dataset, and groups are defined based on the unique factors associated with each sample.

### Plotly

Plotly is a third-party software that is using data provided by GeneLab to create the interactive visualizations displayed. At the top-right corner of each plot will be options to help a user better visualize the data. Hover over the plot to display these options, as seen in the screenshot below.

```{image} ../../_static/images/data_viz/data-visualization-portal-plotly-example.png
:alt: Plotly options
:width: 800px
```

The house icon within the options will reset the axes of the plots back to default. Users are also provided the option to zoom in/out on each plot as well as auto-scale the graphic. There are two tools provided for data point selection, which are the lasso tool and box tool. Each of these tools provides a shape that will select any data points that fall within them. Lastly, there is a download button in the shape of a camera that will let you download the plot as a PNG file. Hover over the icons to see what each one does as shown below.

```{image} ../../_static/images/data_viz/data-visualization-portal-plotly-toolbar.png
:alt: Plotly tool options
:width: 400px
```

In each plot there is an icon in the top right corner, hover over that icon for a description of what that plot is.

### PCA Plots

[Link to read about PCA plots](https://builtin.com/data-science/step-step-explanation-principal-component-analysis)

PCA stands for Principal Component Analysis, and this type of plot is used to reduce the dimensionality of large sets of data to simplify the process of analyzing the data points.

```{image} ../../_static/images/data_viz/data-visualization-portal-pca-plot.png
:alt: PCA plot example
:width: 800px
```

Each PCA plot will include options for a 2D and 3D representation of the data. The default selection is a 3D representation on an "X", "Y", and "Z" axis.

In the upper left corner of the plot area select the "2D" button and then press "Update" to display the data on an "X", and "Y" axis only as shown below.

```{image} ../../_static/images/data_viz/data-visualization-portal-2d-pca-plot.png
:alt: 2D PCA plot
:width: 800px
```

The "Color by Factor" feature allows users to select a specific factor from the study for representation on the graph to allow for easier comparison between different factors in the data.

Select the "Color by Factor" drop down menu. Within the drop down menu select one factor, then press the "Update" button.

In the example below, the "spaceflight" factor was selected from the drop down menu.

```{image} ../../_static/images/data_viz/data-visualization-portal-pca-plot-color.png
:alt: PCA plot colored by spaceflight factor
:width: 800px
```

The results will now be represented by colors matching the factor that was selected.

In the example above (OSD-321), the colors represent the different spaceflight conditions from the experiment and clearly show how this could be driving the differences in gene expression between the samples.

The difference will become more apparent by using the "Scale axis using eigenvectors" option. Eigenvectors are vectors that indicate the directions of maximum stretch or compression within data. By applying eigenvectors to the x-, y-, and z-axis, we can scale the axes according to their magnitude of separating apart the samples, which will make it easier to identify the primary source of divergence among the samples, as shown in the example below.

```{image} ../../_static/images/data_viz/data-visualization-portal-pca-plot-eigenvector.png
:alt: PCA plot with eigenvector scaling
:width: 800px
```

Another feature within the PCA plot tool allows users to hide factors by selecting the label located on the right side of the plot.

The labels provided represent the factor values corresponding to each sample. Click on the label "Ground Control" and the data points will be hidden as shown below:

```{image} ../../_static/images/data_viz/data-visualization-portal-pca-plot-labels.png
:alt: PCA plot with hidden factor
:width: 800px
```

Click on the label a second time and the data will return.

### Pair Plots

[Link to read about pair plots](https://medium.com/analytics-vidhya/pairplot-visualization-16325cd725e6#:~:text=Pair%20plot%20is%20used%20to,separation%20in%20our%20data%2Dset.)

Pair plots are used for Exploratory Data Analysis, where the plot visualizes the data in order to find a relationship between variables that can be continuous or categorical. In the data visualization portal, a Pair plot is used to understand the best set of features (e.g. expressed genes) to explain a relationship between two samples.

The default display for the pair plot will be the comparison between two sets of data with a % difference color threshold of 20%. Two plots will be displayed on the dashboard for the ability to compare multiple sets of data simultaneously. The "Group 1" plot will include all the samples in Group 1 and the "Group 2" plot will include all the samples in Group 2. Hover over a dot on the plot to display the gene name and count value for each sample on the pair plot as shown below.

```{image} ../../_static/images/data_viz/Pair_Plot_OSD-321_hover.png
:alt: Default pair plot display
:width: 800px
```

Within the plot, users have the ability to change the % difference color threshold. Below is an example of the color threshold being altered to 40%.

```{image} ../../_static/images/data_viz/Pair_Plot_OSD-321_40pct-diff.png
:alt: Pair plot with 40% color threshold
:width: 800px
```

Clicking each of the drop down menus will allow users to change the samples displayed. By default, the pair of samples with the highest correlation coefficient are shown.

```{image} ../../_static/images/data_viz/Pair_Plot_OSD-321_sample-display.png
:alt: Pair plot sample selection
:width: 800px
```

Users also have the capability to view different data correlations by clicking the green "Samples" button at the top of the plot. Clicking this button will change the dropdown to show multiple correlation coefficients for a set of data. When clicking "Update" the plot will show the pair of samples with the selected correlation coefficient.

```{image} ../../_static/images/data_viz/Pair_Plot_OSD-321_correl-coeff.png
:alt: Pair plot correlation coefficient selection
:width: 800px
```

### Volcano Plots

[Link to read about volcano plots](https://www.htgmolecular.com/blog/2022-08-25/understanding-volcano-plots)

A volcano plot is useful for identifying events (e.g. gene expression) that differ significantly between two groups of experimental subjects. The name volcano plot comes from its resemblance to a volcanic eruption with the most significant points at the top, like spewed pieces of molten lava. Each point on the graph represents a gene. The log2-fold differences between the groups are plotted on the x-axis and the -log10 Adjusted P value differences are plotted on the y-axis. The dots on the plot, representing genes, are color-coded based on the thresholds displayed in the key on the top right corner of the plot.

The default display for Volcano Plots will have the Adj P Value threshold set to 0.05 and Log2 FC threshold set to 1.00 as shown below. Hover over a dot on the plot to show the gene name and x and y values.

```{image} ../../_static/images/data_viz/data-visualization-portal-volcano-plot.png
:alt: Default volcano plot display
:width: 800px
```

The ability to change the Adjusted P value threshold and/or the Log2 FC threshold are available. The image below shows an Adjusted P value threshold increase to 0.1 and the log2 fold-change threshold increase to 2.0.

```{image} ../../_static/images/data_viz/data-visualization-portal-volcano-plot-thresholds.png
:alt: Volcano plot with adjusted thresholds
:width: 800px
```

Users have the ability to change the type of data displayed on the Y axis, and the options from the dropdown menu include P Value, Adjusted P Value, -Log10(P Value), and -Log10(Adj P Value). Below is an example of the "-log10 P value" display for a volcano plot.

```{image} ../../_static/images/data_viz/data-visualization-portal-volcano-plot-displayed-data.png
:alt: Volcano plot with -log10 P value on Y axis
:width: 800px
```

### Heatmap

[Link to read about heatmaps](https://www.htgmolecular.com/blog/2023-05-03/understanding-heat-maps-in-gene-expression-profiling)

Heatmaps allow researchers to quickly and easily identify patterns of gene expression that are associated with specific conditions or treatments and uses color coding to indicate the magnitude of values. By measuring the number of read counts produced by genes in a particular sample, researchers can determine the level of gene expression. The default settings for the heatmap are shown in the image below. The heatmap links genes depending on how alike they are based on the conditions set in the experiment.

```{image} ../../_static/images/data_viz/data_viz_OSD-120_heatmap.png
:alt: Default heatmap display
:width: 800px
```

- Choosing Clustering Method:
  - Users can select a clustering method to display results. The default is set to UPGMA (Unweighted Pair Group Method with Arithmetic Mean).
  - Clustering helps group genes with similar expression profiles, making patterns more apparent. Clustering method options are shown below.

```{image} ../../_static/images/data_viz/data-visualization-portal-heatmap-clustering-method.png
:alt: Clustering method selection
:width: 400px
```

- Toggling Rows and Columns:
  - Users can toggle off the clustering of rows (genes) or columns (samples). This affects how the heatmap links genes based on similarity.
  - The following example shows the heatmap with clustered columns but not rows.

```{image} ../../_static/images/data_viz/data-visualization-portal-heatmap-toggle-data.png
:alt: Heatmap with clustered columns only
:width: 800px
```

- Log2 Transformation:
  - The Log2 transformation is available to enhance the display of differentially expressed genes with smaller gene counts.
  - The Log2 transformation can be toggled off, which could drastically increase the min and max values of the scale making it more difficult to distinguish subtle variations in gene expression between conditions.

- Filtering by Significance:
  - Users can filter the genes displayed on the heatmap based on their significance. By default the heatmap shows only the genes with an Adjusted p-value < 0.05 for the selected group comparison.
  - This filtering helps highlight genes with statistically significant expression changes.
  - If the study has no genes with an Adjusted p-value smaller than the value entered, an error message will be displayed saying "No genes passed through the filtering condition". The user can modify the value and Update the plot.
  - The ability to filter based on Log2FC is also available but is set to off by default.
  - Below is an example with the Adj p Value cutoff set to < 0.0001 and the |Log2FC| cutoff set to > 4.

```{image} ../../_static/images/data_viz/data_viz_OSD-120_heatmap_row-names.png
:alt: Heatmap with clustered columns only
:width: 800px
```


### DGE Table

Each study will have an associated Differential Gene Expression (DGE) table available that includes information on each individual sample from the study.

```{image} ../../_static/images/data_viz/data-visualization-portal-dge-table.png
:alt: DGE table example
:width: 800px
```

Users can sort the table by the different features in the column headers by clicking on the column header of the desired feature (e.g. ENSEMBL, Symbol, Log2FC, P value, or Adjusted P value).

Users can also change the genes displayed in the table by applying either the Maximum p-value threshold or the Maximum adjusted p-value threshold in the top right corner. By default only genes with an adjusted p-value of <= 0.05 are shown. Below is an example of how the table changes with a Maximum adjusted p-value threshold of 0.01.

```{image} ../../_static/images/data_viz/data-visualization-portal-dge-table-thresholds.png
:alt: DGE table with adjusted p-value threshold
:width: 800px
```

To copy or export the Differential Gene Expression (DGE) table from the study visualization page, follow these steps:

1. Copy the Table to Clipboard:
   - Click the "Copy" button above the table on the left. This action will copy the entire table, including all data, headers, and values, to your device's clipboard.

2. Save as CSV, Excel, PDF, or Print:
   - To save the data in various file formats, look for the corresponding buttons above the table on the left.
   - For a CSV file:
     - Locate and click the "CSV" button. This will prompt a download of the DGE table data in CSV format to your device.
   - For an Excel file:
     - Look for the "Excel" button. Click it to initiate the download of the DGE table data in Excel format (XLSX) to your device.
   - For a PDF file:
     - Find and select the "PDF" button. This action will convert the DGE table into a PDF file that you can save to your device.
   - For Printing:
     - Spot the "Print" button. Clicking this will open a new window displaying a printer-friendly version of the DGE table.
     - You can then use your browser's print functionality to print the table directly.

By following these steps, you can export the Differential Gene Expression table data from the study visualization page in a variety of formats. Choose the method that best suits your needs to access and analyze the DGE data efficiently.

### GSEA

[Link to read about GSEA](https://www.pnas.org/doi/10.1073/pnas.0506580102)

GSEA stands for gene set enrichment analysis, a method to identify gene groups that are overrepresented in a large gene set. It uses statistics to pinpoint significantly enriched or depleted gene classes.

```{image} ../../_static/images/data_viz/data-visualization-portal-gsea.png
:alt: GSEA overview
:width: 800px
```

The default Gene set is "KEGG_2019", but this can be changed by selecting a different Gene set from the drop-down menu then clicking "Update". In the example below the Gene set has been changed to "MSigDB_Hallmark_2020".

```{image} ../../_static/images/data_viz/data-visualization-portal-gsea-update-gene-set.png
:alt: GSEA with MSigDB_Hallmark_2020 gene set
:width: 800px
```

Within this GSEA section, there are various parameters you can customize:

1. Choose Gene Sets: Opt for the gene sets to filter from. The default is "KEGG 2019".
   - Learn more about GSEA Gene Sets by browsing the [GSEA Mouse and Human Gene Set database](https://www.gsea-msigdb.org/gsea/msigdb/mouse/genesets.jsp).

2. Permutations: Decide on the number of permutations you desire and whether they're based on phenotypes or gene sets. The default number of Permutations is 300, and the default Permutation type is "Gene set".

3. Gene Number Range: Adjust the minimum and maximum gene set sizes. The minimum threshold omits gene sets with fewer than the specified number of genes, and the maximum threshold omits gene sets with more than the specified number of genes. The default values for min and max size thresholds are 15 and 500, respectively.

4. Weighted Score Type: Defaults to a score type of 1. This value can be changed using the drop-down menu.

5. Statistical Method: Select your preferred statistical method. The default is the t-test. The method can be changed using the drop-down menu. Available methods include, signal-to-noise, t-test, fold change, difference of class, or log2 fold change.

To update the plot with your changes, simply click "Update." Various plot types are available:

- **NES Table:** View different gene sets in a table format. Export this table using the options at the top. The table includes the Enrichment Score (ES), Normalized Enrichment Score (NES), P value (PVAL), False Discovery Rate (FDR), Gene set size, Matched size, and genes for each resulting gene set.

```{image} ../../_static/images/data_viz/data-visualization-portal-gsea-nes-table.png
:alt: NES Table
:width: 800px
```

- **NES Plot:**
  - The default plot displays normalized enrichment scores (NES) based on gene sets.
  - The number of gene sets displayed can be modified by adjusting the number under "Number of gene sets" under the plot options on the left side panel.
  - By default, the gene sets with a false discovery rate (FDR) bigger or equal to 0.25 are displayed in red while the gene sets with an FDR smaller than 0.25 are displayed in blue. FDR indicates the likelihood that a result is a false positive, e.g., FDR of 0.25 means there is a 25% chance that the result is a false positive. This threshold can also be modified.
  - In the example below the plot has been modified to show only the first 20 gene sets ordered by ascending NES and gene sets with an FDR smaller than 0.50 are displayed in blue.

```{image} ../../_static/images/data_viz/data-visualization-portal-gsea-nes-plot.png
:alt: NES Plot
:width: 800px
```

- **Dot Plot:**
  - Similar to NES Plot, it showcases the top gene sets sorted by NES and filtered by FDR.
  - The FDR threshold for gene sets to be displayed can be modified by adjusting the number under "Maximum FDR" on the left side panel.
  - The size of each dot represents the gene ratio, which is the proportion of genes that are differentially expressed with that gene set.
  - The color of each dot represents its FDR, blue being the lowest value and red being the highest.

```{image} ../../_static/images/data_viz/data-visualization-portal-gsea-dot-plot.png
:alt: Dot Plot
:width: 800px
```

- **Ridge Plot:**
  - This reveals the fold change distribution of the top gene sets with an FDR under 0.25 by default.
  - As with previous plots, the number of gene sets displayed and FDR threshold can be modified in the left side panel.
  - The color of each plot represents the FDR value for the gene set, blue being the lowest value and red being the highest value.

```{image} ../../_static/images/data_viz/data-visualization-portal-gsea-ridge-plot.png
:alt: Ridge Plot
:width: 800px
```

- **Network Plot:**
  - Visualize relationships between gene sets using a network plot.
  - The size of each dot represents the gene set size.
  - The color of each dot represents the adjusted p value for the gene set, blue being the lowest value and red being the highest.
  - As with previous plots, the number of gene sets displayed and FDR threshold can be modified on the left side panel.
  - Hovering over one dot will highlight the gene sets it is connected to. The distance between dots can be changed by adjusting the “Dot Attraction Force” on the left side panel. The dots can also be moved around by clicking and dragging them. The example below shows the gene sets connected to “Oxidative Phosphorylation”.

```{image} ../../_static/images/data_viz/OSD-173_GSEA-network.png
:alt: Network Plot
:width: 800px
```

- **GSEA Info:** Displays in-depth details about GSEA creation, statistics, and plot documentation.

```{image} ../../_static/images/data_viz/data-visualization-portal-gsea-info.png
:alt: GSEA Info
:width: 800px
```

With these steps, you can effectively navigate and utilize the GSEA section, gaining insights into gene set enrichment analysis for your study.

### Ideogram

[Link to read about ideograms](https://www.nature.com/scitable/topicpage/chromosome-mapping-idiograms-302/)

Ideograms provide a schematic representation of chromosomes, and they are used to show the relative size of the chromosomes and their characteristic banding patterns.

OSDR ideogram offers three customization options:

- Filter genes by adjusted p-value and/or Log2 FC value, the default values are 0.05 and 1, respectively.
- Change the Annotations layout for the Ideogram using the drop down menu, the Histogram annotations layout is shown by default.

```{image} ../../_static/images/data_viz/data-visualization-portal-ideogram-layout.png
:alt: Ideogram customization options
:width: 200px
```

```{image} ../../_static/images/data_viz/data-visualization-portal-ideogram.png
:alt: Ideogram example
:width: 800px
```

## Multi-Study

```{image} ../../_static/images/data_viz/multi-study_viz_retina.png
:alt: Multi-Study overview
:width: 800px
```

Multi-Study analysis is an advanced tool designed for analyzing and visualizing multiple RNA sequencing studies concurrently. The multi-study page is used to initialize the parameters for data visualization of the multiple studies. Researchers can uncover intricate patterns of gene expression associated with specific conditions or treatments across a variety of experiments.

To combine studies, there are two main steps: selecting the samples and factors you wish to use and running the Differential Gene Expression (DGE) analysis. Factors are used as the groups between which differential expression is calculated.

To help you select the samples and variables to be used as factors, you will be redirected to a page containing the PCA plot for the combined studies, a table to add variables to be used as factors and a table to select samples. This page has the following components:

- Information about how studies were combined and normalized.
- PCA plot of normalized counts.
- PCA plot of unnormalized counts.
- Factor selection table: Displays each studies' values for the variables added to the table.
- Sample selection table
- Option to normalize data using a subset of samples and specific variables as factors.

Below are detailed instructions on how to effectively navigate and utilize the Multi-Study Page:

- Selecting studies for Multi-Study analysis:
  - For your initial test, let's use rodent studies as an example.
  - Start by selecting "rodent" as the organism of interest.
    - *Since combining DNA microarray assays is not yet supported, ensure to filter by both "rodent" and "RNA sequencing" in the assay technology type.*
  - Then select a specific tissue, we'll use retina in this example.
  - Choose multiple different rodent studies containing retina RNAseq data. For this example, OSD-194, OSD-203, OSD-255, and OSD-397 were selected.
  - Mark the checkboxes beside the selected studies in the studies table.
  - Click the "Visualize Study" button to proceed.

```{image} ../../_static/images/data_viz/multi-study_viz_retina_datasets_selection.png
:alt: Selecting studies for Multi-Study analysis
:width: 800px
```

- Data Normalization:
  - A dialog box will appear to prompt you for data normalization options.
  - The default selection is "DESeq2" for normalization, but you can also choose "No Normalization". If normalization is chosen, the sample count data in the studies will be normalized for read depth using the DESeq2 median of ratios method.
    - *Note: Only gene IDs present in all studies will be kept.*
  - If desired, you can enter your email address to receive a notification when the studies have been combined. The email will contain a URL you can use to access the combined studies.
    - Alternatively, proceed without entering an email address.

```{image} ../../_static/images/data_viz/multi-study_viz_retina_datasets_combine.png
:alt: Data normalization options
:width: 800px
```

### Exploring the Multi-Study Page

- Information about how the studies were combined and normalized and the resulting number of samples, genes kept, and discarded genes can be displayed by clicking on the information icon next to the label "Counts were normalized using DESeq2".

```{image} ../../_static/images/data_viz/multi-study_viz_retina_info.png
:alt: Information about study combination
:width: 800px
```

```{image} ../../_static/images/data_viz/multi-study_viz_retina_info-display.png
:alt: Detailed information about normalization
:width: 800px
```

- Add additional variables from the combined dataset as factors by selecting them in the drop-down menu under “Factor Selection” on the right then clicking the “Add” button. Each added factor will be populated as a display option on the PCA plot.


### Multi-Study PCA Plot

- A PCA plot for data visualization will be included on the multi-study page

- If the data was normalized, the "Normalized Counts PCA Plot" title will be displayed at the top.

  - You can use the drop-down menus to change the condition used for the color, shape, and size of each dot on the plot, which represents the samples. The variables available on each drop-down menu are dynamically added when you add variables to the Factors table.

```{image} ../../_static/images/data_viz/multi-study_viz_retina-PCA.png
:alt: Multi-Study PCA Plot options
:width: 800px
```

- The PCA plot axis can be scaled using eigenvectors by selecting that option and clicking "Update"

```{image} ../../_static/images/data_viz/multi-study_viz_retina-PCA-eigenvectors.png
:alt: Multi-Study PCA Plot options
:width: 800px
```

- The PCA plot can be displayed as a 2D or 3D plot

```{image} ../../_static/images/data_viz/multi-study_viz_retina-PCA-eigenvectors-3D.png
:alt: 3D PCA Plot
:width: 800px
```

- You can display the PCA plot of the Unnormalized counts by clicking on the checkbox next to "Show Unnormalized Counts PCA". The unnormalized counts PCA plot has the same features as the normalized counts PCA, it can be displayed as a 2D or 3D plot, the color, shape, and size of the dots can be customized, and the axis can be scaled using eigenvectors.

```{image} ../../_static/images/data_viz/multi-study_viz_retina-PCA-unnorm.png
:alt: Unnormalized Counts PCA Plot
:width: 800px
```

### Factor Selection for Gene Expression Analysis

- The variables selected as factors will be used to group samples and calculate differential expression. The counts table will also be normalized based on these groups.

- For example, in the image below the user has added spaceflight to the factors table. If the user chooses to use spaceflight as a factor, all samples with the spaceflight value as  “Space Flight” will be treated as one group, samples with the spaceflight value as “Ground Control” will be treated as a second group and samples with the spaceflight value as “Basal Control” will be treated as a third group. If any samples do not have the selected factor, “nan” will be added for the value and the samples with the spaceflight value as “nan” will be treated as a fourth group. DGE Analysis will then show pairwise comparisons (Fold Change, p-value, Adjusted p-value) between each of the groups, e.g. Space Flight vs. Ground Control, Space Flight vs. Basal Control, Space Flight vs. nan, etc..

- Any characteristic, parameter, or factor from each studies' metadata can be added to the table. Adding a variable to the table will also add it as an option to use for the color, size, and shape of the PCA plots.

- Under "Factor Selection," choose variables to generate a factors table for differential gene expression analysis.

- Select parameters, characteristics, or factors from the dropdown list to add to the table. The factors, characteristics, and parameters are retrieved from the studies' metadata ISA files. More information about the ISA model and what defines a parameter, characteristic, and factor can be found here [https://isa-specs.readthedocs.io/en/latest/isamodel.html](https://isa-specs.readthedocs.io/en/latest/isamodel.html).

```{image} ../../_static/images/data_viz/multi-study_viz_retina-factors.png
:alt: Factor Selection dropdown
:width: 800px
```

- The table will display the values each study contains for the added variables. If a variable is not common between studies and the information is not available on one of the studies' metadata, the table will display an empty value and the respective values in the samples table below will be filled with “nan” as shown in the next steps.

```{image} ../../_static/images/data_viz/multi-study_viz_retina-factors-add.png
:alt: Factor Selection table
:width: 800px
```

- Variables can be deleted from the table by clicking on the trash icon next to each column header.

```{image} ../../_static/images/data_viz/multi-study_viz_retina-factors-remove.png
:alt: Deleting variables from Factor Selection table
:width: 800px
```

### Sample Selection for Gene Expression Analysis

- Select specific samples by clicking the "Expand table" button.

- This will display a table with all the samples and their values for the variables added to the factors table.

```{image} ../../_static/images/data_viz/multi-study_viz_retina_sample-selection.png
:alt: Sample Selection table
:width: 800px
```

- You can use the checkbox next to the Samples table header to select all samples. The search boxes underneath each column header can be helpful to filter samples with a specific value.

```{image} ../../_static/images/data_viz/multi-study_viz_retina_sample-selection-filter.png
:alt: Sample Selection table with search options
:width: 800px
```

- Use the checkbox next to each sample name to select the samples you wish to use on the next steps.

### Normalize Using Only Selected Samples and/or Factors

- You can choose to normalize the combined counts table using only a subset of samples and any factor (or factors) added to the factors table. The PCA plot will be updated, and this can help you make a better decision on which variables to use as factors for DGE analysis.

```{image} ../../_static/images/data_viz/multi-study_viz_retina_norm_using_selected_samples_factors.png
:alt: Sample Selection table with search options
:width: 800px
```

- Click on the Normalize using only selected samples and/or factors button. This will display a modal with the different options for normalization.

```{image} ../../_static/images/data_viz/multi-study_viz_retina_norm_using_selected_samples_factors-display.png
:alt: Normalization options modal
:width: 800px
```

- Use the checkboxes to select the factor or factors you want to use to normalize. Only the samples selected on the samples table will be used.

### Visualizing and Downloading Results

- Next, click "Visualize Studies" to proceed to visualization plots or to download the counts table.

- A modal will be displayed with the options to continue. You can choose to download the unnormalized counts table, download the normalized counts table, or navigate to visualization plots.

```{image} ../../_static/images/data_viz/multi-study_viz_retina_visualize_using_selected_samples_factors-display.png
:alt: Visualization and download options modal
:width: 800px
```

- If you wish to navigate to visualization plots, you can choose which variables you would like to use as factors. Only samples selected on the samples table will be used. You will have the option to enter your email to be notified when the DGE analysis is ready. The email sent will contain a URL you can use to access the visualization plots resulting from the DGE analysis.

- Click the continue button to perform the selected action.

### Exploring Visualization Plots

- Upon completion, the page will direct you to a range of visualization plots and graphs for your data analysis.

```{image} ../../_static/images/data_viz/multi-study_viz_retina_visualizations_landing.png
:alt: Visualization plots overview
:width: 800px
```

- The visualization portal will have the same plots and capabilities as the single study visualization portal described above.

```{image} ../../_static/images/data_viz/multi-study_viz_retina_visualizations_1of6.png
:alt: Multi-Study visualization plot 1 of 6
:width: 400px
```

```{image} ../../_static/images/data_viz/multi-study_viz_retina_visualizations_2of6.png   
:alt: Multi-Study visualization plot 2 of 6
:width: 400px
```

```{image} ../../_static/images/data_viz/multi-study_viz_retina_visualizations_3of6.png   
:alt: Multi-Study visualization plot 3 of 6
:width: 400px
```

```{image} ../../_static/images/data_viz/multi-study_viz_retina_visualizations_4of6.png   
:alt: Multi-Study visualization plot 4 of 6
:width: 400px
```

```{image} ../../_static/images/data_viz/multi-study_viz_retina_visualizations_5of6.png   
:alt: Multi-Study visualization plot 5 of 6
:width: 400px
```

```{image} ../../_static/images/data_viz/multi-study_viz_retina_visualizations_6of6.png   
:alt: Multi-Study visualization plot 6 of 6
:width: 400px
```


With these comprehensive instructions, you are well-equipped to navigate the Multi-Study Page efficiently. This tool empowers you to analyze multiple RNA sequencing studies simultaneously, uncovering complex gene expression patterns and gaining valuable insights into your experimental data.  
