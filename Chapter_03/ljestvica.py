comp = input().split('|')

# Handle duplication of '|' character
measures = []
joined = ''

if len(comp) >= 2:
    measures = [measure for measure in comp if measure != '']
    joined = ''.join(measures)

    # print('debug: measures ', measures)
#    print('debug: joined', joined)
    
    c_count = 0
    a_count = 0
    
    for tone in measures:
        # print('debug: tone ', tone[0])
        if tone[0] in ['C', 'F', 'G']:
            c_count += 1
        if tone[0] in ['A', 'D', 'E']:
            a_count += 1
    
    # print('debug: counts ', c_count, a_count)
    
    if c_count > a_count:
        print('C-dur')
    elif a_count > c_count:
        print('A-mol')
    elif len(joined) >= 2:
        # print('debug: last ', measures[-1])
        if joined[-1] == 'A':
            print('A-mol')
        else:
            print('C-dur')
