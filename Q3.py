class Car:
  def __init__(self,model_no):
    self.model_no = model_no

def swap_model_no(c1,c2):
  tem_var = c1.model_no
  c1.model_no = c2.model_no
  c2.model_no = tem_var

c1 = Car("A_SERIES")
c2 = Car("S_SERIES")
print("Object c1 model no:",c1.model_no)
print("Object c2 model no:",c2.model_no)

swap_model_no(c1,c2)
print("Object c1 model no:",c1.model_no)
print("Object c2 model no:",c2.model_no)




