characters = [
  "Ryu", "Ken", "Chun-Li", "Cammy", "Juri", "Luke", "Manon", "Deejay",
  "Marisa", "Jamie", "Kimberley", "Rashid"
]

print("Select a Character! (Choose their number)")
print("--------------------")
for id, name in enumerate(characters):
  print(f"{name} = {id}")

print("---------------------")
p1 = int(input("Player 1 ---> "))
p2 = int(input("Player 2 ---> "))

print("----------------------")
print(characters[p1], "VS", characters[p2] + "!", "Let's Rock!")
