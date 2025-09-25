def type_tell():
    name = 'Bridget'
    print(type(name))
    #type_tell() # this will cause an error. we shouldnot call a fuction  withi its body.

type_tell()

name = 'Nankunda'
print(name)

def my_printer():
    print('Ozzy')

def my_list():
    nums = [10,20,30] 
    nums.pop()
    print(nums)
my_list()
#static function- gives you the same answer whenever you call upon it 
#dynamic fuctions - A fuction that is capable of giving you different answers whenever you call upon it eg print(), type()

def sum():
    num1, num2=20,50
    ans = num1 + num2
    print(ans)

def sum2(num1, num2): #the values num1 and num2 are called parameters
    ans = num1+num2
    print(ans)

sum2(100, 200) # the values 100 and 200 are called arguments
sum2(10, 30)
sum2(90, 78)
    
def even_odd(num):
    if num%2 == 0:
        print('even')
    else:
        print('odd')
even_odd(103)