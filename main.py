from sys import exit


def main() -> None:
    exit_message: str = 'Exiting program...'
    while True:
        try:
            user_input: str = input('Enter a string: ')

            if user_input == 'exit':
                print(exit_message)
                exit()

            reversed: str = user_input[::-1]

            print(f'The reverse of {user_input} is {reversed}')
        except KeyboardInterrupt:
            print(exit_message)
            exit()


if __name__ == '__main__':
    main()
