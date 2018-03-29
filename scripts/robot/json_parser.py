# Converts a string to a JSON object

import json


class Json_parser:

    def parse(self, jsonstring):
        # Check if the string is using a valid JSON format
        try:
            parsed_json = json.loads(jsonstring)
            print("JSON succesfully parsed")
            return parsed_json
        except ValueError:
            print("JSON format not correct")
            return ""
