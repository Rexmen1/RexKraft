import re

def replace_xxx_with_numbers(filename):
    # Read the content of the YAML file
    with open(filename, 'r') as file:
        content = file.read()

    # Define a function to replace 'xxx' sequentially with numbers, repeating each number three times
    def replace(match):
        nonlocal current_number, repetition_count
        replacement = str(current_number)
        repetition_count += 1
        if repetition_count > 3:
            repetition_count = 1
            current_number += 1
            if current_number > 10:
                current_number = 1
        return replacement

    current_number = 1
    repetition_count = 1
    # Replace 'xxx' with numbers according to the specified pattern
    replaced_content = re.sub(r'\bxxx\b', replace, content)

    # Write the modified content back to the file
    with open(filename, 'w') as file:
        file.write(replaced_content)

# Replace 'xxx' with numbers according to the specified pattern in test.yaml
replace_xxx_with_numbers('test.yaml')
