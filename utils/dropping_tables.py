""" This module is used to get the normalised data set.
    It uses the parse_xml and process_df modules to get the data set.
    It drops the columns that are not required and returns the DataFrame.
"""

import pandas as pd
from . import parse_xml as tpx
from . import process_df as tpd


def get_normalised_data_set() -> pd.DataFrame:
    """
    Get the Data Set from the XML file and
    return the DataFrame after dropping columns.
    """
    data_frame: pd.DataFrame = tpx.parse_xml("../data/parking_bay_data.xml")
    data_frame = tpd.drop_columns(
        data_frame,
        [
            "disclaimer",
            "epsg_27700_well_known_text_geometry",
            "epsg_4326_well_known_text_geometry",
            "epsg_27700_geojson_geometry",
            "epsg_4326_geojson_geometry",
            "spatial_accuracy",
            "last_uploaded",
            "location",
            "organisation_uri",
            "unique_identifier",
        ],
    )
    total_rows: int = len(data_frame)
    print(f"Total Rows: {total_rows}")
    print(data_frame.columns.tolist())
    tpd.print_rows(data_frame, 0, 5)
    return data_frame
