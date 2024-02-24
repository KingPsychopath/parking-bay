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
    total_rows: int = len(data_frame)
    print(f"Total Rows: {total_rows}")

    tpd.print_rows(data_frame, 0, 5)


if __name__ == "__main__":
    main()
else:
    print("Please do not import this module. Run it directly.")
