import json


def verify_input_json(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

            # Check if Resource field contains a single asterisk or a list of resources
            resource_field = data.get("PolicyDocument", {}).get("Statement", [{}])[0].get("Resource", "")
            if isinstance(resource_field, list):
                if "*" in resource_field:
                    return False
                else:
                    return True
            elif resource_field == "*":
                return False
            else:
                return True
    except FileNotFoundError:
        print("File not found.")
        return False
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return False


# Example usage:
input_json_file = "input.json"  # Replace "input.json" with the path to your JSON file
result = verify_input_json(input_json_file)
print("Verification result:", result)
