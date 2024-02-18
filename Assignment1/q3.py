def simulate_DFSM(input_string):
    state = 'q0'
    for symbol in input_string:
        if state=='q0':
            if symbol=='a':
                state='q1'
            else:
                state='q3'
        elif state=='q1':
            if symbol=='a':
                state='q2'
            else:
                state='q1'
        elif state=='q2':
            if symbol=='a':
                state='q2'
            else:
                state='q1'
        elif state=='q3':
            if symbol=='a':
                state='q3'
            else:
                state='q4'
        elif state=='q4':
            if symbol=='a':
                state='q3'
            else:
                state='q4'
    if state=='q2' or state=='q4':
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