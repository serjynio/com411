def list_entities():
  entities =['Mercury','Venus', 'Earth','Mars','Jupiter','Saturn','Uranus','Neptune', 'Pluto']
  cols = [4,5]
  for list11 in entities:
    if len(cols) == 0:
      for j in list11:
        print(j, end=", ")
      print("\n")
    else:
      for i in cols:
        print(entities[i], end=", ")
      return
list_entities()




'''def save():
  print("How do you want to save the data?")
  options = ['Export as CSV','Export as TXT','Export as JSON']
  for index, options in enumerate(options, start =1):
    print(index, options)
  u_input = int(input())

  if u_input == range(1, len(options)+1):
      print(u_input)
      return u_input
  else:
      print('bad command')
      return None

save()'''
