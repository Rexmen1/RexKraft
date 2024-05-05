import yaml

# Load data from the YAML file
with open('test.yml', 'r') as file:
    data = yaml.safe_load(file)

# Update the required votes amount for each level
required_votes = 1825
for item_key, item_value in data['items'].items():
    if item_key.startswith('l'):
        required_votes += 25
        for lore_item_index, lore_item in enumerate(item_value['lore']):
            if 'Requires' in lore_item:
                # Replace the required votes amount
                data['items'][item_key]['lore'][lore_item_index] = f"&bRequires: &7{required_votes} Votes"
                break

# Save the changes back to the YAML file
with open('test.yml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)
