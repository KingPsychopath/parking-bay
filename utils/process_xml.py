"""
This module contains functions for pre-processing
and parsing XML files for use in the main application.

Functions:
    func1() -- does this
    func2() -- does that
"""

import xml.etree.ElementTree as ET
import pandas as pd


def parse_xml_to_list(xml_file: str) -> list:
    """
    Parses an XML file and returns a list of dictionaries containing the data.

    Parameters:
    xml_file (str): The path to the XML file.

    Returns:
    list: A list of dictionaries,
    where each dictionary represents an element in the XML file.
        The keys of the dictionaries are the XML element tags,
        and the values are the corresponding text content.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Skip and ignore the initial <response></response> field
    if root.tag == "response":
        root = root[0]

    # Print the structure of the XML file up to 5 levels deep
    print_structure(root, 0, 0, 5)
    data = []
    for element in root:
        data_dict = {}
        for subelement in element:
            data_dict[subelement.tag] = subelement.text
        data.append(data_dict)
    return data


def parse_xml_to_df(xml_file: str) -> pd.DataFrame:
    """
    Parses an XML file and returns a pandas DataFrame.

    Parameters:
    xml_file (str): The path to the XML file.

    Returns:
    pandas.DataFrame: The parsed data as a DataFrame.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = []
    for element in root:
        data_dict = {}
        for subelement in element:
            data_dict[subelement.tag] = subelement.text
        data.append(data_dict)
    return pd.DataFrame(data)


def print_field_names(xml_file):
    """
    Prints the field names present in the XML file.

    Args:
      xml_file (str): The path to the XML file.

    Returns:
      None
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    tags = set()
    for element in root.iter():
        tags.add(element.tag)

    for tag in tags:
        print(tag)


def print_all_fields(xml_file):
    """
    Prints all the fields in the given XML file.

    Args:
      xml_file (str): The path to the XML file.

    Returns:
      None
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for element in root.iter():
        print(f"{element.tag}: {element.text}")


def print_rows(xml_file, start, end=None):
    """
    Prints rows from a XML file.

    Parameters:
    xml_file (str): The path to the XML file.
    start (int): The index of the start row to print.
    end (int, optional): The index of the end row to print.
    If not specified, only the start row is printed.

    Returns:
    None
    """
    df = parse_xml_to_df(xml_file)
    if end is None:  # If no end row is specified, print only the start row
        print(df.iloc[start])
    else:  # If an end row is specified, print all rows from start to end-1
        print(df.iloc[start:end])


def print_structure(element, indent=0, start=0, end=None):
    """
    Recursively prints the structure of an XML element.

    Args:
        element (Element): The XML element to print the structure of.
        indent (int): The number of spaces to
        indent each level of the structure.
        start (int): The index of the start row to print.
        end (int, optional): The index of the end row to print.
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
