import re
import uuid, datetime

def validateInput(input):
    rgx='[A-Za-z0-9]+$'
    return bool(re.match(rgx,input))

def generateID(data):
    # make SHA-1 hash of a namespace UUID and a name
    str_id = str(uuid.uuid5(uuid.uuid4(), data)).split('-')
    result = ''.join(str_id)
    return result


def findUser(sid, users):
    print('find user:')
    for user in users:
        print(user['username'], user['session_id'])
        if user['session_id'] == sid:
            return user['username']
        else:
            return

