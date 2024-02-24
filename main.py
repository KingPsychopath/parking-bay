"""
    Main Method.
    Typical Import Structure -> System, Third Party, Local

"""

import pandas as pd

# import utils.test_process_xml as xml_processor
from utils import test_process_xml as tpx


def main() -> None:
    """
    The entry point for the program.
    """
    data = tpx.parse_xml_to_list("./data/parking_bay_data.xml")
    df = pd.DataFrame(data)

    total_bays = len(df)
    print(df.info())

    print(f"Total parking bays: {total_bays}")
    tpx.print_rows("./data/parking_bay_data.xml", 0, 5)
    # average_occupancy = df['parking_bay_length_metres'].mean()
    # Replace 'occupancy' with your actual column name


if __name__ == "__main__":
    main()
