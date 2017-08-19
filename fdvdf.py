import vk
import time
login = raw_input("Enter login: ")
passw = raw_input("Enter pass: ")
inter = input("Enter pause(second): ")
session = vk.Session()
session = vk.AuthSession('5001234', login, passw, scope='groups')
vk_api = vk.API(session)
api = vk.API(session)
a = vk_api.groups.get(filter = "groups, publics, events", fields = "name", extended = "1")
i =1
while i != len(a):
    vk_api.groups.leave(group_id = str(a[i]["gid"]))
    print a[i]["name"]
    i += 1
    time.sleep(inter)
