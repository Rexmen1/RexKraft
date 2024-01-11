import yaml

# Sample blocks.yml content
blocks_yml_content = """
#Common
- OAK_LOG
- BIRCH_LOG
- JUNGLE_LOG
- SPRUCE_LOG
- DARK_OAK_LOG
- ACACIA_LOG
- MANGROVE_LOG
"""

# Load the blocks.yml content
block_data = yaml.safe_load(blocks_yml_content.split('\n'))

# Initialize dictionaries to store common and rare blocks
common_blocks = {}
rare_blocks = {}

# Variables to track current rarity while iterating through the block_data
current_rarity = None

# Iterate through the block_data to categorize common and rare blocks
for block in block_data:
    if block.startswith("#Common"):
        current_rarity = 'common'
    elif block.startswith("#Rare"):
        current_rarity = 'rare'
    else:
        if current_rarity == 'common':
            common_blocks[block] = True
        elif current_rarity == 'rare':
            rare_blocks[block] = True

# Function to generate the required-progress range based on rarity
def get_required_progress_range(rarity):
    if rarity == 'common':
        return (256, 1024)
    elif rarity == 'rare':
        return (32, 64)
    else:
        return (0, 0)  # Default, if the rarity is not recognized

# List to store quest data
quest_list = []

# Iterate through the common_blocks and rare_blocks to generate quests
for block in common_blocks.keys():
    required_progress_range = get_required_progress_range('common')
    quest_data = {
        'name': f'Common Block Quest - {block}',
        'type': 'block-break',
        'variable': block,
        'required-progress': required_progress_range,
        'points': 8,
        'anti-abuse': True,
        'item': {
            'material': block,
            'name': f'&e&lQUEST: &f{block} Miner',
            'lore': [
                '&8 » &7To complete this quest, you must',
                f'&8 » &7Mine &3{required_progress_range[0]}-{required_progress_range[1]} {block} blocks.',
                '',
                '&e&lINFORMATION',
                '&8 » &7Type: &fFree',
                '&8 » &7EXP: &f8x',
                '&8 » &7%total_progress%&7/&e%required_progress%',
                '',
                '%progress_bar% &7(&a%percentage_progress%&7)'
            ]
        }
    }
    quest_list.append(quest_data)

for block in rare_blocks.keys():
    required_progress_range = get_required_progress_range('rare')
    quest_data = {
        'name': f'Rare Block Quest - {block}',
        'type': 'block-break',
        'variable': block,
        'required-progress': required_progress_range,
        'points': 8,
        'anti-abuse': True,
        'item': {
            'material': block,
            'name': f'&e&lQUEST: &f{block} Miner',
            'lore': [
                '&8 » &7To complete this quest, you must',
                f'&8 » &7Mine &3{required_progress_range[0]}-{required_progress_range[1]} {block} blocks.',
                '',
                '&e&lINFORMATION',
                '&8 » &7Type: &fFree',
                '&8 » &7EXP: &f8x',
                '&8 » &7%total_progress%&7/&e%required_progress%',
                '',
                '%progress_bar% &7(&a%percentage_progress%&7)'
            ]
        }
    }
    quest_list.append(quest_data)

# Save the generated quest_list in test1.yml
with open('test1.yml', 'w') as file:
    yaml.dump(quest_list, file, default_flow_style=False)

# Print the generated quest_list
for quest in quest_list:
    print(quest)
