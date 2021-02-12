"""In this example, when the function fun() is called, it creates
 an instance of class B which passes itself to class A, which
  then sets a reference to class B and resulting in a
  circular reference.

  Due to the use of custom destructor which marks this item
  as uncollectable, python garbage collector can't remove it..

  Simply it doesn't know the order in which to destroy the
  objects, so it leaves them. Therefore, if your instances
  are involved in circular references they will live in memory
  for as long as the application run....
  """
class A:
    def __init__(self, bb):
        self.b = bb
        print("A")

class B:
    def __init__(self):
        self.a = A(self)
        print("B before die")
    def __del__(self):
        print("die")

def fun():
    b = B()

fun()
