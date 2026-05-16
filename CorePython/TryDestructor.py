class Employee:
  def __init__(self):
    print("object created")
  def calctax(self,annualsalary):
    tax=annualsalary*5/100
    print(f"tax is {tax}")
  def __del__(self):
    print("object destroyed")

e=Employee()
e.calctax(400000)


