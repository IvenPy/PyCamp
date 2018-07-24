def calculate_matches(dicts):
    s = set()
    d_keys = {}   #key:[value, count]
    for d in dicts:
        for key in d:
            if key in d_keys and d[key] == d_keys[key][0]:
                d_keys[key][1] += 1
            else:
                d_keys[key] = [d[key], 1]
    return [{'key':x,'value':d_keys[x][0],'count':d_keys[x][1]} for x in d_keys]

def main():
    dicts = [{1:2,3:4}, {1:2}, {4:5}, {4:5, 'smth':'trratata'}]
    print(calculate_matches(dicts))


if __name__ == '__main__':
    main()
