import csv

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

def generate_report(students):
   """Generate a report listing student and their grades."""
   lines=["Student Report","-----------------"]
   for name,marks in students:
      grade = calculate_grade(marks)
      lines.append(f"{name}:{marks}-Grade{grade}")
   return "\n".join(lines)

def read_students(filename="students.csv"):
   students=[]
   with open(filename,newline="") as file:
      reader=csv.DictReader(file)
      if not reader.fieldnames or not {"name","marks"}.issubset(reader.fieldnames):
         raise ValueError("CSV must contain name and marks columns")
      for row in reader:
         try:
            name=row["name"].strip()
            marks=float(row["marks"])
            if not name:
               raise ValueError("Student name cannot be empty")
            grade=calculate_grade(marks)
            students.append((name,marks,grade))
         except (ValueError,TypeError,AttributeError) as error:
            raise ValueError(f"Invalid CSV record:{row}") from error 
   return students

if __name__ =="__main__":
   try:
      students=read_students()
      print(generate_report([(name,marks)for name,marks,_ in students]))
   except (ValueError,OSError,csv.Error) as error:
      print(f"Error:{error}")