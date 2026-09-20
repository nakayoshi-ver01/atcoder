once_try=[['.' for j in range(1000)] for i in range(1000)]
 
once_try[499][499]='#'
 
for i in range(1000):
  print(''.join(once_try[i]))