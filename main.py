def get_the_context(x, y, my_array):
    # Set the value of the rows elements for the specific space column
    int_value = int(my_array[x][y], base=16)
    for j in range(8):
        val = int(my_array[j][y], base=16) ^ int_value
        my_array[j][y] = chr(val ^ 32)


def transform(my_array, index_row):
    # Take a row by row .
    # Check each row with others rows.
    # Each element xor with each element in same column and check if it produce letter or spaces .
    # if all elements in same column introduce this it proves that the char is space.
    for i, row in enumerate(my_array[index_row]):
        # Convert The value to it's decimal value
        if len(row) > 1:
            int_value = int(row, base=16)
        count = 0
        for j in range(0, len(my_array)):
            if len(my_array[j][i]) > 1:
                # Xor elements
                val = int(my_array[j][i], base=16) ^ int_value
                # Check if elements in the columns is a letter or space
                if val == 0 or 65 <= val <= 90 or 97 <= val <= 122:
                    count += 1
        # Check if all elements in this column is a letter or space, if true, it's a space.
        # Get the element corresponded to this space in other rows.
        if count == 8:
            get_the_context(index_row, i, my_array)


# Print the cipher text
def print_cipher(arr):
    plain_text = ""
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if len(arr[i][j]) > 1:
                plain_text += "X"
            else:
                plain_text += arr[i][j]
        if i != len(arr) - 1:
            plain_text += "\n"
    return plain_text


if __name__ == '__main__':
    text = [
        "70A20FBD7E209324A979BFE2997A46E61B22749692EB1655FA995D46A9FA654F43C93F2114A21E3E227714580A6790B88BD74F9E09107D8B0EAC",
        "6FA20DBA622CDD28EC68F0F0C16D41A7023778C29EB8455EFC894B46EDA96C46459E2D2A1CEF1239707F571604618CEB9DD85E955013628B0DAE",
        "6FA20DBA6220893AA970A4B5CD664CE609286D8799B80010F68A0F56FAE868405BD72A2A51E118386E7214520E6994AC9D964E824A16648B16B9",
        "71A80AAA6227DD20FB68A0E1D6695BA71C3864C285AE1445F09E4A50A9EA6B5B52D82B3F51E3192922645D5100769ABE8B965C89480F6F910BB3",
        "7DA30ABD753A8E63FB70BEF1D66340BC0D24748D99EB065FEC804B03F9FB6F5F52D02A731CE31B24617F5B431C2496AA94DA1D865D17778109B3",
        "75B34EA66369932CFD31A0E7D86D5DAF0F3171C283A44542FC805603FAE6664C5BC77E3C1FA204346F7B51421D6D96EB9DD85E955013628B0DAE",
        "75E71DA771259163E774A6F0CB2E5BA3192378C283A30010EA8D4246A9F96B5A44C9312115A21823227B415A1B6D85A79D965C844A0C638C16B3",
        "68AF0BEF7F39982DA975B5E6D06947E61C22748C94A2155CFCCC464DEAFB6F4844DB2D7312ED192B6B7251580C61D5A296964E824A16648B16B9"]
    # split the sentence into list of bytes.
    array = []
    for sentence in text:
        split_list = [sentence[i:i + 2] for i in range(0, len(sentence), 2)]
        array.append(split_list)
    # Find spaces and predict the letters
    for i in range(8):
        transform(array, i)
    #  Print the result.
    #  Each unspecified letter will be X
    print("Unknown Characters" + "\n" + print_cipher(array))
    print("\n \n")
    # Start Guessing, Guessing some characters from first sentence and from second to get all ciphertext
    # Get all unknown characters index in the first sentence because all sentence has the same unknown index
    places = []
    for i in range(len(array[0])):
        if len(array[0][i]) > 1:
            places.append(i)
    # My Guess.
    guessing = [['l', 'n', 'o', 'w', 'r', 'i', 'e', 'c', 'o', 'f', 't', 'i', 's', 'a', 'e', 's', 'y'],
                ['p', 't', 'i', 'o', 'n']]
    # Guess The remaining characters.
    size = len(guessing)
    t = 0
    for k in range(size):
        for i in range(len(guessing[k])):
            raw = array[k][places[i + t]]
            for j in range(len(array)):
                if len(array[j][places[i + t]]) > 1:
                    val = int(array[j][places[i + t]], base=16) ^ ord(guessing[k][i]) ^ int(raw, base=16)
                    array[j][places[i + t]] = (chr(val ^ 32 ^ 32))
        t += len(guessing[k])
    # Show results
    print("The True Cipher Text : " + "\n" + print_cipher(array))
