# App Name:            Diner Invite App: Python Crash Course - Exercise 3-9
# App Creation Date:   05/23/2019
# App Description:     This Python script is the independent exercise in 
#                      'Python Crash Course', from page 50, Exercise 3.9.
# 
#                      Code Well & For Good.

# Defines original guest list
original_guests = ['michael giesen ', ' emma giesen', "Walter 'tha cat' Giesen", "Little 'larry' giesen", "Fred"]
non_human_guests = ["Walter 'tha cat' Giesen", "Little 'larry' giesen"]
human_guests = ['michael giesen ', 'emma giesen', 'fred']

# prints initial guest number
print(" ************* Secret Diner Club ************** " + '\n') 
print('Number of Invited Guests Attending: ')
print(len(original_guests))
print('\n')

# defines an update events section
print(" ------------- EVENT UPDATES ------------- ")
print("It looks like the following non-humans can't attend the party: ")
print(non_human_guests)
print('\n')

# updates the new guest list and prints the output
print("The following guests can still make the party: ")
del original_guests[2]
print(original_guests)
print('\n')

print("That updates the list to ")
print(len(human_guests))
