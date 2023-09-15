#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


players = ["Player 1", "Player 2"]
current_player = random.choice(players)


# In[3]:


board = [
    "Go", "Mediterranean Avenue", "Community Chest", "Baltic Avenue",
    "Income Tax", "Reading Railroad", "Oriental Avenue", "Chance",
    "Vermont Avenue", "Connecticut Avenue", "Jail", "St. Charles Place",
    "Electric Company", "States Avenue", "Virginia Avenue", "Pennsylvania Railroad",
    "St. James Place", "Community Chest", "Tennessee Avenue", "New York Avenue",
    "Free Parking", "Kentucky Avenue", "Chance", "Indiana Avenue",
    "Illinois Avenue", "B&O Railroad", "Atlantic Avenue", "Ventnor Avenue",
    "Water Works", "Marvin Gardens", "Go To Jail", "Pacific Avenue",
    "North Carolina Avenue", "Community Chest", "Pennsylvania Avenue", "Short Line",
    "Chance", "Park Place", "Luxury Tax", "Boardwalk"
]


# In[4]:


player_positions = {player: 0 for player in players}


# In[5]:


def roll_dice():
    return random.randint(1, 6)


# In[ ]:


while True:
    print(f"It's {current_player}'s turn.")
    input("Press Enter to roll the dice...")
    
    dice_roll = roll_dice()
    print(f"{current_player} rolled a {dice_roll}.")
    
    
    player_positions[current_player] += dice_roll
    
    if player_positions[current_player] >= len(board):
        player_positions[current_player] -= len(board)
        print(f"{current_player} passed Go and collected $200!")

        
    print(f"{current_player} landed on {board[player_positions[current_player]]}.")

