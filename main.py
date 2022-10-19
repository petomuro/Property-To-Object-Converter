import json
from re import sub


def clear_object_unicode(file_path):
    if file_path.endswith('.json'):
        with open(file_path) as f:
            parsed_object = json.load(f)

        text_file = open(file_path, "w")
        text_file.write(str(parsed_object).replace("'", '"'))
        text_file.close()


def camel_case(s):
    s = sub(r"([_\-.])+", " ", s).title().replace(" ", "")

    return ''.join([s[0].lower(), s[1:]])


def clear_object_keys_dots(file_path):
    if file_path.endswith('.json'):
        data = {}

        with open(file_path) as f:
            parsed_object = json.load(f)

        for key, value in parsed_object.items():
            if '_' in key:
                modified_key = camel_case(key)
            elif '-' in key:
                modified_key = camel_case(key)
            elif '.' in key:
                modified_key = camel_case(key)
            else:
                modified_key = key

            data[modified_key] = value

        object_data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        text_file = open(file_path, "w")
        text_file.write(object_data)
        text_file.close()


def convert_properties_to_object(file_path):
    if file_path.endswith('.properties'):
        f = open(file_path)
        lines = f.read().splitlines()
        f.close()
        data = {}

        for i, line in enumerate(lines):
            if line != '':
                arr = line.split("=", 1)
                key = arr[0].strip()
                val = arr[1].strip()
                data[key] = val

        object_data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        text_file = open(file_path.replace('.properties', '') + ".json", "w")
        text_file.write(object_data)
        text_file.close()
        # os.unlink(file_path)


if __name__ == '__main__':
    # file_path = 'property.properties'
    # convert_properties_to_object(file_path)
    # clear_object_keys_dots(file_path)

    # After run first two methods you need to find all \\ in your .json files and replace with \ manually.
    # Then comment all above this comment and uncomment all below this comment. Run.

    file_path = 'property.json'
    clear_object_unicode(file_path)
