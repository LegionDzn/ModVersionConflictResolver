import os

def get_file_name(file_path):
    return os.path.splitext(file_path)[0]

def compare_files(file1, file2):
    score = 0
    name1 = get_file_name(file1)
    name2 = get_file_name(file2)
    for char1, char2 in zip(name1, name2):
        if char1 == char2:
            score += 1
    return (score / len(name1)) >= 0.5

def find_similar_files(file_list):
    similar_files = []
    for i, file1 in enumerate(file_list):
        for file2 in file_list[i + 1:]:
            if compare_files(file1, file2):
                similar_files.append((file1, file2))
    similar_file_groups = []
    for file1, file2 in similar_files:
        added = False
        for group in similar_file_groups:
            if file1 in group or file2 in group:
                group.update([file1, file2])
                added = True
                break
        if not added:
            similar_file_groups.append({file1, file2})
    return similar_file_groups

def delete_files(file_group):
    file_group = sorted(file_group)
    keep_file = file_group[-1]
    delete_files = file_group[:-1]
    confirmation = input(f"Do you want to delete {delete_files} and keep {keep_file}? [y/n] ")
    if confirmation == 'y':
        for file in delete_files:
            os.remove(file)
        print(f"Deleted files: {delete_files}")
        print(f"Kept file: {keep_file}")

file_list = [file for file in os.listdir() if os.path.isfile(file)]
similar_file_groups = find_similar_files(file_list)
for file_group in similar_file_groups:
    delete_files(file_group)
