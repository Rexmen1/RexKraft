import yaml

def generate_condenser_config(materials):
    condenser_config = {}

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
            'base': {
                'material': 'PLAYER_HEAD',
                'skull-texture': {
                    'value': 'eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvY2VmMTE5ZjA4ODUxYTcyYTVmMTBmYmMzMjQ3ZDk1ZTFjMDA2MzYwZDJiNGY0MTJiMjNjZTA1NDA5Mjc1NmIwYyJ9fX0=',
                    'uuid': '701aa558-c1b0-4eb7-81e4-79b1af25283c'
                },
                'name': f'&c{condensed_name}',
                'lore': [
                    f'&7Crafted from 256 normal {material_name} into',
                    '&7Condensed version. Useful for crafting',
                    '&7gears or higher Tier of material'
                ],
                'hide-enchants': True,
                'revision-id': 1,
                'enchants': {'unbreaking': 1},
                'disable-interaction': True,
                'crafting': {
                    'shaped': {
                        '1': {
                            'input': [f'v {material} - 32.0..|v {material} - 32.0..|v {material} - 32.0..',
                                      f'v {material} - 32.0..|v AIR 0 1..|v {material} - 32.0..',
                                      f'v {material} - 32.0..|v {material} - 32.0..|v {material} - 32.0..']
                        }
                    }
                },
                'craft-permission': f'milestones.mining.condensed_{material}'
            }
        }

        enhanced_config = {
            'base': {
                'material': 'PLAYER_HEAD',
                'skull-texture': {
                    'value': 'eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmI3OGZhNWRlZmU3MmRlYmNkOWM3NmFiOWY0ZTExNDI1MDQ3OWJiOWI0NGY0Mjg4N2JiZjZmNzM4NjEyYiJ9fX0=',
                    'uuid': '701aa558-c1b0-4eb7-81e4-79b1af25283c'
                },
                'name': f'&c{enhanced_name}',
                'lore': [
                    f'&7Crafted from 16 Condensed {material_name} into',
                    '&7Enhanced version. Useful for crafting',
                    '&7gears or higher Tier of material'
                ],
                'hide-enchants': True,
                'revision-id': 1,
                'enchants': {'unbreaking': 1},
                'commands': {
                    'cmd0': {
                        'format': f'mi stations open condenser %player_name%',
                        'delay': 0.0,
                        'console': True
                    }
                },
                'disable-interaction': True,
                'crafting': {
                    'shaped': {
                        '1': {
                            'input': [f'm MATERIAL {condensed_key} 2.0..|m MATERIAL {condensed_key} 2.0..|m MATERIAL {condensed_key} 2.0..',
                                      f'm MATERIAL {condensed_key} 2.0..|v AIR 0 1..|m MATERIAL {condensed_key} 2.0..',
                                      f'm MATERIAL {condensed_key} 2.0..|m MATERIAL {condensed_key} 2.0..|m MATERIAL {condensed_key} 2.0..']
                        }
                    }
                }
            }
        }

        purified_config = {
            'base': {
                'material': 'PLAYER_HEAD',
                'skull-texture': {
                    'value': 'eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTQxMmQyZWMzZDQ1ODEyY2ZkYWMwYjg1NmRlODdmMWQzODM4YzFjNTA5ODM2ZmYyMWEwYTVjZDQ3Yzc5MDY5ZiJ9fX0=',
                    'uuid': '701aa558-c1b0-4eb7-81e4-79b1af25283c'
                },
                'name': f'&c{purified_name}',
                'lore': [
                    f'&7Crafted from 8 Enhanced {material_name} into',
                    '&7Purified version. Useful for crafting',
                    '&7gears or higher Tier of material'
                ],
                'hide-enchants': True,
                'revision-id': 1,
                'enchants': {'unbreaking': 1},
                'commands': {
                    'cmd0': {
                        'format': f'mi stations open condenser %player_name%',
                        'delay': 0.0,
                        'console': True
                    }
                },
                'disable-interaction': True,
                'crafting': {
                    'shaped': {
                        '1': {
                            'input': [f'm MATERIAL {enhanced_key} 1.0..|m MATERIAL {enhanced_key} 1.0..|m MATERIAL {enhanced_key} 1.0..',
                                      f'm MATERIAL {enhanced_key} 1.0..|v AIR 0 1..|m MATERIAL {enhanced_key} 1.0..',
                                      f'm MATERIAL {enhanced_key} 1.0..|m MATERIAL {enhanced_key} 1.0..|m MATERIAL {enhanced_key} 1.0..']
                        }
                    }
                }
            }
        }

        condenser_config[condensed_key] = condensed_config
        condenser_config[enhanced_key] = enhanced_config
        condenser_config[purified_key] = purified_config

    return condenser_config

# Load materials from materials.yml
with open('materials.yml', 'r') as file:
    materials = yaml.safe_load(file)

# Generate condenser config
condenser_config = generate_condenser_config(materials)

# Write condenser config to condenser.yml
with open('condenser.yml', 'w') as file:
    yaml.dump(condenser_config, file, default_flow_style=False, sort_keys=False)

