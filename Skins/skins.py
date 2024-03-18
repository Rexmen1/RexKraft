def generate_item(item_name, model_data, slot, display_name, lore, left_click_commands, left_click_requirement):
    item_template = f'''
  {item_name}:
    material: FISHING_ROD
    model_data: {model_data}
    slot: {slot}
    display_name: '{display_name}'
    lore:
    {"".join([f"    - '{line}'\n" for line in lore])}
    left_click_commands:
    {"".join([f"      - '{command}'\n" for command in left_click_commands])}
    left_click_requirement:
      requirements:
    {"".join([f"        {key}:\n          {sub_key}: {value}\n" for key, sub_dict in left_click_requirement.items() for sub_key, value in sub_dict.items()])}
    '''
    return item_template

# Example usage
for i in range(1, 6):  # Generate 5 items
    item_name = f"fishing_rod_{i}"
    model_data = 100 + i
    slot = 8 + i
    display_name = f"&dFishing Rod {i}"
    lore = ["", "&7To equip the skin, wield the tool", "&7in your hand and left click.", "", "&aUnlocked: &f%luckperms_has_permission_skin.fishing_rod_1%"]
    left_click_commands = ["[console] cmi itemcmdata set %player_name% 101", "[console] lp user %player_name% permission settemp skin.fishing_rod_1.claimed true 30d"]
    left_click_requirement = {
        "item1": {"type": "string contains", "input": "%checkitem_getinfo:mainhand_mat:%", "output": "FISHING_ROD",
                  "deny_commands": ["[message] &cYou need to hold Fishing Rod in hand.", "[sound] ENTITY_VILLAGER_NO"]},
        "perms1": {"type": "has permission", "permission": f"skin.{item_name}",
                   "deny_commands": ["[message] &cYou don't have this skin unlocked.", "[sound] ENTITY_VILLAGER_NO"]},
        "perms2": {"type": "!has permission", "permission": f"skin.{item_name}.claimed",
                   "deny_commands": ["[message] &cYou have this skin already applied please wait %luckperms_inherited_expiry_time_skin.{item_name}.claimed%.",
                                     "[sound] ENTITY_VILLAGER_NO"]}
    }
    
    item_data = generate_item(item_name, model_data, slot, display_name, lore, left_click_commands, left_click_requirement)
    print(item_data)
