import xml.etree.ElementTree as ET
import pandas as pd

# Currently testing ingress of data from XML file and determining shape of data before building application


def parse_xml_to_list(xml_file):
    """
    Parses an XML file and returns a list of dictionaries containing the data.

    Parameters:
    xml_file (str): The path to the XML file.

    Returns:
    list: A list of dictionaries, where each dictionary represents an element in the XML file.
        The keys of the dictionaries are the XML element tags, and the values are the corresponding text content.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = []
    for element in root:
        data_dict = {}
        for subelement in element:
            data_dict[subelement.tag] = subelement.text
        data.append(data_dict)
    return data


def parse_xml_to_df(xml_file):
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
    Prints rows from a DataFrame parsed from an XML file.

    Parameters:
    xml_file (str): The path to the XML file.
    start (int): The index of the start row to print.
    end (int, optional): The index of the end row to print. If not specified, only the start row is printed.

    Returns:
    None
    """
    df = parse_xml_to_df(xml_file)
    if end is None:  # If no end row is specified, print only the start row
        print(df.iloc[start])
    else:  # If an end row is specified, print all rows from start to end-1
        print(df.iloc[start:end])


data = parse_xml_to_list("./res/Parking Bay Data.xml")
df = pd.DataFrame(data)

total_bays = len(df)
print(df.info())

print(f"Total parking bays: {total_bays}")
print_rows("./res/Parking Bay Data.xml", 0, 5)
# average_occupancy = df['parking_bay_length_metres'].mean()  # Replace 'occupancy' with your actual column name
