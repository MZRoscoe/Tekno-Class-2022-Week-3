from dataset import data

folder_id = int(input())


def find_folder(data, folder_id):
    id_child = []
    for i in data:
        if i['id'] == folder_id:
            for j in i['children']:
                id_child.append(j['id'])
        else:
            if i['is_file'] == False:
                id_child += find_folder(i['children'], folder_id)
    return id_child

print(find_folder(data, folder_id))

