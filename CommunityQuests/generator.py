import os
import yaml
import random

def generate_quest(mob):
    quest_name = f"{mob.capitalize()}Quest"
    display_name = f"&c&l{mob.capitalize()} Slayer"
    quest_type = "mobkill"
    entities = [mob]
    goal = random.randint(100, 256)
    description = f"&fKill {goal} {mob}s as fast as you can!"
    display_item = f"{mob.upper()}_SPAWN_EGG"
    world = "World"
    rewards = {
        "money": 2500,
        "commands": "voucher give randomepic 2 player",
    }

    quest_data = {
        quest_name: {
            "displayName": display_name,
            "type": quest_type,
            "entities": entities,
            "description": description,
            "displayItem": display_item,
            "worlds": [world],
            "goal": goal,
            "rewards": rewards
        }
    }

    return quest_data

def main():
    mobs_file_path = os.path.join("List", "mobs.yml")
    quests_folder = "Quests"
    community_file_path = os.path.join(quests_folder, "community.yml")

    with open(mobs_file_path, "r") as mobs_file:
        mobs_data = yaml.safe_load(mobs_file)

    quests_data = {}
    for mob in mobs_data:
        quests_data.update(generate_quest(mob))

    os.makedirs(quests_folder, exist_ok=True)
    with open(community_file_path, "w") as community_file:
        yaml.dump(quests_data, community_file, default_flow_style=False)

    print(f"Quests saved in {community_file_path}")

if __name__ == "__main__":
    main()
