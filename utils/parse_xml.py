"""
This module contains functions for pre-processing
and parsing XML files for use in the main application.

Functions:
    parse_xml(xml_file: str, return_type: str = "dataframe")
    -> Union[pd.DataFrame, list]
        - Parses an XML file and returns either a pandas DataFrame
          or a list of dictionaries containing the data.

    print_field_names(xml_file: str)
        - Prints the field names present in the XML file.

    print_all_fields(xml_file: str)
        - Prints all the fields in the given XML file.

    print_structure(element, indent=0, start=0, end=None)
        - Recursively prints the structure of an XML element with indentation.
"""

from typing import Union
from xml.etree.ElementTree import Element, ElementTree, parse

# import xml.etree.ElementTree as ET
import pandas as pd


def parse_xml(
    xml_file: str, return_type: str = "dataframe"
) -> Union[pd.DataFrame, list]:
    """
    Parses an XML file and returns either a pandas DataFrame
        or a list of dictionaries containing the data.

    Parameters:
    xml_file (str): The path to the XML file.
    return_type (str): The desired return type.
        Default is 'dataframe'.
        Valid values are 'dataframe' or 'list'.

    Returns:
    object: The parsed data as a pandas DataFrame
        or a list of dictionaries.
    """
    tree: ElementTree = parse(xml_file)
    root: Element = tree.getroot()

    # Skip and ignore the initial <response></response> field
    # TODO - Determine whether to use a WHILE loop to skip any other fields
    if root.tag == "response":
        root = root[0]

    # Print the structure of the XML file up to 5 levels deep
    # print_structure(root, 2, 0, 5)
    data = []
    for element in root:
        data_dict = {}
        for subelement in element:
            data_dict[subelement.tag] = subelement.text
        data.append(data_dict)

    if return_type == "dataframe":
        return pd.DataFrame(data)
    elif return_type == "list":
        return data

    raise ValueError(
        "Invalid return type. " + "Valid values are 'dataframe' or 'list'."
    )


def print_field_names(xml_file: str):
    """
    Prints the field names present in the XML file.

    Args:
      xml_file (str): The path to the XML file.

    Returns:
      None
    """
    tree: ElementTree = parse(xml_file)
    root: Element = tree.getroot()

    tags = set()
    for element in root.iter():
        tags.add(element.tag)

    for tag in tags:
        print(tag)


def print_all_fields(xml_file: str):
    """
    Prints all the fields in the given XML file.

    Args:
      xml_file (str): The path to the XML file.

    Returns:
      None
    """
    tree: ElementTree = parse(xml_file)
    root: Element = tree.getroot()

    for element in root.iter():
        print(f"{element.tag}: {element.text}")


# TODO - Add a parameter to specify the number of levels to print
# TODO - Decouple child elements printed from rows printed


def print_structure(element, indent=0, start=0, end=None):
    """
    Recursively prints the structure of an XML element.

    Args:
        element (Element): The XML element to print the structure of.
        indent (int): The number of spaces to
        indent each level of the structure.
        start (int): The index of the start child to print.
        end (int, optional): The index of the end child to print.
            If not specified, the last index is used.

    Returns:
        None
    """
    text = element.text if element.text is not None else ""
    print(" " * indent + element.tag + ": " + text)
    for i, child in enumerate(element):
        if i >= start:
            if end is None or i < end:
                print_structure(child, indent + 2, start, end)


def main() -> None:
    """
    Testing the parse_xml module.
    """
    data_frame: pd.DataFrame = parse_xml("../data/parking_bay_data.xml")
    total_rows: int = len(data_frame)
    total_columns: int = len(data_frame.columns)
    print(data_frame.head())
    print(data_frame.tail())
    print(f"Total Rows: {total_rows}")
    print(f"Total Columns: {total_columns}")


if __name__ == "__main__":
    main()
