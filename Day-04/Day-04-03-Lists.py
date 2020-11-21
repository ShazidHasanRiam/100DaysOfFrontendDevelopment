#Day-04 of 100 Days of Coding
#November 21, 2020
#Shazid Hasan Riam

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana",
                     "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
                     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
                     "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
                     "Arizona", "Alaska", "Hawaii"]
print(states_of_america[45])
print(states_of_america[-1])

#changing element
states_of_america[1] = "Pencilvania"
print(states_of_america)

#add to list
states_of_america.append("Riamland")
print(states_of_america)

states_of_america.extend(["Angelaland", "Hasanland"])
print(states_of_america)

# list.append()
# list.extend()
# list.insert()
# list.remove()
# list.pop()
# list.clear()

