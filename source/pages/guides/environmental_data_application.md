# View and Download Environmental Data

The [Environmental Data Application (EDA)](https://visualization.osdr.nasa.gov/eda/) allows users to visualize, compare, and download ISS (International Space Station) cabin environmental telemetry data, including temperature, humidity, and CO2, and radiation data from spaceflight missions.

Users can select a specific Rodent Research (RR) mission from the Mission Dashboard on the EDA landing page indicated in the screenshot below.

```{image} ../../_static/images/eda/eda-landing-page.png
:alt: EDA landing page
:width: 800px
```

## Telemetry data

Users can view the Temperature, Relative Humidity, and CO2 values collected from the ISS cabin and respective ground control for the duration of the selected RR mission. Each telemetry data plot is interactive.

Hover over the plot to display the plotly options in the top right corner that can be used to modify the plot display and download the plot as a png, and hover over the values on each plot to display the Month Day, Year, Time (HH:MM), and measurement as shown in the screenshot below.

```{image} ../../_static/images/eda/eda-telemetry-data-plot.png
:alt: EDA telemetry data plot
:width: 800px
```

The values from the ISS and ground control can be toggled on and off by clicking on "ISS" and "Ground" in the legend, respectively. By default, both ISS and ground control values are displayed. The screenshot below shows the display with only the ground control values selected.

```{image} ../../_static/images/eda/eda-telemetry-data-plot-legend.png
:alt: EDA telemetry data plot legend
:width: 800px
```

Users can click the box next to "Display Mission milestones" to add the respective mission milestones to each telemetry plot as shown below.

```{image} ../../_static/images/eda/eda-telemetry-data-plot-mission-milestones.png
:alt: EDA telemetry data plot mission milestones
:width: 800px
```

## Radiation data

Users can view the daily dose of ionizing radiation from Galactic Cosmic Rays (GCR) without the contribution from the South Atlantic Anomaly (SAA) and the daily dose only from the SAA for the duration of the selected RR mission. Each radiation data plot is interactive.

Hover over the plot to display the plotly options in the top right corner that can be used to modify the plot display and download the plot as a png, and hover over the values on each plot to display the Month Day, Year, and measurement as shown in the screenshot below. Click on the "i" next to the plot titles to learn more.

```{image} ../../_static/images/eda/eda-radiation-data-plot.png
:alt: EDA radiation data plot
:width: 800px
```

Users can view the daily dose measurements from GCR without SAA, GCR from SAA, and the Total Radiation Dose on the same interactive plot. These values can be toggled on and off by clicking on "GCR", "SAA", and "Total" in the legend. By default, all 3 values are displayed.

```{image} ../../_static/images/eda/eda-radiation-data-plot-legend.png
:alt: EDA radiation data plot legend
:width: 800px
```

Users can also view an interactive plot of the accumulated radiation dose over the duration of the selected RR mission as shown in the screenshot below.

```{image} ../../_static/images/eda/eda-radiation-data-plot-accumulated.png
:alt: EDA radiation data plot accumulated
:width: 800px
```

Users can click the box next to "Display Mission milestones" to add the respective mission milestones to each radiation plot as shown below.

```{image} ../../_static/images/eda/eda-radiation-data-plot-mission-milestones.png
:alt: EDA radiation data plot mission milestones
:width: 800px
```

## Mission comparison

Users can navigate to "Mission Comparison" in the left side panel to compare the telemetry and radiation data from different RR missions. Select the RR missions of interest from the provided options at the top of the page then select the telemetry data type or radiation data you want to view from the left side panel. The Telemetry and Radiation data plots will populate with the data from the selected RR missions, scaling the launch date to 0 on the x-axis to enable comparison across missions. Similar to single RR mission plots, plotly features are available to modify the plot display and download the plot as a png, users can hover over data points to display information, and RR mission data can be toggled on and off by clicking on the RR missions in the legend as shown in the screenshots below.

Corresponding summary data are shown below each plot in table format. Tables are interactive and can be sorted by clicking on the column headers, searched using the search box, and can be copied, downloaded in Excel, CSV, or PDF formats, or printed using the respective buttons on the top left of the tables as indicated in the screenshots below.

For the Telemetry data plots ISS data are displayed on top with the corresponding ground control data shown below.

```{image} ../../_static/images/eda/eda-mission-comparison-telemetry.png
:alt: EDA mission comparison telemetry
:width: 800px
```

An example of the Radiation data plots and features are shown below.

```{image} ../../_static/images/eda/eda-mission-comparison-radiation.png
:alt: EDA mission comparison radiation
:width: 800px
```

## Data Tables

Users can navigate to "Data Tables" in the left side panel to access the telemetry and radiation data in table format. Select the desired RR mission from the drop-down menu on the left side panel. Available data tables include:

- Summary table containing max, min, mean, standard deviation, and median values for each type of telemetry and radiation data for the select mission
- Telemetry data table with ISS and ground control values for temperature, humidity, and CO2 at each time point of the selected mission
- Radiation data table with the daily GRC dose without SAA contribution, SAA contribution, total, and the accumulated dose over the duration of the selected mission

Tables are interactive and can be sorted by clicking on the column headers, searched using the search box, and can be copied, downloaded in Excel, CSV, or PDF formats, or printed using the respective buttons on the top left of the tables as indicated in the screenshots below.

```{image} ../../_static/images/eda/eda-data-tables.png
:alt: EDA data tables
:width: 800px
```
