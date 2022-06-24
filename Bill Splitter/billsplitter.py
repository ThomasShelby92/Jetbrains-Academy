# write your code here
import random
def friends_input(n):
    d = {}
    for i in range (0,n):
        x = input()
        d.update({x:0.0})
    return d

print("Enter the number of friends joining (including you):")

try:
    n = int(input())
    if n <= 0:
        print("No one is joining for the party")
        quit()
except ValueError:
    print("No one is joining for the party")
    quit()

print("Enter the name of every friend (including you), each on a new line:")
d = friends_input(n)
print("Enter the total bill value:")
bill = int(input())
for i in d:
    d[i] = round(bill/len(d),2)
# print(d)

print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
s = input()
if s == 'Yes':
    persons = list(d.keys())
    lucky_person = random.choice(persons)
    print(f"{lucky_person} is the lucky one!")
    for i in d:
        if i == lucky_person:
            d[i] = 0
        else:
            d[i] = round(bill / (len(d) - 1), 2)
    print(d)
else:
    print("No one is going to be lucky")
    print(d)





