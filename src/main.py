from read_txt import read_txt
from read_cli import read_cli
from util import intro
import math
import time
import combination
import output

#Pemilihan Masukan dan Load Variabel yang Dibutuhkan
intro()
choice = int(input("Masukan file dari (1) file .txt (2) otomatis / CLI : "))
if choice==1:
    filename = input("Masukkan nama file dalam <namafile>.txt: ")
    buffer_size, matrix_width, matrix_height, matrix , number_of_sequences, sequences, rewards = read_txt(filename)
elif choice==2:
    buffer_size, matrix_width, matrix_height, matrix , number_of_sequences, sequences, rewards = read_cli()

#Inisialisasi Nilai
start_time = time.time()
max_reward = 0
min_steps = 999999
current_steps = 0
current_coordinate = []
ongoing_coordinates = []
final_coordinates = []
current_reward = 0
state = "hor"
col_win = -1

#Definisi Fungsi-Fungsi
def get_token_combinations():
    all_perm = combination.generate_permutations(number_of_sequences)
    seqcomb = combination.tokens_of_permutations(all_perm, sequences)
    all_combinations = combination.generate_all_combinations(seqcomb, all_perm)
    return all_combinations

def move_vertical(next_token, row_coordinate=0):
    '''Mencari token selanjutnya yang sesuai dengan pergerakan vertikal'''
    global current_coordinate
    global current_steps
    global ongoing_coordinates

    current_coordinate=ongoing_coordinates[-1]
    curr_row = current_coordinate[0]-1
    curr_col = current_coordinate[1]-1
    i=row_coordinate
    found=False
    while (i<matrix_height) and (not found):
        if (i != curr_row):
            if (matrix[i][curr_col]==next_token):
                found=True
                current_steps+=1
                current_coordinate = [i+1, curr_col+1]
                ongoing_coordinates.append(current_coordinate)
        i+=1
    if (not found):
        # reset()
        return False
    else:
        return True

def move_horizontal(next_token, col_coordinate=0):
    '''Mencari token selanjutnya yang sesuai dengan pergerakan horizontal'''
    global current_coordinate
    global current_steps
    global ongoing_coordinates

    current_coordinate=ongoing_coordinates[-1]
    curr_row = current_coordinate[0]-1
    curr_col = current_coordinate[1]-1
    i=col_coordinate
    found=False
    while (i<matrix_width) and (not found):
        if (i != curr_col):
            if (matrix[curr_row][i]==next_token):
                found=True
                current_steps+=1
                current_coordinate = [curr_row+1, i+1]
                ongoing_coordinates.append(current_coordinate)
        i+=1
    if (not found):
        # reset()
        return False
    else:
        return True

def reset():
    '''Melakukan reset nilai variabel current dan ongoing'''
    global current_coordinate
    global current_steps
    global ongoing_coordinates

    current_steps = 0
    current_coordinate = []
    ongoing_coordinates = []

def matching_check(ongoing_coordinates):
    '''Mengecek apakah di urutan token saat ini memenuhi sequence token-token'''
    reward_points = 0
    ongoing_tokens = []
    for i in range(len(ongoing_coordinates)):
        ongoing_tokens.append(matrix[ongoing_coordinates[i][0]-1][ongoing_coordinates[i][1]-1])
    
    for j in range(number_of_sequences):
        found=False
        for k in range(len(ongoing_tokens) - len(sequences[j]) + 1):
            if ongoing_tokens[k:k+len(sequences[j])] == sequences[j]:
                found = True
                break
        if found:
            reward_points += rewards[j]

    return reward_points

def coord_to_token(coord):
    '''Menyimpan nilai titik-titik koordinat dalam bentuk urutan token'''
    tokens = []
    for i in range(len(coord)):
        tokens.append(matrix[coord[i][0]-1][coord[i][1]-1])
    return tokens

def adjust_final_coordinates(coord, steps, i):
    '''Melakukan penyesuaian susunan dan mencegah dari eror'''
    tokens = coord_to_token(coord)
    j=0
    if tokens[0] != allcomb[i]:
        j=1
    final_tokens = tokens[0:j+steps]
    final_coordinates = coord[0:j+steps]

    return final_tokens, final_coordinates

