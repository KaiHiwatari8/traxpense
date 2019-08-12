import datetime

desc = {}
amt = {}

def new_expense():
    choice = input('Start entering expenses?(Y/N): ')
    while(True):
        if choice.lower() == 'y':
            description = input('Enter description of expenses: ')
            amount = float(input('Enter amount: '))
            desc[int(len(desc)+1)] = description
            amt[int(len(amt)+1)] = amount
            
        else:
            break
        choice = input('Enter more expenses?(Y/N): ')

def total_amt():
    total = 0
    for y in amt:
        total += amt[y]
    return "Your today's total is $ " +str(total)



def driver():
    answer = datetime.datetime.now().strftime('%c') + "\n"

    new_expense()

    for x in range(1,len(desc)+1):
        answer += str(x) + ':' + str(desc[x]) + '= $'+ str(amt[x]) + '\n'

    answer += total_amt() + '\n'
    return answer