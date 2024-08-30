# Use the RadLab Portal and Data API

[RadLab OSDR Visualization Application](https://visualization.osdr.nasa.gov/radlab/gui/data-overview/)

OSDR RadLab centralizes radiation data from multiple spacecrafts and sensors. By linking radiation data with vehicle and time metadata, the application enables efficient data filtering and sorting to facilitate greater contextual understanding for the users. This tool is essential for researchers studying the effects of space radiation.

## Data Overview Page

RadLab initially displays a data overview page summarizing sensors, collection times, and spacecraft. The interactive menu on the left and the drop-down menus at the top of the graph allow users to filter through the radiation data.

```{image} ../../_static/images/radlab/radlab-overview-page.png
:alt: Data overview page
:width: 800px
```

The left-hand navigation bar offers various visualization options, selecting LEO (low Earth orbit) or ISS (International Space Station) causes the graph to focus on the missions associated with those destinations. The example below shows the ISS display, where users can select specific ISS modules from the interactive diagram for radiation data from the sensors that reside there.

```{image} ../../_static/images/radlab/radlab-iss-display.png
:alt: ISS display
:width: 800px
```

Selecting "BLEO" selects studies that are Beyond Low Earth Orbit.

```{image} ../../_static/images/radlab/radlab-bleo-studies.png
:alt: BLEO selection
:width: 800px
```

## RadLab Time Series Line Plots

This page allows you to view the radiation data. To display the time series plots, define the timeframe you want displayed, select the instruments of interest using the checkboxes to the right of the instrument name, and select either a "Linear" or a "Log" scale below the chart. Then click on "Retrieve" to load the data into the graph below.

```{image} ../../_static/images/radlab/radlab-time-series-line-plot.png
:alt: Time series line plots
:width: 800px
```

*Note: You can click on the ["click here"](https://visualization.osdr.nasa.gov/radlab/gui/time-series-plots/#timestamp%3E=2022-03-01T00%3A00&timestamp%3C=2022-03-02T00%3A00&instrument_id=DosTel1%7CDosTel2%7CLidal%7CREM-Lid&absorbed_dose_rate=&plotScale=log&plotScaleLP=log&plotScalePP=log&projection=orthographic&instrumentX=Lidal&instrumentY=REM-Lid) link above the chart to load an example data set, as shown below:*

```{image} ../../_static/images/radlab/radlab-time-series-plot.png
:alt: Example data set
:width: 800px
```

Hover over the plot to display the plotly options in the top right corner that can be used to modify the plot display, and hover over the lines on the plot to display the specific Instrument, Spacecraft, Module, Timestamp, and Absorbed dose rate as shown below.

```{image} ../../_static/images/radlab/radlab-time-series-plot-export.png
:alt: Plotly options and hover information
:width: 800px
```

To change the y-axis scale, click "Linear" or "Log" at the top of the plot followed by the "Update" button. The plot colors can be changed by clicking "Adjust colors" at the top of the plot. Instrument displays can be toggled on and off by clicking on the instrument name in the legend.

To export the data, select the CSV, TSV, JSON, or HTML link at the top of the plot to download the data in the respective format.

To export the plot, select the PNG, SVG, or PDF link at the top of the plot to download the plot in the respective file type.

## Data Comparison

This page allows you to compare the radiation data from 2 different sensors over a specified time period. To display the data comparison plots, define the time periods you want displayed, select the 2 instruments you want to compare using the checkboxes to the right of the instrument name, and select either a "Linear" or a "Log" scale below the chart. Then click on "Retrieve" to load the data into the graph below.

```{image} ../../_static/images/radlab/radlab-data-comparison.png
:alt: Data comparison
:width: 800px
```

The user can switch which instrument is displayed on the x- and y-axes of the pair plot by clicking "Switch" then "Update" to refresh the data in the graph as shown below.

```{image} ../../_static/images/radlab/radlab-plot-axes.png
:alt: Switching axes
:width: 800px
```

Hover over the plots to show different features:

- Hover over each plot to display the plotly options in the top right corner that can be used to modify the plot display.
- Hover over the lines on the timestamp plot to display the specific Instrument, Spacecraft, Module, Timestamp, and Absorbed dose rate as shown below.
- Hover over a dot on the pair plot to display the timestamp and the Absorbed dose rate for each instrument.
- Hover over the red dotted line on the pair plot to display the R^2 value.

```{image} ../../_static/images/radlab/radlab-plot-hover-features.png
:alt: Hover features
:width: 800px
```

In the Timestamp plot, you can select one of the instrument names in the legend to only display values for that instrument as shown below. To change the y-axis scale, click "Linear" or "Log" at the top of the plot followed by the "Update" button. The plot colors can be changed by clicking "Adjust colors" at the top of the plot.

```{image} ../../_static/images/radlab/radlab-plot-instrument-selection.png
:alt: Timestamp plot legend selection
:width: 800px
```

To export the data, select the CSV, TSV, JSON, or HTML link at the top of the plots to download the data in the respective format.

To export the line plot, select the PNG, SVG, or PDF link next to "Export line plot" at the top of the plots to download the plot in the respective file type.

To export the pair plot, select the PNG, SVG, or PDF link next to "Export pair plot" at the top of the plots to download the plot in the respective file type.

## Geospatial Plots

This page allows you to view the data from one instrument on the world map over a specified time period. To display the geospatial plot, define the timeframe you want displayed, select the instrument you want displayed using the check box to the right of the instrument name, and select either a "Linear" or a "Log" scale below the chart. Then click on "Retrieve" to load the data into the graph below.

```{image} ../../_static/images/radlab/radlab-geospatial-plots.png
:alt: Geospatial plot
:width: 800px
```

The "Orthographic" projection on a Log scale is displayed by default, but these can be changed using the Projection and Scale drop-down menus above the plot and clicking "Update". Projection options include: Orthographic, Equirectangular, Equal Earth, and Natural Earth.

```{image} ../../_static/images/radlab/radlab-geospatial-heatmap.png
:alt: Projection options
:width: 800px
```

Large datasets (e.g. a long timeframe such as a year) will be rendered as a heatmap as shown above, whereas small datasets (e.g. a short timeframe such as a day) will be rendered as a scatter plot as shown below.

```{image} ../../_static/images/radlab/radlab-geospatial-scatter-plot.png
:alt: Scatterplot for small datasets
:width: 800px
```

Hover over the plot to display the plotly options in the top right corner that can be used to modify the plot display, and hover over the data points on the plot to display the specific Instrument, Spacecraft, Module, Timestamp, Longitude, Latitude, Altitude, and Absorbed dose rate as shown below.

```{image} ../../_static/images/radlab/radlab-geospatial-scatter-plot-export.png
:alt: Hover information for geospatial plot
:width: 800px
```

The plot colors can be changed by clicking "Adjust colors" at the top of the plot.

To export the data, select the CSV, TSV, JSON, or HTML link at the top of the plot to download the data in the respective format.

To export the plot, select the PNG, SVG, or PDF link at the top of the plot to download the plot in the respective file type.

## Knowledgebase

The knowledge base index provides definitions and more information about each location, sensor, and acronym used in the RadLab portal.

```{image} ../../_static/images/radlab/radlab-knowledge-base.png
:alt: Knowledgebase
:width: 800px
```

## Data API

An API is available to programmatically query and download data hosted on RadLab.

```{image} ../../_static/images/radlab/radlab-data-api.png
:alt: Data API
:width: 800px
```

## Settings

This page provides a list of all instruments in RadLab, along with the data source, the spacecraft, and the color that RadLab uses to define them in the portal. This page also reminds users to clear their "cookies" if they have previously saved any settings.

```{image} ../../_static/images/radlab/radlab-settings.png
:alt: Settings page
:width: 800px
```

Please note that large data requests can take some time to process.

```{image} ../../_static/images/radlab/radlab-requesting-data.png
:alt: Processing notification
:width: 300px
```
