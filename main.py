# Author: Haorong Xu hxx5086@psu.edu 
# Collaborator: Joshua Chang jvc6690@psu.edu
# Collaborator: Christian Dell'Edera cmd6705@psu.edu
# Section: 12
# Breakout: 16

def getLetterGrade(gd):
  if gd>=93.0:
    lt="A"
  elif gd>=90:
    lt="A-"
  elif gd>=87:
    lt="B+"
  elif gd>=83:
    lt="B"
  elif gd>=80:
    lt="B-"
  elif gd>=77:
    lt="C+"
  elif gd>=70:
    lt="C"
  elif gd>=60:
    lt="D"
  else:
    lt="F"
  return lt

def run():
  finalgrade=float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(finalgrade)}.")

if __name__ == "__main__":
  run()
  