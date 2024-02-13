import numpy as np

def read_cli():
    #Get Unique Tokens
    num_unique_tokens = int(input("Masukkan jumlah token unik: "))
    print("Token haruslah dua karakter alfanumerik.")

    tokens=[]
    for i in range(num_unique_tokens):
        token = input(f"Masukkan token {i+1}: ")
        tokens.append(token)

    #Get Buffer Size
    buffer_size = int(input("Masukkan ukuran buffer: "))

    #Generate Matrix
    matrix_height = int(input("Masukkan tinggi matriks: "))
    matrix_width = int(input("Masukkan lebar matriks: "))
    matrix = np.random.choice(tokens, size=(matrix_height, matrix_width))

    #Read Sequence Req
    number_of_sequences = int(input("Masukkan jumlah sequences: "))
    seq_max_length = int(input("Berapa panjang maksimal sequences-nya?: ")) + 1

    #Generate Sequences
    sequences = []
    rewards = []
    for i in range(number_of_sequences):
        sequence = [np.random.choice(tokens) for j in range(np.random.randint(2, seq_max_length))]
        sequences.append(sequence)
        rewards.append(np.random.randint(5,30))

    #Information
    print("\nMatriks yang digunakan adalah:")
    for i in range (matrix_height):
        for j in range(matrix_width):
            print(matrix[i][j], end=' ')
        print()

    print("\nSequences yang akan dicocokkan adalah:")
    for seq in range (len(sequences)):
        print(f"{seq+1}.", end=' ')
        for tok in range(len(sequences[seq])):
           print(sequences[seq][tok], end=' ')
        print(f"(Reward = {rewards[seq]})")

    return buffer_size, matrix_width, matrix_height, matrix , number_of_sequences, sequences, rewards