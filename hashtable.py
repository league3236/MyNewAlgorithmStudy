class Hashtable:
  
  def __init__(self):
    self.table = [None for _ in range(139)]
    
  def simple_hash(self,name):
    sum = 0
    for letter in name:
      sum += ord(letter)
    return sum % len(self.table)
    
  def put(self, name, num):
    self.table[self.simple_hash(name)] = num
    
  def show(self):
    for idx, value in enumerate(self.table):
      if value:
        print(idx, value)
    
  def find(self, name):
    return self.table[self.simple_hash(name)]
    
boo = Hashtable()
boo.put('Kim', 7458)
boo.put('John', 8569)
boo.put('Smith', 1452)

boo.show()

print(boo.find('Kim'))
