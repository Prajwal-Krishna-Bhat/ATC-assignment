def simulate_DFSM(input_string):
    state = 'q00'
    for symbol in input_string:
        if state == 'q00':
            if symbol== 'a':
                state='q10'
            else:
                state='q01'
        elif state == 'q01':
            if symbol== 'a':
                state='q11'
            else:
                state='q02'
        elif state == 'q02':
            if symbol== 'a':
                state='q12'
            else:
                state='q00'
        elif state == 'q10':
            if symbol== 'a':
                state='q20'
            else:
                state='q11'
        elif state == 'q11':
            if symbol== 'a':
                state='q21'
            else:
                state='q12'
        elif state == 'q12':
            if symbol== 'a':
                state='q22'
            else:
                state='q10'
        elif state == 'q20':
            if symbol== 'a':
                state='q00'
            else:
                state='q21'
        elif state == 'q21':
            if symbol== 'a':
                state='q01'
            else:
                state='q22'
        elif state == 'q22':
            if symbol== 'a':
                state='q02'
            else:
                state='q20'
    if state=='q00' or state=='q11' or state=='q22':
        decision="Accepted"
    else:
        decision="Not accepted"
    return decision
s="yes"
while s=="yes":
    input_string=input("Enter the input string:")
    output=simulate_DFSM(input_string)
    print(output)
    s=input("Do you want to try again (yes/no):")
    
            