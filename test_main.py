import io
import sys
import unittest
from main import print_field_names

class TestMain(unittest.TestCase):
    def test_print_field_names(self):
        xml_file = "./res/Parking Bay Data.xml"  # Replace with the actual path to your XML file
        # TODO: Create a test XML file with different field names for testing purposes

        # Call the function and capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_field_names(xml_file)
        sys.stdout = sys.__stdout__

        # Assert that the expected field names are printed
        field_names = [
    'nearest_machine',
    'postcode',
    'easting',
    'cashless_identifier',
    'epsg_27700_geojson_geometry',
    'controlled_parking_zone',
    'restriction_type',
    'tariff',
    'road_name',
    'location',
    'times_of_operation',
    'epsg_4326_geojson_geometry',
    'longitude',
    'response',
    'unique_identifier',
    'parking_bay_length_metres',
    'epsg_4326_well_known_text_geometry',
    'organisation_uri',
    'northing',
    'latitude',
    'disclaimer',
    'row',
    'parking_spaces',
    'spatial_accuracy',
    'epsg_27700_well_known_text_geometry',
    'maximum_stay',
    'valid_parking_permits',
    'last_uploaded'
]
        #self.assertEqual(captured_output.getvalue(), "\n".join(field_names) + "\n")
        expected_output = '\n'.join(sorted(field_names)) + '\n'
        captured_output = sorted(captured_output.getvalue().strip())
        print(expected_output)
        # Sort the captured output and compare it with the sorted expected output
        #self.assertEqual(sorted(captured_output.split('\n')), sorted(expected_output.split('\n')))
        #self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
