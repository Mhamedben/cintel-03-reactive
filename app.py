import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # This package provides the Palmer Penguins dataset
from shiny import render
import pandas as pd
import seaborn as sns

# Use the built-in function to load the Palmer Penguins dataset
# Provides the Palmer Penguins dataset
import palmerpenguins

# Load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

# Title to main page
ui.page_opts(title="Penguin Data MhamedM", fillable=True)

# Use ui.input_selectize() to create a dropdown input to choose a column
with ui.sidebar(open="open"):
    ui.h2("Sidebar")
    ui.input_selectize(
        "selected_attribute",
        "select attribute",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    )
# Use ui.input_numeric() to create a numeric input for the number of Plotly histogram bins
    ui.input_numeric("plotly_bin_count", "plotly bin count", 40)

# Use ui.input_slider() to create a slider input for the number of Seaborn bins
    ui.input_slider("seaborn_bin_count", "seaborn bin count", 1, 40, 20)

# Use ui.input_checkbox_group() to create a checkbox group input to filter the species
    ui.input_checkbox_group(
        "selected_species_list",
        "select species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Gentoo", "Chinstrap"],
        inline=True,
    )
# Use ui.hr() to add a horizontal rule to the sidebar
    ui.hr()

# Use ui.a() to add a hyperlink to the sidebar
    ui.a(
        "Mhamedben's GitHub Repo",
        href="https://github.com/Mhamedben/cintel-02-data/blob/main/app.py",
        target="_blank",
    )

# create a layout to include 2 cards with a data table and data grid
with ui.layout_columns():
    with ui.card(full_screen=True):  # full_screen option to view expanded table/grid
        ui.h2("Penguin Data Table")

        @render.data_frame
        def penguins_datatable():
            return render.DataTable(penguins_df)

# Expanded table/grid
    with ui.card(full_screen=True):  
        ui.h2("Penguin Data Grid")

        @render.data_frame
        def penguins_datagrid():
            return render.DataGrid(penguins_df)


# Added a horizontal rule
ui.hr()

# Create a layout to include 3 cards with different plots
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.h2("Species Plotly Histogram")

        @render_plotly
        def plotly_histogram():
            return px.histogram(
                penguins_df,
                x=input.selected_attribute(),
                nbins=input.plotly_bin_count(),
                color="species",
            )

    with ui.card(full_screen=True):
        ui.h2("Seaborn Histogram")

        @render.plot(alt="Species Seaborn Histogram")
        def seaborn_histogram():
            seaborn_plot = sns.histplot(
                data=penguins_df,
                x=input.selected_attribute(),
                bins=input.seaborn_bin_count(),
                multiple="dodge",
                hue="species",
            )
            seaborn_plot.set_title("Species Seaborn Histogram MhamedM")
            seaborn_plot.set_ylabel("Measurement")

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")
    with ui.card(full_screen=True):
        ui.h2("Species Plotly Scatterplot MhamedM")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
        @render_plotly
        def plotly_scatterplot():
            return px.scatter(
                penguins_df,
                title="Plotly Scatterplot MhamedM",
                x="body_mass_g",
                y="bill_length_mm",
                color="species",
                symbol="species",
            )
