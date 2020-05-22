def multiplica(multiplicador, multiplicando):

  list_multiplicando = []

  multiplicador = str(multiplicador)
  multiplicando = str(multiplicando)
   
  for i in multiplicando:
    list_multiplicando.append(i)

  results = []
  list_multiplicando.reverse()
  casas_decimais = 0
  result = 0

  for m in list_multiplicando:
    calc = str(int(m) * int(multiplicador))
    results.append(calc + casas_decimais*' ')
    result += int(calc + casas_decimais*'0')
    casas_decimais += 1

  
  len_result = len(str(result))
  print(' {}\nx{}\n {}'.format(
  multiplicador.rjust(len_result),
  multiplicando.rjust(len_result),
  len_result*'-'))
    
  for x in results:
    print(' ' + x.rjust(len_result))
  print(' {}\n {}'.format(len_result*'-', result))
    
  return result

# multiplica(99999999, 88888888)
