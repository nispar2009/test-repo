from user import User

users = [
    User(1, 'Carefree Guy', '1234')
]

username_mapping = {
    u.username: u for u in users
}

userid_mapping = {
    u.id: u for u in users
}

def authenticate(username, password):
    user = username_mapping[username]
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping[user_id]