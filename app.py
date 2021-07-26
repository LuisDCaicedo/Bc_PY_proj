blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction == None: 
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transcation_value():
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print("Outputting Block")
        print(block)



while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Ouput the blockchain blocks')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        txt_amount = get_transcation_value()
        add_transaction(txt_amount, get_last_blockchain_value())    
    elif user_choice == '2':
       print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please choose a valid option')
    print('Choice registered!')

print("Done!")
