import os
import csv

def extract_info_and_save_csv(directory_path, output_csv_path):
    data = []
    
    for filename in os.listdir(directory_path):
        if filename.endswith(".mp4"):
            parts = filename.split('_')
            last_number = parts[-1].split('.')[0]  # Split on dot and take the first part
            filename = "/home/mahtab/jepa/data/Phase_1/" + filename + ' ' + str(last_number)
            data.append([filename])
    
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['File Name'])  # Write header
        writer.writerows(data)


directory_path = '/Users/mahtab/Documents/my_files/Courses/UIC/Cs518/Project/V_jepa_code/jepa/data/processed_videos/Phase_1'
output_csv_path = '/Users/mahtab/Documents/my_files/Courses/UIC/Cs518/Project/V_jepa_code/jepa/data/processed_videos/Phase_1/train.csv'
extract_info_and_save_csv(directory_path, output_csv_path)
