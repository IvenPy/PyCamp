import random
def calculate_matches(dicts):
    s = set()
    d_keys = {}   #key:[value, count]
    for d in dicts:
        for key in d:
            if d[key] in d_keys and key == d_keys[d[key]][0]:
                d_keys[d[key]] = [key, d_keys[d[key]][1] + 1]
            else:
                d_keys[d[key]] = [key, 1]
    return [{'key':x,'value':d_keys[x][0],'count':d_keys[x][1]} for x in d_keys]

def create_data():
    tamplate = ['id','success','name', ]
    names = ['Naruto', 'Sakura', 'Saske', 'Kakashi', 'Kiba', 'Hinata','Giraya']
    data_list = []
    for x in range(100):
        data_list.append({tamplate[0]:random.randint(0,20),
                        tamplate[1]:random.randint(0,1)==1,
                        tamplate[2]:names[random.randint(0,len(names) - 1)]})
    return data_list


def main():
    data = create_data()
    print(calculate_matches(data))


if __name__ == '__main__':
    main()
