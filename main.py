"""
    Main Method.
    Typical Import Structure -> System, Third Party, Local

"""

# import utils.test_process_xml as xml_processor
from utils import parse_xml as tpx, process_df as tpd


def main() -> None:
    """
    The entry point for the program.
    """
    data_frame: object = tpx.parse_xml("./data/parking_bay_data.xml")
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
        ],
    )
    total_rows: int = len(data_frame)
    print(f"Total Rows: {total_rows}")
    print(data_frame.columns.tolist())


if __name__ == "__main__":
    main()
else:
    print("Please do not import this module. Run it directly.")
