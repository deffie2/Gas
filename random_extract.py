import csv

def extract_moves_from_csv(output_file):
    with open('board_4_cut_ off_r.csv', 'r') as csvfile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(outfile)
        for row in reader:
            print(row)
            row[0] = row[0][1:]
            parts= row[0].split()
            moves = int(parts[-2])
            print(moves)
            writer.writerow([moves])  

def read_source_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

# Function to append data to target.csv
def append_to_target_csv(file_path, data):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    output_file = 'data/Random/board_4_r_9x9.csv'
    file_path = 'data/Random/Freq_moves_WOH/board_4_410_freq_move_WOH_9x9.csv'
    data = read_source_csv(file_path)
    target_path= 'data/Random/board_4_r_9x9.csv'
    append_to_target_csv(target_path, data)