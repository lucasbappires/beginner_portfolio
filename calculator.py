while True:
    num_1 = input('Type a number: ')
    num_2 = input('Type another number: ')
    operator = input('Type an operator: (+-*/) ')

    valid_num = None
    float_num_1 = 0
    float_num_2 = 0

    try:
        float_num_1 = float(num_1)
        float_num_2 = float(num_2)
        valid_num = True

    except:
        if valid_num is None:
            print('One or both numbers aren\'t valid.')
            continue
    
    valid_operators = ('+-*/')

    if operator not in valid_operators:
        print('The operator you typed isn\'t valid.')
        continue

    if len(operator) > 1:
        print('Please type only one operator.')
    
    print('Calculating...')
    if operator == '+':
        print(f'{num_1} + {num_2} = {float_num_1 + float_num_2}')
    if operator == '-':
        print(f'{num_1} - {num_2} = {float_num_1 - float_num_2}')
    if operator == '*':
        print(f'{num_1} * {num_2} = {float_num_1 * float_num_2}')
    if operator == '/':
        print(f'{num_1} / {num_2} = {float_num_1 / float_num_2}')
        
    quit = input('Want to [q]uit? ').lower().startswith('q')
    if quit:
        break