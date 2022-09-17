def arithmetic_arranger(problems, solve = False):
  first_row = ""
  second_row = ""
  third_row = ""
  sumx = ''
  for i in problems:
    line = ''
    first = i.split(' ')[0]
    second = i.split(' ')[1]
    third = i.split(' ')[2]
    length = max(len(str(first)),len(str(third)))+2
    top = str(first).rjust(length)
    bottom = second + str(third).rjust(length-1)
    if first.isnumeric() != True or third.isnumeric()!= True:
      return "Error: Numbers must only contain digits."
    if len(str(first)) >= 5 or len(str(third))>= 5:
      return "Error: Numbers cannot be more than four digits."
    if len(problems) > 5:
      return "Error: Too many problems."
    if second ==  "+":
      sum = int(first) + int(third)
    elif second == "-":
      sum = int(first) - int(third)
    else:
      return "Error: Operator must be '+' or '-'."
    
    answer = str(sum).rjust(length)
    
    for d in range(length):
      line += '-'
    if i != problems[-1]:
      first_row += top + '    '
      second_row += bottom + '    '
      third_row += line + '    '
      sumx += answer + '    '
    else:
      first_row += top 
      second_row += bottom 
      third_row += line 
      sumx += answer 
  if solve:
    string = first_row + '\n' + second_row + '\n' + third_row + '\n' + sumx
  else:
    string = first_row + '\n' + second_row + '\n' + third_row
  return string
