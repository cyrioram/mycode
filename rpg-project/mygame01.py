#!/usr/bin/python3

"""
Author: David

These edits where made to change the players startingarea and vastly increase the layout of the play
area beginning on or about line 38.
"""

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {
            'Frontyard Garden' : {
                'north' : 'Front Gate',
                'south' : 'Front Porch',
                'item' : 'water hose'
                },

            'Front Porch' : {
                'north' : 'Frontyard Garden',
                'south' : 'Front Door'
                },
            
            'Front Door' : {
                'north' : 'Front Porch',
                'south' : 'Grand Main Hall'
                },

            'Grand Main Hall' : { 
                  'north' : 'Front Door',
                  'northeast' : 'Living Room',
                  'southeast' : 'Guest Powder Room',
                  'up' : '2nd Floor Landing',
                  'south' : 'Dining Room'
                },

            'Dining Room' : {
                  'north' : 'Grand Main Hall'
                  'southwest' : 'Guest Bedroom',
                  'southeast' : 'Kitchen'
                },

            'Kitchen' : {
                'north' : 'Dining Room',
                'east' : 'Back Door'
                },

            'Back Door' : {
                'west' : 'Kitchen',
                'east' : 'Back Porch'
                },

            'Back Porch' : {
                'west' 'Back Door',
                'south' 'Backyard Garden'
                 },

            'Backyard Garden' : {
                'northwest' : 'Backyard Basement Garden Door', 
                'northeast' : 'Back Porch'

            'Guest Bedroom' : {
                'north' : 'Dining Room',
                'down' : 'Basement'
                },

            'Basement' : {
                'up' : 'Guest Bedroom',
                'southwest' : 'Backyard Garden Door'
                },

            'Backyard Basement Garden Door' {
                    'south' : 'Backyard Garden'
                    },

            '2nd Floor Landing' : {
                    'north' : 'Master bedroom',
                    'south' : 'Bedroom',
                    'west' : '2nd Floor Hall',
                    'up' : 'Attic Landing',
                    'down' : 'Grand Main Hall'
                },

            'Master Bedroom' : {
                    'south' : '2nd Floor Landing',
                    'item' : 'matches'
                    },

            'Bedroom' : {
                    'north' : '2nd Floor Landing'
                    },

            '2nd Floor Hall' : {
                    'west' : 'Closet' #Can open and view but too small to enter"
                    'southeast' : 'Main Bathroom',
                    'south' : 'Spare Bedroom'
                 },

            'Main Bathroom' : {
                    'west' : '2nd Floor Hall'
                    },

            'Spare Bedroom': {
                    'north' : '2nd Floor Hall',
                    'item' : 'revolver'
                    },

            'Attic Landing' : {
                    'north' : 'North Attic Room',
                    'south' : 'South Attic Room',
                    'down' : '2nd Floor Landing'
                 },

            'North Attic Room' {
                    'south' : 'Attic Landing',
                    },

            'South Attic Room' {
                'north' : 'Attic Landing',
                'item' : 'revolver ammunition'
                }

         }

#start the player in the Front Garden
currentRoom = 'Frontyard Garden''

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
  
  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

