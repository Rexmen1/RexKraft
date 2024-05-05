import os
import yaml
import random

# Load mobs.yml file
with open('List/mobs.yml', 'r') as file:
    mobs_data = yaml.load(file, Loader=yaml.FullLoader)

# Load blocks.yml file
with open('List/blocks.yml', 'r') as file:
    blocks_data = yaml.load(file, Loader=yaml.FullLoader)

# Load food.yml file
with open('List/food.yml', 'r') as file:
    food_data = yaml.load(file, Loader=yaml.FullLoader)

# Load smeltable.yml file
with open('List/smeltable.yml', 'r') as file:
    smeltable_data = yaml.load(file, Loader=yaml.FullLoader)

# Load tamable.yml file
with open('List/tamable.yml', 'r') as file:
    tamable_data = yaml.load(file, Loader=yaml.FullLoader)

# Load rideable.yml file
with open('List/rideable.yml', 'r') as file:
    rideable_data = yaml.load(file, Loader=yaml.FullLoader)

# Generate quest for killing mobs
def generate_mob_quest(quest_id, mob_name):
    required_progress = random.randint(16, 64)
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 2100 + 1)
    quest = {
        quest_id: {
            'item': {
                'lore': [
                    "&8 \xBB &7To complete this quest, you must",
                    f"&8 \xBB &7kill &3{required_progress} {mob_name} &7Mobs.",
                    '',
                    '&e&lINFORMATION',
                    "&8 \xBB &7EXP: &f5x",
                    "&8 \xBB &7%total_progress%&7/&e%required_progress%",
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)',
                ],
                'material': 'Stone_Sword',
                'name': f'&e&lQUEST:&f {mob_name} Slayer'
            },
            'name': f'{mob_name} Hunter',
            'points': 5,
            'required-progress': required_progress,
            'type': 'kill-mob',
            'variable': mob_name
        }
    }
    return quest

# Generate quest for mining blocks
def generate_mining_quest(quest_id, block_name):
    required_progress = random.randint(16, 64)
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 2250 + 1)
    quest = {
        quest_id: {
            'anti-abuse': True,
            'item': {
                'lore': [
                    "&8 \xBB &7To complete this quest, you must",
                    f"&8 \xBB &7Mine &3{required_progress} {block_name} &7Blocks.",
                    '',
                    '&e&lINFORMATION',
                    "&8 \xBB &7EXP: &f4x",
                    "&8 \xBB &7%total_progress%&7/&e%required_progress%",
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)',
                ],
                'material': block_name,
                'name': f'&e&lQUEST:&f {block_name} Miner'
            },
            'name': f'{block_name} Miner',
            'points': 4,
            'required-progress': required_progress,
            'type': 'block-break',
            'variable': block_name
        }
    }
    return quest

# Generate quest for placing blocks
def generate_placing_quest(quest_id, block_name):
    required_progress = random.randint(16, 64)
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 2500 + 1)
    quest = {
        quest_id: {
            'anti-abuse': True,
            'item': {
                'lore': [
                    "&8 \xBB &7To complete this quest, you must",
                    f"&8 \xBB &7Place &3{required_progress} {block_name} &7Blocks.",
                    '',
                    '&e&lINFORMATION',
                    "&8 \xBB &7EXP: &f4x",
                    "&8 \xBB &7%total_progress%&7/&e%required_progress%",
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)',
                ],
                'material': block_name,
                'name': f'&e&lQUEST:&f {block_name} Builder'
            },
            'name': f'{block_name} Builder',
            'points': 4,
            'required-progress': required_progress,
            'type': 'block-place',
            'variable': block_name
        }
    }
    return quest

