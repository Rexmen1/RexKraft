import os
import yaml

# Load blocks from blocks.yml
with open('List/blocks.yml', 'r') as file:
    blocks_data = yaml.safe_load(file)

# Create a directory for quests if it doesn't exist
quests_folder = 'Quests'
if not os.path.exists(quests_folder):
    os.makedirs(quests_folder)

# List of amounts for each quest
amounts = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]

# Flag to indicate whether the "Events:" header has been written
events_header_written = False

# Generate quests for each block
for block in blocks_data:
    for amount in amounts:
        event_name = f"{block.lower().replace(' ', '-')}-{amount}"
        quest_data = {
            'one_time': True,
            'type': 'player_statistic',
            'conditions': [
                f'"%statistic_name% == MINE_BLOCK"',
                f'"%block% == {block.upper().replace(" ", "_")}"',
                f'"%new_value% == {amount}"'
            ],
            'actions': {
                'default': [
                    '"centered_message: &a&lAchievement Unlocked!"',
                    '"centered_message:  "',
                    f'"centered_message:  &eMine {amount} {block} Blocks."',
                    '"centered_message:  "',
                    '"centered_message:  &aRewards:"',
                    f'"centered_message:  &7- ${amount * 10}"',
                    f'"console_command: cmi money give %player% {amount * 10}"'
                ]
            }
        }
        quest_file_path = os.path.join(quests_folder, 'mining.yml')
        with open(quest_file_path, 'a') as quest_file:
            if not events_header_written:
                quest_file.write("Events:\n")
                events_header_written = True
            quest_file.write(f"  {event_name}:\n")
            for key, value in quest_data.items():
                if key == 'actions':
                    quest_file.write("    actions:\n")
                    for action_key, action_value in value.items():
                        quest_file.write(f"      {action_key}:\n")
                        for action_line in action_value:
                            quest_file.write(f"        - {action_line}\n")
                elif key == 'conditions':
                    quest_file.write("    conditions:\n")
                    for condition in value:
                        quest_file.write(f"      - {condition}\n")
                else:
                    quest_file.write(f"    {key}: {value}\n")
            quest_file.write('\n')
