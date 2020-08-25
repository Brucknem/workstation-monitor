import os
import pandas as pd
from pandas import DataFrame
from pathlib import Path
from io import StringIO
from bokeh.models import ColumnDataSource
from bokeh.plotting import output_file, figure, show
from bokeh.models.formatters import DatetimeTickFormatter
from datetime import datetime

timestamp_format = f'%Y/%m/%d %H:%M:%S.%f'

def convert_dataframe_to_column_data_source(df: pd.DataFrame, indices: list) -> ColumnDataSource:
    """Converts a dataframe into ColumnDataSources grouped by the indices other than the timestamp.
    """
    indices_without_timestamp = indices
    indices_without_timestamp.remove('timestamp')
    grouped = df.groupby(indices_without_timestamp)

    cdss = {}

    for key, group in grouped:
        group = group.drop(indices_without_timestamp, axis=1)
        group = group.set_index('timestamp')
        cds = ColumnDataSource(group)
        # cds.data['timestamp'] = cds.data['timestamp'].astype(datetime)
        cdss[key] = cds

    return cdss

def render_bokeh(sources: dict, keys: list, title: str):
    p = figure(x_axis_type='datetime', title=title)
    # p.xaxis.formatter=DatetimeTickFormatter(
    #     hours=["%d %B %Y"],
    #     days=["%d %B %Y"],
    #     months=["%d %B %Y"],
    #     years=["%d %B %Y"],
    # )
    # p.xaxis.major_label_orientation = 0.3

    for name, source in sources.items():
        for key in keys:
            # print(source.data)
            p.line(x='timestamp', y=key, source=source, legend_label=f'{name}', )
        break
    output_file("tmp/line.html")
    show(p)

def get_timestamp_min_max(sources: dict):
    minimum = None
    maximum = None

    for _, source in sources.items():
        timestamps = source.data['timestamp']
        print(timestamps)