# Generate quest for eating
def generate_eating_quest(quest_id, food_name):
    required_progress = random.randint(16, 64)
    random_amount = random.randint(1, 8)
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 2750 + 1)    
    quest = {
        quest_id: {
            'type': 'consume',
            'name': f'{food_name} Eater',
            'variable': food_name,
            'required-progress': required_progress,
            'points': 4,
            'item': {
                'material': food_name,
                'name': f'&e&lQUEST:&f {food_name} Consumer',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Eat &3{required_progress} {food_name} &7Food.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f4x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

# Generate quest for smelting items
def generate_smelting_quest(quest_id, smeltable_item):
    required_progress = random.randint(16, 64)
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3000 + 1)      
    quest = {
        quest_id: {
            'type': 'smelt',
            'name': f'{smeltable_item} Smelter',
            'variable': smeltable_item,
            'required-progress': required_progress,
            'points': 4,
            'exclusive': 'premium',
            'item': {
                'name': '&e&lQUEST:&f Smelting Expert',
                'material': smeltable_item,
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Smelt &3{required_progress} {smeltable_item} &7items.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7Type: &fPremium',
                    '&8 » &7EXP: &f4x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

# Generate quest for tamable mobs
def generate_taming_quest(quest_id, tamable_mob):
    required_progress = random.randint(16, 64)
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3200 + 1)          
    quest = {
        quest_id: {
            'type': 'tame',
            'name': f'{tamable_mob} Pet',
            'variable': tamable_mob,
            'required-progress': required_progress,
            'points': 4,
            'item': {
                'name': '&e&lQUEST:&f Taming Expert',
                'material': 'FEATHER',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Tame &3{required_progress} {tamable_mob} &7mobs.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f4x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

# Generate quest for rideable mobs
def generate_riding_quest(quest_id, rideable_mob):
    required_progress = random.randint(16, 64)
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3250 + 1)          
    quest = {
        quest_id: {
            'type': 'ride-mob',
            'name': f'{rideable_mob} Riding',
            'variable': rideable_mob,
            'required-progress': required_progress,
            'points': 4,
            'item': {
                'name': '&e&lQUEST:&f Riding Expert',
                'material': 'SADDLE',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Ride &3{required_progress} {rideable_mob} &7mobs.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f4x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_shearing_quest(quest_id):
    required_progress = random.randint(16, 64)
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3300 + 1)          
    quest = {
        quest_id: {
            'type': 'shear',
            'name': 'Sheep Shearer',
            'required-progress': required_progress,
            'points': 4,
            'item': {
                'name': '&e&lQUEST:&f Sheep Shearer',
                'material': 'SHEARS',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Shear &3{required_progress} sheep.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f4x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_milk_quest(quest_id):
    required_progress = random.randint(16, 64)
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3350 + 1)          
    quest = {
        quest_id: {
            'type': 'milk',
            'name': 'Cow Milker',
            'required-progress': required_progress,
            'points': 4,
            'item': {
                'name': '&e&lQUEST:&f Cow Milker',
                'material': 'BUCKET',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Milk &3{required_progress} cows.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f4x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_honey_extract_quest(quest_id):
    required_progress = random.randint(16, 64)
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3400 + 1)          
    quest = {
        quest_id: {
            'type': 'honey-extract',
            'name': 'Honey Extractor',
            'required-progress': required_progress,
            'points': 4,
            'item': {
                'name': '&e&lQUEST:&f Honey Extractor',
                'material': 'GLASS_BOTTLE',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Extract honey from &3{required_progress} hives.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f4x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_honey_comb_extract_quest(quest_id):
    required_progress = random.randint(16, 64)
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3450 + 1)          
    quest = {
        quest_id: {
            'type': 'honey-comb-extract',
            'name': 'Honeycomb Extractor',
            'required-progress': required_progress,
            'points': 4,
            'item': {
                'name': '&e&lQUEST:&f Honeycomb Extractor',
                'material': 'SHEARS',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Extract honeycombs from &3{required_progress} hives.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f4x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_regenerate_quest(quest_id):
    required_progress = random.randint(1, 5)
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3500 + 1)          
    quest = {
        quest_id: {
            'type': 'regenerate',
            'name': 'Regenerator',
            'required-progress': required_progress,
            'points': 2,
            'item': {
                'name': '&e&lQUEST:&f Regenerator',
                'material': 'HEART_OF_THE_SEA',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Regenerate health &3{required_progress} times.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f2x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

def generate_playtime_quest(quest_id):
    required_playtime = random.randint(30, 120)
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3550 + 1)          
    quest = {
        quest_id: {
            'type': 'playtime',
            'name': 'Time Spender',
            'required-playtime': required_playtime,
            'points': 3,
            'item': {
                'name': '&e&lQUEST:&f Time Spender',
                'material': 'CLOCK',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Play for &3{required_playtime} minutes.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f3x',
                    '&8 » &7%total_progress%&7/&e%required_playtime%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

# Generate quest for moving
def generate_move_quest(quest_id):
    required_progress = random.randint(1000, 5000)  # Example range for required distance moved
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3600 + 1)          
    quest = {
        quest_id: {
            'type': 'move',
            'name': 'Adventurous Traveller',
            'required-progress': required_progress,
            'points': 6,
            'item': {
                'name': '&e&lQUEST:&f Adventurous Traveller',
                'material': 'COMPASS',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Move a distance of &3{required_progress} blocks.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f6x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

# Generate quest for swimming
def generate_swim_quest(quest_id):
    required_progress = random.randint(500, 2000)  # Example range for required distance swam
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3650 + 1)          
    quest = {
        quest_id: {
            'type': 'swim',
            'name': 'Water Explorer',
            'required-progress': required_progress,
            'points': 5,
            'item': {
                'name': '&e&lQUEST:&f Water Explorer',
                'material': 'WATER_BUCKET',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Swim a distance of &3{required_progress} blocks.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f5x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

# Generate quest for sprinting
def generate_sprint_quest(quest_id):
    required_progress = random.randint(100, 500)  # Example range for required distance sprinted
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3700 + 1)          
    quest = {
        quest_id: {
            'type': 'sprint',
            'name': 'Speed Demon',
            'required-progress': required_progress,
            'points': 5,
            'item': {
                'name': '&e&lQUEST:&f Speed Demon',
                'material': 'SUGAR',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Sprint a distance of &3{required_progress} blocks.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f5x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

# Generate quest for sneaking
def generate_sneak_quest(quest_id):
    required_progress = random.randint(500, 2000)  # Example range for required time sneaked
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3750 + 1)          
    quest = {
        quest_id: {
            'type': 'sneak',
            'name': 'Stealthy Ninja',
            'required-progress': required_progress,
            'points': 5,
            'item': {
                'name': '&e&lQUEST:&f Stealthy Ninja',
                'material': 'OBSIDIAN',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Sneak for &3{required_progress} seconds.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f5x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

# Generate quest for gliding
def generate_glide_quest(quest_id):
    required_progress = random.randint(500, 2000)  # Example range for required distance glided
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3800 + 1)          
    quest = {
        quest_id: {
            'type': 'glide',
            'name': 'Sky Diver',
            'required-progress': required_progress,
            'points': 6,
            'item': {
                'name': '&e&lQUEST:&f Sky Diver',
                'material': 'ELYTRA',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Glide a distance of &3{required_progress} blocks.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f6x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

# Generate quest for flying
def generate_fly_quest(quest_id):
    required_progress = random.randint(1000, 5000)  # Example range for required distance flown
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3850 + 1)          
    quest = {
        quest_id: {
            'type': 'fly',
            'name': 'Aviator',
            'required-progress': required_progress,
            'points': 7,
            'item': {
                'name': '&e&lQUEST:&f Aviator',
                'material': 'FEATHER',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Fly a distance of &3{required_progress} blocks.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f7x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

# Function to generate a quest for breaking items
def generate_item_break_quest(quest_id):
    required_progress = random.randint(50, 200)  # Example range for number of items broken
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 3900 + 1)          
    quest = {
        quest_id: {
            'type': 'item-break',
            'name': 'Tool Master',
            'required-progress': required_progress,
            'points': 3,
            'item': {
                'name': '&e&lQUEST:&f Tool Master',
                'material': 'IRON_PICKAXE',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Break &3{required_progress} items with a pickaxe.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f3x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

# Function to generate a quest for gaining experience
def generate_gain_experience_quest(quest_id):
    required_progress = random.randint(1000, 5000)  # Example range for experience points required
    adjusted_id = int(quest_id)
    quest_id = str((adjusted_id - 1) + 4000 + 1)          
    quest = {
        quest_id: {
            'type': 'gain-experience',
            'name': 'Experience Hunter',
            'required-progress': required_progress,
            'points': 6,
            'item': {
                'name': '&e&lQUEST:&f Experience Hunter',
                'material': 'EXPERIENCE_BOTTLE',
                'lore': [
                    '&8 » &7To complete this quest, you must',
                    f'&8 » &7Gain a total of &3{required_progress} experience points.',
                    '',
                    '&e&lINFORMATION',
                    '&8 » &7EXP: &f6x',
                    '&8 » &7%total_progress%&7/&e%required_progress%',
                    '',
                    '%progress_bar% &7(&a%percentage_progress%&7)'
                ]
            }
        }
    }
    return quest

# Generate quests using mob names from mobs.yml
generated_mob_quests = {}
for mob_name in mobs_data:
    quest_id = str(len(generated_mob_quests) + 1)
    generated_mob_quests.update(generate_mob_quest(quest_id, mob_name))

# Generate quests using block names from blocks.yml
generated_mining_quests = {}
for block_name in blocks_data:
    quest_id = str(len(generated_mining_quests) + 1)
    generated_mining_quests.update(generate_mining_quest(quest_id, block_name))


# Generate quests using block names from blocks.yml
generated_placing_quests = {}
for block_name in blocks_data:
    quest_id = str(len(generated_placing_quests) + 1)
    generated_placing_quests.update(generate_placing_quest(quest_id, block_name))

# Generate quests using food names from food.yml
generated_food_quests = {}
for food_name in food_data:
    quest_id = str(len(generated_food_quests) + 1)
    generated_food_quests.update(generate_eating_quest(quest_id, food_name))

# Generate quests using smeltable item names
generated_smelting_quests = {}
for smeltable_item in smeltable_data:
    quest_id = str(len(generated_smelting_quests) + 1)
    generated_smelting_quests.update(generate_smelting_quest(quest_id, smeltable_item))

# Generate quests using tamable mobs names
generated_taming_quests = {}
for tamable_mob in tamable_data:
    quest_id = str(len(generated_taming_quests) + 1)
    generated_taming_quests.update(generate_taming_quest(quest_id, tamable_mob))

# Generate quests using rideable mobs names
generated_riding_quests = {}
for rideable_mob in rideable_data:
    quest_id = str(len(generated_riding_quests) + 1)
    generated_riding_quests.update(generate_riding_quest(quest_id, rideable_mob))

# Generate quests for shearing
generated_shearing_quests = {}
quest_id = '1' 
generated_shearing_quests.update(generate_shearing_quest(quest_id)) 

# Generate quests for milking
generated_milk_quests = {}
quest_id = '1' 
generated_milk_quests.update(generate_milk_quest(quest_id)) 

# Generate quests for honey-extract
generated_honey_extract_quests = {}
quest_id = '1' 
generated_honey_extract_quests.update(generate_honey_extract_quest(quest_id)) 

# Generate quests for honey-comb-extract
generated_honey_comb_extract_quests = {}
quest_id = '1' 
generated_honey_comb_extract_quests.update(generate_honey_comb_extract_quest(quest_id)) 

# Generate quests for regenerate
generated_regenerate_quests = {}
quest_id = '1' 
generated_regenerate_quests.update(generate_regenerate_quest(quest_id)) 

# Generate quests for playtime
generated_playtime_quests = {}
quest_id = '1' 
generated_playtime_quests.update(generate_playtime_quest(quest_id)) 

# Generate quests for move
generated_move_quests = {}
quest_id = '1' 
generated_move_quests.update(generate_move_quest(quest_id)) 

# Generate quests for swim
generated_swim_quests = {}
quest_id = '1' 
generated_swim_quests.update(generate_swim_quest(quest_id)) 

# Generate quests for sprint
generated_sprint_quests = {}
quest_id = '1' 
generated_sprint_quests.update(generate_sprint_quest(quest_id)) 

# Generate quests for sneak
generated_sneak_quests = {}
quest_id = '1' 
generated_sneak_quests.update(generate_sneak_quest(quest_id)) 

# Generate quests for glide
generated_glide_quests = {}
quest_id = '1' 
generated_glide_quests.update(generate_glide_quest(quest_id)) 

# Generate quests for fly
generated_fly_quests = {}
quest_id = '1' 
generated_fly_quests.update(generate_fly_quest(quest_id)) 

# Generate quests for item_break
generated_item_break_quests = {}
quest_id = '1' 
generated_item_break_quests.update(generate_item_break_quest(quest_id)) 

# Generate quests for gain_experience
generated_gain_experience_quests = {}
quest_id = '1' 
generated_gain_experience_quests.update(generate_gain_experience_quest(quest_id)) 


# Create 'Quests' folder if it doesn't exist
os.makedirs('Quests', exist_ok=True)

# Save the generated quests in 'Quests/mobs.yml'
with open('Quests/mobs.yml', 'w') as file:
    yaml.dump(generated_mob_quests, file, default_flow_style=False)

# Save the generated quests in 'Quests/mining.yml'
with open('Quests/mining.yml', 'w') as file:
    yaml.dump(generated_mining_quests, file, default_flow_style=False)

# Save the generated quests in 'Quests/building.yml'
with open('Quests/building.yml', 'w') as file:
    yaml.dump(generated_placing_quests, file, default_flow_style=False)

# Save the generated quests in 'Quests/foods.yml'
with open('Quests/foods.yml', 'w') as file:
    yaml.dump(generated_food_quests, file, default_flow_style=False)

# Save the generated smelting quests in 'Quests/smelting.yml'
with open('Quests/smelting.yml', 'w') as file:
    yaml.dump(generated_smelting_quests, file, default_flow_style=False)

# Save the generated smelting quests in 'Quests/taming.yml'
with open('Quests/taming.yml', 'w') as file:
    yaml.dump(generated_taming_quests, file, default_flow_style=False)

# Save the generated smelting quests in 'Quests/taming.yml'
with open('Quests/riding.yml', 'w') as file:
    yaml.dump(generated_riding_quests, file, default_flow_style=False)

# Save the generated smelting quests in 'Quests/shearing.yml'
with open('Quests/shearing.yml', 'w') as file:
    yaml.dump(generated_shearing_quests, file, default_flow_style=False)

# Save the generated milk quests in 'Quests/milk.yml'
with open('Quests/milk.yml', 'w') as file:
    yaml.dump(generated_milk_quests, file, default_flow_style=False) 

# Save the generated honey_extract quests in 'Quests/honey_extract.yml'
with open('Quests/honey_extract.yml', 'w') as file:
    yaml.dump(generated_honey_extract_quests, file, default_flow_style=False)

# Save the generated honey_comb_extract quests in 'Quests/honey_extract.yml'
with open('Quests/honey_comb_extract.yml', 'w') as file:
    yaml.dump(generated_honey_comb_extract_quests, file, default_flow_style=False)

# Save the generated regenerate quests in 'Quests/honey_extract.yml'
with open('Quests/regenerate.yml', 'w') as file:
    yaml.dump(generated_regenerate_quests, file, default_flow_style=False)    

# Save the generated playtime quests in 'Quests/honey_extract.yml'
with open('Quests/playtime.yml', 'w') as file:
    yaml.dump(generated_playtime_quests, file, default_flow_style=False)  

# Save the generated move quests in 'Quests/honey_extract.yml'
with open('Quests/move.yml', 'w') as file:
    yaml.dump(generated_move_quests, file, default_flow_style=False)  

# Save the generated swim quests in 'Quests/honey_extract.yml'
with open('Quests/swim.yml', 'w') as file:
    yaml.dump(generated_swim_quests, file, default_flow_style=False)  

# Save the generated sprint quests in 'Quests/honey_extract.yml'
with open('Quests/sprint.yml', 'w') as file:
    yaml.dump(generated_sprint_quests, file, default_flow_style=False)  

# Save the generated sneak quests in 'Quests/honey_extract.yml'
with open('Quests/sneak.yml', 'w') as file:
    yaml.dump(generated_sneak_quests, file, default_flow_style=False)  

# Save the generated glide quests in 'Quests/honey_extract.yml'
with open('Quests/glide.yml', 'w') as file:
    yaml.dump(generated_glide_quests, file, default_flow_style=False)    

# Save the generated fly quests in 'Quests/honey_extract.yml'
with open('Quests/fly.yml', 'w') as file:
    yaml.dump(generated_fly_quests, file, default_flow_style=False)    

# Save the generated item_break quests in 'Quests/honey_extract.yml'
with open('Quests/item_break.yml', 'w') as file:
    yaml.dump(generated_item_break_quests, file, default_flow_style=False)    

# Save the generated gain_experience quests in 'Quests/honey_extract.yml'
with open('Quests/gain_experience.yml', 'w') as file:
    yaml.dump(generated_gain_experience_quests, file, default_flow_style=False)    

# Combine all generated quests into a single dictionary
all_generated_quests = {}
all_generated_quests.update(generated_mob_quests)
all_generated_quests.update(generated_mining_quests)
all_generated_quests.update(generated_placing_quests)
all_generated_quests.update(generated_food_quests)
all_generated_quests.update(generated_smelting_quests)
all_generated_quests.update(generated_taming_quests)
all_generated_quests.update(generated_riding_quests)
all_generated_quests.update(generated_shearing_quests)
all_generated_quests.update(generated_milk_quests)
all_generated_quests.update(generated_honey_extract_quests)
all_generated_quests.update(generated_honey_comb_extract_quests)
all_generated_quests.update(generated_regenerate_quests)
all_generated_quests.update(generated_playtime_quests)
all_generated_quests.update(generated_move_quests)
all_generated_quests.update(generated_swim_quests)
all_generated_quests.update(generated_sprint_quests)
all_generated_quests.update(generated_sneak_quests)
all_generated_quests.update(generated_glide_quests)
all_generated_quests.update(generated_fly_quests)
all_generated_quests.update(generated_item_break_quests)
all_generated_quests.update(generated_gain_experience_quests)

# Save all generated quests into a single file
with open('Quests/extra.yml', 'w') as file:
    yaml.dump(all_generated_quests, file, default_flow_style=False)

# Combine all generated quests into a single dictionary
mega_quests = {}

# Merge the generated mob quests
mega_quests.update(generated_mob_quests)

# Merge the generated mining quests
mega_quests.update(generated_mining_quests)

# Merge the generated building quests
mega_quests.update(generated_placing_quests)

# Merge the generated food quests
mega_quests.update(generated_food_quests)

# Merge the generated smelting quests
mega_quests.update(generated_smelting_quests)

# Merge the generated taming quests
mega_quests.update(generated_taming_quests)

# Merge the generated riding quests
mega_quests.update(generated_riding_quests)

# Merge the generated shearing quests
mega_quests.update(generated_shearing_quests)

# Merge the generated milk quests
mega_quests.update(generated_milk_quests)

# Merge the generated honey extract quests
mega_quests.update(generated_honey_extract_quests)

# Merge the generated honey comb extract quests
mega_quests.update(generated_honey_comb_extract_quests)

# Merge the generated regenerate quests
mega_quests.update(generated_regenerate_quests)

# Merge the generated playtime quests
mega_quests.update(generated_playtime_quests)

# Merge the generated move quests
mega_quests.update(generated_move_quests)

# Merge the generated swim quests
mega_quests.update(generated_swim_quests)

# Merge the generated sprint quests
mega_quests.update(generated_sprint_quests)

# Merge the generated sneak quests
mega_quests.update(generated_sneak_quests)

# Merge the generated glide quests
mega_quests.update(generated_glide_quests)

# Merge the generated fly quests
mega_quests.update(generated_fly_quests)

# Merge the generated item break quests
mega_quests.update(generated_item_break_quests)

# Merge the generated gain experience quests
mega_quests.update(generated_gain_experience_quests)

# Save all quests in 'mega.yml'
with open('Quests/mega.yml', 'w') as file:
    yaml.dump(mega_quests, file, default_flow_style=False)



print("Generated quests have been saved in their respective files.")