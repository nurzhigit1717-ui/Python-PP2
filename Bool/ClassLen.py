class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#

def myFunction() :
  return True

print(myFunction())


#


def myFunction222() :
  return True

if myFunction222():
  print("YES!")
else:
  print("NO!")


#

x = 200
print(isinstance(x, int))