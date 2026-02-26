from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
def anyRelationship(state: CollectionState, world: World, player: int):
    """Has the player all the required relationship levels?"""
    count = 0
    
    required_count = world.options.number_max_relationships.value
    required_level = world.options.max_lvl_relationship.value

    for item in ["Progressive Grand Marshal Akiko 14 Relationship", "Progressive Carmelina Silence Relationship", "Progressive Crimson Acid Relationship", "Progressive Henry Division Relationship", "Progressive Lydia Day Break Relationship", "Progressive Doctor Doom Jazz Relationship", "Progressive Sam Day Break Relationship", "Progressive The Witness To The End Relationship", "Progressive Yuri Night Relationship", "Progressive One Last Kiss Relationship"]:
        if state.count(item, player) >= required_level:
            count+=1
    if count >= required_count:
        return True
    else:
        return False