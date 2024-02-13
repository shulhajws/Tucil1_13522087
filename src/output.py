#File ini berisi fungsi untuk melakukan output

import os

def print_to_console(max_reward, sequence, final_coordinates, time):
    print()
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("Solusi paling optimal adalah:")
    print()
    print(max_reward)
    # Most optimal Sequence
    for i in range(len(sequence)):
        print(sequence[i], end=' ')
    print()
    # Most Optimal Coordinates
    for i in range(len(final_coordinates)):
        print(f"{final_coordinates[i][0]},{final_coordinates[i][1]}")
    print()
    print(time, " ms")

    print("Anda dapat menyimpan solusi ini dalam file.txt")

def save_txt(filename, max_reward, sequence, final_coordinates, time):
    filepath = os.path.join(os.path.dirname(__file__), '..', 'test', 'output', filename)
    f = open(filepath, "w")

    f.write(str(max_reward) + '\n')
    for i in range(len(sequence)):
        f.write(sequence[i])
        f.write(' ')
    f.write('\n')
    for i in range(len(final_coordinates)):
        f.write(f"{final_coordinates[i][0]},{final_coordinates[i][1]}\n")
    f.write('\n')
    f.write(str(time))
    f.write(" ms")

    f.close()

    print(f"\nSolusi Anda telah disimpan pada file {filename}")

# print_output()
# save_output("tes.txt")