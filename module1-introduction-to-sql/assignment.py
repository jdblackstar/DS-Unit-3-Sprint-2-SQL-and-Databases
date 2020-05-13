import os
import sqlite3
import pandas as pd 


DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

connection - sqlite3.connect(DB_FILEPATH)

cursor = connection.cursor()

# total characters
total_characters = '''
SELECT
    count(distinct charactercreator_character.character_id)
FROM
    charactercreator_character
    '''

# QUESTION 1
q1 = cursor.execute(total_characters).fetchall()
print("Total Characters: ", q1[0][0])

# sub-class totals
subclass_totals = '''
SELECT
    count(rage) AS fighter_count,
    count(charactercreator_cleric.using_shield) as cleric_count,
    count(charactercreator_mage.has_pet) as mage_count,
    count(charactercreator_thief.is_sneaking) as thief_count
FROM
    charactercreator_character
    LEFT JOIN charactercreator_cleric ON charactercreator_character.character_id = charactercreator_cleric.character_ptr_id
    LEFT JOIN charactercreator_fighter ON charactercreator_character.character_id = charactercreator_fighter.character_ptr_id
    LEFT JOIN charactercreator_mage ON charactercreator_character.character_id = charactercreator_mage.character_ptr_id
    LEFT JOIN charactercreator_thief ON charactercreator_character.character_id = charactercreator_thief.character_ptr_id
WHERE
    rage IS NOT NULL
    or charactercreator_cleric.using_shield IS NOT NULL
    or charactercreator_mage.has_pet IS NOT NULL
    or charactercreator_thief.is_sneaking IS NOT NULL
'''

# QUESTION 2
q2 = cursor.execute(subclass_totals).fetchall()
print("Total Characters per Subclass: ", q2[0][0])

# total items
total_items = '''
select
	count(distinct armory_item.name)
from
	armory_item
'''

# QUESTION 3
q3 = cursor.execute(total_items).fetchall()
print("Total Items: ", q3[0][0])

# total weapons
total_weapons = '''
select
    count(distinct armory_weapon.item_ptr_id)
from
    armory_weapon
'''

# QUESTION 4
q4 = cursor.execute(total_weapons).fetchall()
print("Total Weapons: ", q4[0][0])

# items that aren't weapons
items_no_weapons = q3[0][0] - q4[0][0]
print("Total Items (no weapons): ", items_no_weapons)

# character items
character_items = '''
select
    character_id,
    count(distinct item_id) as number_of_items
from charactercreator_character_inventory
group by character_id
limit 20
'''

# QUESTION 5
q5 = cursor.execute(character_items).fetchall()
print("Character's Items: ", q5)

# character weapons
character_weapons = '''
select
    character_id,
    count(distinct item_id) as number_of_items
from charactercreator_character_inventory
join armory_weapon on armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
group by character_id
limit 20
'''

# QUESTION 6
q6 = cursor.execute(character_weapons).fetchall()
print("Character's Weapons: ", q6)

# items per character
items_per_character = '''
select 
	avg(number_of_items) as avg_items
FROM(
	select
	    character_id,
	    count(distinct item_id) as number_of_items
	from charactercreator_character_inventory
	group by character_id
)
'''

# QUESTION 7
q7 = cursor.execute(items_per_character).fetchall()
print("Average Items per Character: ", q7[0][0])

weapons_per_character = '''
select 
	avg(number_of_items) as avg_items
FROM(
    select
        character_id,
        count(distinct item_id) as number_of_items
    from charactercreator_character_inventory
    join armory_weapon on armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
    group by character_id
)
'''

# QUESTION 8
q8 = cursor.execute(weapons_per_character).fetchall()
print("Average weapons per Character: ", q8[0][0])

df = pd.read_csv('buddymove_holidayiq.csv')

print(df.shape)

print(df.head())


# Assignment part 2:
path = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")

db = sqlite3.connect(path)
#print("CONNECTION:", connection)

cursor = db.cursor()

df.to_sql("review", con=db, if_exists="replace", index=False,
          dtype={"user_id": "TEXT",
                 "sports": "INTEGER",
                 "religious": "INTEGER",
                 "nature": "INTEGER",
                 "theatre": "INTEGER",
                 "shopping": "INTEGER",
                 "picnic": "INTEGER"})