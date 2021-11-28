# Creating Dictonary
silicon = {'CPU':['Core','Cache'],'GPU':['Pipeline'],'IO':['USB','SATA'],'Year':1997}
# Printing Dictonary  & its key and values
print(silicon)
Dict_keys = list(silicon.keys())
Dict_values = list(silicon.values())
print(Dict_keys)
print(Dict_values)
# Adding NEw Entry & Update existing entry in Dictonary
silicon['CPU']=['NEWUPDATES']   #Updaing existing
silicon['Price']=900
print(silicon)

# Deletes Entry from dict
del silicon['IO']
print(silicon)

# Find Key Value
print(silicon.get(Dict_keys[1]))



# Find key values
# Sort dictionary
