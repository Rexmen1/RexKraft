import re
import yaml

def replace_xxx_with_numbers(input_file):
    with open(input_file, 'r') as file:
        data = yaml.safe_load(file)

    # Define a function to replace "xxx" with incremental numbers
    def replace(match):
        nonlocal count
        count += 1
        return str(count)

    count = 0
    # Convert data to string to perform regex substitution
    data_str = yaml.dump(data)
    # Perform the replacement using regular expressions
    modified_data_str = re.sub(r'(?<!\w)xxx(?!\w)', replace, data_str)
    modified_data = yaml.safe_load(modified_data_str)

    output_file = input_file.replace('.yml', 'output.yml')
    with open(output_file, 'w') as file:
        yaml.dump(modified_data, file)

    print(f"Modified data saved to '{output_file}'")

# Replace 'xxx.yml' with the path to your YAML file
replace_xxx_with_numbers('xxx.yml')
