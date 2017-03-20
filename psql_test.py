import sys

for x in range(5):
    if x == 3:
        continue
    print(x)

place_id = sys.argv[1]
if place_id == 'None':
   sys.exit() 

print(place_id)

sql = """
  select * from context
  where context = hogehoge;
"""

print(sql)

