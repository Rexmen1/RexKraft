import yaml

def convert_to_mediawiki(input_file, output_file):
    with open(input_file, 'r') as f:
        ranks_data = yaml.safe_load(f)

    mediawiki_data = []
    for level, data in ranks_data.items():
        rewards = data.get('Rewards', [])
        rewards_text = '\n* '.join(rewards)
        row = f"| {level} || {data.get('name', '')} || {data.get('money', '')} || {data.get('xp', '')} || \n* {rewards_text}"
        mediawiki_data.append(row)

    with open(output_file, 'w') as f:
        f.write("{| class=\"wikitable\"\n! Level !! Name !! Money !! XP !! Rewards\n|-")
        f.write("\n|-\n".join(mediawiki_data))
        f.write("\n|}")

convert_to_mediawiki("ranks.yml", "ranksoutput.yml")
