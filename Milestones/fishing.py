import os
import yaml

# Function to load block types from blocks.yml
def load_block_types():
    with open('fish.yml', 'r') as file:
        blocks_data = yaml.safe_load(file)
        return blocks_data

# Function to generate quest data
def generate_quest_data(starting_number, block_types):
    quests = [starting_number]
    for _ in range(14):
        starting_number = starting_number * 2
        quests.append(starting_number)
    
    quests_data = {}
    for block_type in block_types:
        for i, milestone in enumerate(quests):
            block_type_formatted = block_type.replace(' ', '_').upper()
            quest_id = f"{block_type_formatted}-{milestone}"
            actions = [
                f"centered_message: &a&lMilestone Unlocked! &7(&b{i + 1}&7)",
                "centered_message:  ",
                f"centered_message:  &eFish {milestone} {block_type} Fish.",
                "centered_message:  ",
                "centered_message:  &aRewards:",
                f"centered_message:  &7- {milestone // 4}x Tokens",
                f"centered_message:  &7- {i + 1}x Random Mystery Box" if i >= 0 else "",
                f"console_command: av user %player% addpoints {milestone // 4}",
                f"console_command: voucher give randombp {i + 1} %player%" if i >= 0 else ""
            ]
            block_actions = actions.copy()
            block_conditions = [
                f"%statistic_name% == FISH_CAUGHT",
                f"%new_value% >= {milestone}"
            ]
            block_quest_data = {
                'type': 'player_statistic',
                'one_time': True,
                'conditions': block_conditions,
                'actions': {
                    'default': block_actions
                }
            }
            quests_data[quest_id] = block_quest_data
    return quests_data

# Function to generate GUI data for each block
def generate_gui_data(block_name, starting_number):
    gui_data = {
        'menu_title': '      &8&m-(*)-&8 Milestones &m-(*)-',
        'open_command': ['stonemilestones'],
        'size': 54,
        'update_interval': 1,
        'items': {}
    }
    slots = [10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25]
    milestone_number = starting_number
    for i, slot in enumerate(slots, start=10):
        reward_tokens = milestone_number // 4
        reward_mystery_boxes = i - 9
        gui_data['items'][str(slot)] = {
            'material': block_name.upper(),
            'amount': reward_mystery_boxes,
            'slot': slot,
            'update': True,
            'display_name': f'&a{block_name.capitalize()} Milestone {milestone_number}',
            'lore': [
                '',
                '&7Progress:',
                f'  &fStats: &b%statistic_mine_block:{block_name}%',
                f'  &fClaimed: &b%conditionalevents_onetime_ready_{block_name.upper()}-{milestone_number}%',
                '',
                '&7Rewards:',
                f'  &f{reward_tokens}x Tokens',
                f'  &f{reward_mystery_boxes}x Random Mystery Box' if i >= 0 else ""
            ]
        }
        milestone_number *= 2
    gui_data['items']['glass'] = {
        'material': 'BLACK_STAINED_GLASS_PANE',
        'slots': ['0-9', '17', '18', '26-48', '50-53'],
        'display_name': '&r '
    }
    gui_data['items']['barrier'] = {
        'material': 'barrier',
        'slots': ['49'],
        'display_name': '&r '
    }
    return gui_data

# Main function to generate and save quests and GUI files for each block
def generate_quests_and_gui(starting_number):
    block_types = load_block_types()
    quests_data = generate_quest_data(starting_number, block_types)
    gui_folder = 'gui/fishing'
    if not os.path.exists(gui_folder):
        os.makedirs(gui_folder)
    for block_name in block_types:
        block_gui_data = generate_gui_data(block_name, starting_number)
        gui_file_path = os.path.join(gui_folder, f'{block_name.lower()}.yml')
        with open(gui_file_path, 'w') as file:
            yaml.dump(block_gui_data, file, default_flow_style=False, sort_keys=False)
    with open('fishing.yml', 'w') as file:
        yaml.dump(quests_data, file, default_flow_style=False, sort_keys=False)

# Example starting number
starting_number = 16

# Generate and save quests and GUI files for each block
generate_quests_and_gui(starting_number)
