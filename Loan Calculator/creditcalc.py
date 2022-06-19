from math import ceil, floor, log
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument('--type'  )
parser.add_argument('--payment' )
parser.add_argument('--principal')
parser.add_argument('--periods' )
parser.add_argument('--interest' )
args = parser.parse_args()


def aperiods(principal,payment,interest):
    i = float((interest)) / (12 * 100)
    principal = float(principal)
    payment = float(payment)
    x = (payment) / (payment - i * principal)
    n = ceil(log(x, 1 + i))
    if (n % 12 == 0):
        print(f"It will take you {n // 12} years to repay this loan!")
    else:
        print(f"It will take you {n // 12} years and {n % 12} months to repay this loan!")
    print(f"Overpayment = {int(payment* n- principal)}")

def aprincipal(payment,periods,interest):
    i = float((interest)) / (12 * 100)
    periods = float(periods)
    payment = float(payment)
    x = floor(payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))
    print(f"Your loan principal = {x}")
    print(f"Overpayment = {int(payment * periods - x)}")


def apayment(principal,periods,interest):
    i = float((interest)) / (12 * 100)
    periods = float(periods)
    principal = float(principal)
    x = ceil(principal * ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))
    print(f"Your annuity payment = {x}")
    print(f"Overpayment = {int(x * periods - principal)}")
    return x

if args.payment != None:
    if float(args.payment) < 0:
        print("Incorrect parameters.")
        quit()
if args.principal != None:
    if float(args.principal) < 0:
        print("Incorrect parameters.")
        quit()
if args.periods!= None:
    if float(args.periods) < 0:
        print("Incorrect parameters.")
        quit()
if args.interest != None:
    if float(args.interest) < 0:
        print("Incorrect parameters.")
        quit()

if(args.type == "diff"):
    if args.payment != None:
        print("Incorrect parameters.")
        quit()
if args.interest == None:
    print("Incorrect parameters.")
    quit()


if(len(sys.argv) < 5):
    print("Incorrect parameters.")
    quit()

if(args.principal != None):
    p = int(args.principal)
    p2 = p
if(args.periods != None):
    n = int(args.periods)
i = float(args.interest)/(12*100)



if(args.type == "diff"):
    for k in range(1, n+1):
        d = ceil(p/n + i * (p - (p*(k-1))/n))
        print(f"Month {k}: payment is {d}")
        p2 = p2 - d
    print(f"Overpayment = {abs(p2)}")
elif(args.type == "annuity"):
    if(args.payment == None):
        apayment(args.principal,args.periods,args.interest)
    elif(args.principal == None):
        aprincipal(args.payment, args.periods, args.interest)
    elif(args.periods == None):
        aperiods(args.principal, args.payment, args.interest)

else:
    print("Incorrect parameters")


