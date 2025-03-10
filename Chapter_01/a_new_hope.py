count = int(input())

if count <= 1:
    print('A long time ago in a galaxy' + ' far ' * count + ' away...')
else:
    print('A long time ago in a galaxy' + ' far, ' * (count - 1) + ' far ' + ' away...')