def adjust_allcomb(allcomb, buffer):
    '''Delete duplicated combinations'''
    #Adjust Array
    adjusted_array = [sub_array[:buffer] for sub_array in allcomb]
    #Delete All Duplicated Elements
    unique_array = []
    for sub_array in adjusted_array:
        if( sub_array not in unique_array):
            unique_array.append(sub_array)
    return unique_array

def teso(coord):
    for i in range(len(coord)):
        print(matrix[coord[i][0]-1][coord[i][1]-1], end=' ')

allcomb = get_token_combinations()
allcomb = adjust_allcomb(allcomb, buffer_size)

for cols in range(matrix_width): #Brute force dari setiap sel pada baris pertama
    starting_cell = matrix[0][cols]
    
    for i in range (len(allcomb)): #Brute force dari seluruh kombinasi sequence yang mungkin
        reset()
        state="hor"
        j = 0
        current_reward = 0
        starting_token = allcomb[i][j]
        current_coordinate = [1, cols+1]
        ongoing_coordinates.append(current_coordinate)
        
        #Initiation
        if (starting_cell == starting_token):
            j+=1

        #Looping
        fail = False
        prevfail = False
        while (len(ongoing_coordinates)>0) and (0<=current_steps<buffer_size-1) and (j<len(allcomb[i])):
            current_coordinate = ongoing_coordinates[-1] #memastikan current_coordinate adalah koordinat terakhir
            next_token = allcomb[i][j]

            if state=="hor":
                if not prevfail:
                    row_coordinate=0
                fail = not(move_vertical(next_token, row_coordinate))
                state="ver"
                if fail:
                    if (len(ongoing_coordinates)>1):
                        coord_token_deleted = ongoing_coordinates.pop()
                        col_coordinate = coord_token_deleted[1]
                        j-=1
                        current_steps-=1
                        prevfail = True
                    elif(len(ongoing_coordinates)==1):
                        break
                        
            elif state=="ver":
                if not prevfail:
                    col_coordinate=0
                fail = not(move_horizontal(next_token, col_coordinate))
                state="hor"
                if fail:
                    if (len(ongoing_coordinates)>1):
                        coord_token_deleted = ongoing_coordinates.pop()
                        row_coordinate = coord_token_deleted[0]
                        j-=1
                        current_steps-=1
                        prevfail = True
                    elif(len(ongoing_coordinates)==1):
                        break

            if not fail:
                prevfail=False
                j+=1 #continue to next token
                if matching_check(ongoing_coordinates)!=0: #if already met the end of the sequence
                    current_reward = matching_check(ongoing_coordinates) #save current rewards

                    #Updating if set a new record
                    if current_reward > max_reward:
                        col_win = cols
                        max_reward = current_reward
                        final_coordinates = ongoing_coordinates
                        min_steps = current_steps
                    elif current_reward == max_reward:
                        if len(ongoing_coordinates)-1 < min_steps:
                            col_win = cols
                            min_steps = len(ongoing_coordinates)-1
                            final_coordinates = ongoing_coordinates[:min_steps+1]

        if (current_steps<0) or (current_steps>=buffer_size-1):
            continue
        
if (len(final_coordinates)==0):
    print("Tidak ada solusi")
else:
    final_coordinates_in_tokens, final_coordinates = adjust_final_coordinates(final_coordinates, min_steps, col_win)
    end_time = time.time()
    execution_time = 1000*(end_time-start_time)
    output.print_to_console(max_reward, final_coordinates_in_tokens, final_coordinates, execution_time)

    save_answer = input("\nApakah Anda ingin menyimpannya dalam file .txt? Ketik 'y' jika ingin menyimpan.  ")
    if save_answer=="y":
        filename = input("Masukkan nama file Anda ingin menyimpan solusi di atas? (Masukkan dalam format <namafile>.txt): ")
        output.save_txt(filename, max_reward, final_coordinates_in_tokens, final_coordinates, execution_time)
    else:
        print("Program selesai. Silakan jalankan program ini kembali jika Anda ingin menggunakannya lagi.")
