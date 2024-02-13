import os

def read_txt(filename):

    #Opening .txt file
    filepath = os.path.join(os.path.dirname(__file__), '..','test','input',filename)
    if not (os.path.exists(filepath)):
        print("The file does not exist.")
        return
    else:
        requirements = open(filepath, "r")
        lines = [line.strip() for line in requirements]

        #Get Buffer Size
        buffer_size = int(lines[0])

        #Get Matrix Size
        line1 = lines[1].split()
        matrix_width = int(line1[0])
        matrix_height = int(line1[1])

        #Read Matrix
        matrix = []
        for i in range(2, 2+matrix_height):
            line = lines[i].split()
            matrix_row=[]
            for j in range(matrix_width):
                matrix_row.append(line[j])
            matrix.append(matrix_row)

        #Read Sequences
        seq_numline = 2+matrix_height
        number_of_sequences = int(lines[seq_numline])

        sequences = []
        rewards = []

        for i in range(number_of_sequences):
            sequence = []
            sequence_tokens = lines[seq_numline+1+2*i].split()
            sequences.append(sequence_tokens)

            reward = int(lines[seq_numline+2*(1+i)])
            rewards.append(reward)
            
        return buffer_size, matrix_width, matrix_height, matrix , number_of_sequences, sequences, rewards


