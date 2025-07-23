def check_palindrome(word:str):
    if type(word)==str:
     word=word.upper()#if we use upper with number it will give an error
     if word==word[::-1]:
       return 'palindrome'
     else:
        return 'not a palindrome'
    else:
        return 'invalid data type'#this will work if the above if fails


def give_fibo(n):
 fibo=[0,1]
 for i in range(n-2):
  last_num=fibo[-1]
  second_last_num=fibo[-2]
  next_num=last_num+second_last_num
  fibo.append(next_num)
      
 return fibo 


def check_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return 'Not a Prime Number'
            break
            print('Happy Holi')
    else:
        return 'Prime Number'


def print_star(n = 5, typ = 'left',shape = '*'):
  if typ  == 'left':
    space  = ''

  elif typ == 'right':
    space = '  '

  elif typ == 'mid':
    space = ' '

  for i in range(1,n+1):
    print(space*(n-i) + i*f'{shape} ')



def sum_of_n_natural_numbers(n):
  result =0 
  for i in range(1,n+1):
    result +=i

  return result


def factorial(n):
  result =1
  for i in range(1,n+1):
    result *=i

  return result



