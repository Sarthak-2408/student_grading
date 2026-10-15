def calculate_grade(marks):
  if not isinstance(marks,(int,float)) or isinstance(marks,bool):
     raise ValueError("Marks must be numeric")
  if not 0<=marks<=100:
     raise ValueError("Marks must be between 0 and 100")
  if marks>=90:
     return "A"
  elif marks>=70:
     return "B"
  elif marks>=50:
     return "C"
  elif marks>=30:
     return "D"
  else :
     return "F"

def process_student(name,marks):
   grade=calculate_grade(fl0at(marks))
   return f"{name}:{grade}"