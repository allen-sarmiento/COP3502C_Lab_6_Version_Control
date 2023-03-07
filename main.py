# TODO: Write main script
def main():
    # Showing how encode works
    raw_test_password = "00009962"
    encoded_test_password = encode(raw_test_password)
    print(f"Raw Test Password: {raw_test_password}")
    print(f"Encoded Test Password: {encoded_test_password}")


def encode(password):
    '''
    :param password: Expecting an 8-digit password as a string
    :return: New encoded 8-digit string with each digit shifted up by 3
    '''
    encoded_password = ""
    for digit in password:
        # Cast digit to an int and add 3. % 10 to get the first digit after adding.
        digit = (int(digit)+3) % 10
        # Add each digit to a new string
        encoded_password += str(digit)
    return encoded_password


# TODO: Write decode function
def decode():



if __name__ == '__main__':
    main()