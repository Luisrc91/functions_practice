def hello():
    print('hello, Luis')


def pack(Bus, Car, Truck):
    return [Bus, Car, Truck]

def eat_lunch(list):
  if len(list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(list)):
      if i == 0:
        print(f"First I eat {list[0]}")
      else:
        print(f"Next I eat {list[i]}")


hello()
print(pack("Bus","Car","Truck"))
eat_lunch([])
eat_lunch(["Spaghetti"])
eat_lunch(["Hamburger","Spaghetti","Pizza","Salad"])