import random
import argparse
import os
import csv
import faker


def calculate_matches(dicts):
    d_keys = {}  # key:[value, count]
    for d in dicts:
        for key in d:
            if d[key] in d_keys and key == d_keys[d[key]][0]:
                d_keys[d[key]] = [key, d_keys[d[key]][1] + 1]
            else:
                d_keys[d[key]] = [key, 1]
    return [{'key': d_keys[x][0],
             'value': x,
             'count': d_keys[x][1]}
            for x in d_keys]


def create_data():
    template = ['id', 'success', 'name', ]
    data_list = []
    factory = faker.Faker()
    for x in range(100):
        data_list.append({template[0]: x,
                          template[1]: random.randint(0, 1) == 1,
                          template[2]: factory.name().split(' ')[0]})
    return data_list


def get_file_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        help='specifying path to file that will be translated')
    args = parser.parse_args()
    return args


def check_path_validation(path):
    if not path:
        raise OSError("File name wasn't specified")
    if not os.path.exists(path) or not os.path.isfile(path):
        raise OSError("File {} doesn't exist".format(path))
    if not path.endswith('.csv'):
        raise OSError("File {} is supposed to be in csv extension"
                      .format(path))


def extract_data(path):
    data = []
    with open(path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for index, row in enumerate(reader):
            data.append({})
            for x in row:
                print(index, x, row[x])
                data[index][x] = row[x]
    return data


def write_data(path, data):
    keys = data[0].keys()
    with open(path, 'w') as csv_file:
        reader = csv.DictWriter(csv_file, keys)
        reader.writeheader()
        reader.writerows(data)


def main():
    args = get_file_args()
    path = args.file
    # path = 'users_data.csv'
    check_path_validation(path)

    data = extract_data(path)
    # data = create_data()
    # write_data(path, data)
    print(calculate_matches(data))


if __name__ == '__main__':
    main()
