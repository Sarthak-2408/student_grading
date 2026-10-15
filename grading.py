def calculate_grade(marks):
  if not isinstance(marks,(int,float)) or isinstance(marks,bool):
     raise ValueError("Marks must be numeric")
  if not 0<=marks<=100:
     raise ValueError("Marks must be between 0 and 100")
  if marks>=80:
     return "A"
  elif marks>=60:
     return "B"
  elif marks>=40:
     return "C"
  else :
     return "F"

def generate_report(students):
   """Generate a report listing student and their grades."""
   lines=["Student Report","-----------------"]
   for name,marks in students:
      grade = calculate_grade(marks)
      lines.append(f"{name}:{marks}-Grade{grade}")
   return "\n".join(lines)