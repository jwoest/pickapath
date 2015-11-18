#!/usr/bin/env python3

# A simple pick-your-own-path game engine.

import os
import sys
import yaml


# Function defs

# Load in the "pages" of the adventure.  Each "page" is a section of a YAML
# file kept in the "adventures" subdirectory.  The first page of any
# adventure is always page 1.
def load_adventure(adv):
    filename = "adventures//" + adv + ".yaml"
    # Make sure that the requested adventure exists
    if not os.path.isfile(filename):
        print("Can't find adventure '%s'." % adv)
        sys.exit()

    # Read in the adventure file
    with open(filename, 'r') as fh:
        contents = fh.read()
        data = yaml.load(contents)
        
    return data


# Run a page - print its text and choices, get player input and
# validate it, and return the next page number.
def run_page(adv_pages, page):
    os.system('clear')
    print(adv_pages[page]['text'])
    print("--------------------------------------------\n")

    # If the page has no choices, then this is the end of the game
    if 'choices' not in adv_pages[page]:
        return -1

    # Assign each "next choice" an index number, so that the player
    # can choose what to do next.
    index = 0
    choices = {}
    for c in adv_pages[page]['choices']:
        choices[index] = {}
        choices[index]['next'] = c
        choices[index]['text'] = adv_pages[page]['choices'][c]
        index += 1

    print("Choose what to do next:\n")
    for i in range(len(choices)):
        print("%d - %s" % (i + 1, choices[i]['text']))

    # Get and validate input from the player
    while True:
        player_input = input("\nYour choice?  ")

        try:
            player_input = int(player_input)
        except:
            print("That's not a valid choice.\n")
            continue

        if player_input < 1 or player_input > len(choices):
            print("That's not a valid choice.")
            continue

        return choices[player_input - 1]['next']



### MAIN

# Check the command-line args - the first should be the name of
# the adventure to play.
if len(sys.argv) != 2:
    print("USAGE:  %s <adventure_to_play>" % sys.argv[0])
    sys.exit()
else:
    adventure = sys.argv[1]

# Load the adventure files
adv_pages = load_adventure(adventure)

# run the game
page = 1
while page != -1:
    page = run_page(adv_pages, page)

print("\n")
print("GAME OVER")
print("\n")

