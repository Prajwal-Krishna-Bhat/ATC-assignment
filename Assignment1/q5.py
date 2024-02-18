def simulate_DFSM(input_string):
    state = 'q0'
    decision="Accepted"
    for symbol in input_string:
        if state=='q0':
            if symbol=='a':
                state='q1'
            else:
                state='q2'
        elif state=='q1':
            if symbol=='a':
                state='q1'
            else:
                state='q2'
        elif state=='q2':
            if symbol=='b':
                state='q2'
            else:
                decision="Not Accepted"
                return decision
    return decision
s="yes"
while s=="yes":
    input_string=input("Enter the input string:")
    output=simulate_DFSM(input_string)
    print(output)
    s=input("Do you want to try again (yes/no):")