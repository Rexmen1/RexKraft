import os
import yaml

# Load blocks from blocks.yml
with open('blocks.yml', 'r') as file:
    blocks = yaml.safe_load(file)

# Function to generate quest YAML
def generate_quest(month, day, block):
    quest_data = {
        "enabled": True,
        "disabled_worlds": ["Spawn", "Events"],
        "disabled_gamemodes": ["CREATIVE", "SPECTATOR"],
        "objective": "BLOCK_BREAK",
        "block_whitelist": [block],
        "leaderboard_refresh": 60,
        "timeline": "SPECIFIC",
        "timezone_options": {
            "automatically_detect": True,
            "force_timezone": "GMT"
        },
        "start_date": f"2024/{month:02d}/{day:02d} 00:00:00",
        "end_date": f"2024/{month:02d}/{day:02d} 23:59:00",
        "challenge": {
            "enabled": False,
            "goal": 2000
        },
        "participation": {
            "automatic": True,
            "cost": 0,
            "join_actions": []
        },
        "start_actions": [
            "[BROADCAST] &b&lTournament: &fThe {} miner &7/tourney &fhas just begun, good luck!".format(block)
        ],
        "end_actions": [
            "[BROADCAST] &b&lChallenge: &fThe {} miner &7/tourney &fhas just ended.".format(block)
        ],
        "rewards": {
            '1': [
                "[MESSAGE] &7You have placed &a1st &7in the daily &7tourney!",
                "[CONSOLE] voucher give randombp 5 {PLAYER}"
            ],
            '2': [
                "[MESSAGE] &7You have placed &b2nd &7in the daily &7tourney!",
                "[CONSOLE] voucher give randombp 3 {PLAYER}"
            ],
            '3': [
                "[MESSAGE] &7You have placed &e3rd &7in the daily &7tourney!",
                "[CONSOLE] voucher give randombp 1 {PLAYER}"
            ]
        }
    }
    return quest_data

# Function to generate menu YAML
def generate_menu_entry(month, day, block):
    return {
        "slot": day // 2, # Distribute slots evenly
        "active": {
            "material": block.upper(),
            "glow": True,
            "item_flags": ["HIDE_ATTRIBUTES"],
            "display_name": f"&b&l{block.upper()} MINER &7[#1]",
            "lore": [
                "&8{START_DAY} {START_MONTH} - {END_DAY} {END_MONTH}",
                "",
                "&a&lYOUR STATS",
                "  &7Blocks Mined: &f{PLAYER_SCORE}",
                "  &7Position: &f#{PLAYER_POSITION}",
                "",
                "&a&lTIME REMAINING",
                "  &f{TIME_REMAINING}",
                "",
                "&a&lREWARDS",
                "  &f1st: &75x Random Mystery Boxes",
                "  &f2nd: &73x Random Mystery Boxes",
                "  &f3rd: &71x Random Mystery Boxes",
                "",
                "&a&lPLAYERS",
                "  &f{LEADER_NAME_1} &7({LEADER_SCORE_FORMATTED_1})",
                "  &f{LEADER_NAME_2} &7({LEADER_SCORE_FORMATTED_2})",
                "  &f{LEADER_NAME_3} &7({LEADER_SCORE_FORMATTED_3})",
                "  &f{LEADER_NAME_4} &7({LEADER_SCORE_FORMATTED_4})",
                "  &f{LEADER_NAME_5} &7({LEADER_SCORE_FORMATTED_5})",
                "",
                "&7&o(( Top 5 updates every 60 seconds ))"
            ]
        },
        "waiting": {
            "material": "ORANGE_STAINED_GLASS_PANE",
            "display_name": f"&b&l{block.upper()} MINER &7[#1]",
            "lore": [
                "&8{START_DAY} {START_MONTH} - {END_DAY} {END_MONTH}",
                "",
                "&a&lREWARDS",
                "  &f1st: &75x Random Mystery Boxes",
                "  &f2nd: &73x Random Mystery Boxes",
                "  &f3rd: &71x Random Mystery Boxes",
                "",
                "&a&lSTARTING IN",
                "  &f{TIME_REMAINING}"
            ]
        },
        "ended": {
            "material": "BARRIER",
            "display_name": f"&b&l{block.upper()} MINER &7[#1]",
            "lore": [
                "&8{START_DAY} {START_MONTH} - {END_DAY} {END_MONTH}",
                "",
                "&a&lYOUR STATS",
                "  &7Blocks Mined: &f{PLAYER_SCORE}",
                "  &7Position: &f#{PLAYER_POSITION}",
                "",
                "&a&lREWARDS",
                "  &f1st: &75x Random Mystery Boxes",
                "  &f2nd: &73x Random Mystery Boxes",
                "  &f3rd: &71x Random Mystery Boxes",
                "",
                "&a&lWINNING PLAYERS",
                "  &f{LEADER_NAME_1} &7({LEADER_SCORE_FORMATTED_1})",
                "  &f{LEADER_NAME_2} &7({LEADER_SCORE_FORMATTED_2})",
                "  &f{LEADER_NAME_3} &7({LEADER_SCORE_FORMATTED_3})",
                "",
                "&cThis tournament has ended!"
            ]
        }
    }

# Function to write YAML to file
def write_yaml(data, filename):
    with open(filename, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

# Main function to generate quests and menu for a specific month
def generate_monthly_quests(month, year, last_block_index):
    # Days in month
    num_days = 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30 if month != 2 else 28

    # Special days
    special_days = [7, 14, 21, 28]

    # Menu entries for the month
    month_menu_entries = {}

    # Generate quests for each day
    for day in range(1, num_days + 1):
        if day % 2 != 0 and day not in special_days:
            block = blocks[last_block_index]
            last_block_index = (last_block_index + 1) % len(blocks)
            quest_filename = f"tournaments/{month:02d}{day:02d}.yml"
            
            # Ensure the tournaments directory exists
            os.makedirs(os.path.dirname(quest_filename), exist_ok=True)
            
            quest_data = generate_quest(month, day, block)
            write_yaml(quest_data, quest_filename)

            menu_entry = generate_menu_entry(month, day, block)
            month_menu_entries[f"{month:02d}{day:02d}"] = menu_entry

    return last_block_index, month_menu_entries

# Generate quests and menu for each month
last_block_index = 0
all_menu_entries = {}
for month in range(1, 13):
    last_block_index, month_menu_entries = generate_monthly_quests(month, 2024, last_block_index)
    all_menu_entries.update(month_menu_entries)

# Write all menu entries to a single menu file
write_yaml(all_menu_entries, "menu.yml")
