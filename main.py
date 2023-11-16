import src

def main():
    choice = ''
    while choice != '0':
        print('\nPress 0 to Quit')
        print('Press 1 to Generate a Target')
        print('Press 2 to Generate a Solution')
        print('Press 3 to Verify\n')
        choice = input('Enter your choice: ')
        if choice == '0':
            print('Goodbye!')
        elif choice == '1':
            d = input("Enter POW difficulty d: ")
            src.targetGen(d)
        elif choice == '2':
            src.solutionGen()
        elif choice == '3':
            src.verify()
        else:
            print('Error: Please provide valid number option')
            

if __name__ == '__main__':
    main()