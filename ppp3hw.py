#flatten and shorten an array of integers in ascending order
# FUNCTIONAL PROMPT
def sortnums(numbers):
  arr = []
  for nums in numbers:
    for i in nums:
      arr.append(i)
  print (sorted(arr))
sortnums(["4","5","6","99","1","20"])

# OBJECT ORIENTED PROGRAMMING
# PODRACER CLASS
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed= max_speed
    self.condition= condition
    self.price= price
  def repair(self):
    self.condition = "Repaired"
    print("Pod's current condition:",self.condition)

# ANAKINS CLASS
class AnakinsPod(Podracer):
  def __init__(self,max_speed,condition,price):
    super().__init__(max_speed,condition,price)
  def boost(self):
    self.max_speed *= 2
    print("Anakin's Speed with boost:",self.max_speed)

# SEBULBAS CLASS
class SebulbasPod(Podracer):
  def __init__(self,max_speed,condition,price):
    super().__init__(max_speed, condition, price)
  def flame_jet(self, other):
    other.condition = "Trashed"
    print("Activated flame jet! condition of the other pod:",other.condition)

#PLAYER 0
c0 = Podracer(2,"Trashed",100)
c0.repair()

#PLAYER 1
c1 = AnakinsPod(2,"Perfect",200)
c1.boost()

#PLAYER 2
c2 = SebulbasPod(2,"Perfect",200)
c2.flame_jet(AnakinsPod)