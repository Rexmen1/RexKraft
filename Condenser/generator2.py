import yaml

def generate_material_config(materials):
    material_configs = {}

    for material in materials:
        material_name = material.replace('_', ' ').title()
        material_key = material.upper()

        condensed_name = f'Condensed {material_name}'
        enhanced_name = f'Enhanced {material_name}'
        purified_name = f'Purified {material_name}'

        condensed_key = f'CONDENSED_{material.upper()}'
        enhanced_key = f'ENHANCED_{material.upper()}'
        purified_key = f'PURIFIED_{material.upper()}'

        condensed_config = {
            'output': {
                'type': 'MATERIAL',
                'id': condensed_key,
                'amount': 1
            },
            'crafting-time': 1,
            'ingredients': [
                'vanilla{type=' + material + ',amount=256}'
            ]
        }

        enhanced_config = {
            'output': {
                'type': 'MATERIAL',
                'id': enhanced_key,
                'amount': 1
            },
            'crafting-time': 1,
            'ingredients': [
                f'mmoitem{{type=MATERIAL,id={condensed_key},amount=16,display="{condensed_name}"}}'
            ]
        }

        purified_config = {
            'output': {
                'type': 'MATERIAL',
                'id': purified_key,
                'amount': 1
            },
            'crafting-time': 1,
            'ingredients': [
                f'mmoitem{{type=MATERIAL,id={enhanced_key},amount=8,display="{enhanced_name}"}}'
            ]
        }

        material_configs[f'condensed_{material}'] = condensed_config
        material_configs[f'enhanced_{material}'] = enhanced_config
        material_configs[f'purified_{material}'] = purified_config

    return material_configs


# Load materials from materials.yml
with open('materials.yml', 'r') as file:
    materials = yaml.safe_load(file)

# Generate material config
material_config = generate_material_config(materials)

# Write material config to stations.yml
with open('stations.yml', 'w') as file:
    yaml.dump(material_config, file, default_flow_style=False, sort_keys=False)

