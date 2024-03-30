import unittest
import json
from Intership import verify_input_json  # Import the method from Intership

class TestVerifyInputJSON(unittest.TestCase):
    def test_valid_input(self):
        # Create a temporary JSON file with valid input
        valid_json = {
            "PolicyDocument": {
                "Statement": [
                    {
                        "Resource": "arn:aws:s3:::example_bucket"
                    }
                ]
            }
        }
        with open("valid_input.json", "w") as file:
            json.dump(valid_json, file)

        # Verify the method returns True for valid input
        self.assertTrue(verify_input_json("valid_input.json"))

    def test_invalid_input(self):
        # Create a temporary JSON file with invalid input
        invalid_json = {
            "PolicyDocument": {
                "Statement": [
                    {
                        "Resource": "*"
                    }
                ]
            }
        }
        with open("invalid_input.json", "w") as file:
            json.dump(invalid_json, file)

        # Verify the method returns False for invalid input
        self.assertFalse(verify_input_json("invalid_input.json"))

    def test_invalid_input_with_list(self):
        # Create a temporary JSON file with invalid input containing a list with *
        invalid_json_with_list = {
            "PolicyDocument": {
                "Statement": [
                    {
                        "Resource": ["arn:aws:s3:::example_bucket", "*"]
                    }
                ]
            }
        }
        with open("invalid_input_with_list.json", "w") as file:
            json.dump(invalid_json_with_list, file)

        # Verify the method returns False for invalid input with a list containing *
        self.assertFalse(verify_input_json("invalid_input_with_list.json"))

    def test_file_not_found(self):
        # Verify the method returns False for a non-existent file
        self.assertFalse(verify_input_json("nonexistent_file.json"))

    def test_invalid_json_format(self):
        # Create a temporary JSON file with invalid JSON format
        with open("invalid_json_format.json", "w") as file:
            file.write("invalid JSON")

        # Verify the method returns False for invalid JSON format
        self.assertFalse(verify_input_json("invalid_json_format.json"))

    def test_empty_resource_field(self):
        # Create a temporary JSON file with an empty Resource field
        empty_resource_json = {
            "PolicyDocument": {
                "Statement": [
                    {
                        "Resource": ""
                    }
                ]
            }
        }
        with open("empty_resource_input.json", "w") as file:
            json.dump(empty_resource_json, file)

        # Verify the method returns True for empty Resource field
        self.assertTrue(verify_input_json("empty_resource_input.json"))

    def test_multiple_resources(self):
        # Create a temporary JSON file with multiple resources
        multiple_resources_json = {
            "PolicyDocument": {
                "Statement": [
                    {
                        "Resource": ["arn:aws:s3:::example_bucket", "arn:aws:s3:::another_bucket"]
                    }
                ]
            }
        }
        with open("multiple_resources_input.json", "w") as file:
            json.dump(multiple_resources_json, file)

        # Verify the method returns True for multiple resources
        self.assertTrue(verify_input_json("multiple_resources_input.json"))

    def test_invalid_resource_type(self):
        # Create a temporary JSON file with an invalid type for Resource field
        invalid_type_json = {
            "PolicyDocument": {
                "Statement": [
                    {
                        "Resource": {"invalid_key": "invalid_value"}
                    }
                ]
            }
        }
        with open("invalid_type_input.json", "w") as file:
            json.dump(invalid_type_json, file)

        # Verify the method returns False for invalid resource type
        self.assertFalse(verify_input_json("invalid_type_input.json"))


if __name__ == '__main__':
    unittest.main()