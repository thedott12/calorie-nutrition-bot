
user_history = {}

def save_to_history(user_id, text):
    user_history.setdefault(user_id, []).append(text)

def get_history(user_id):
    return user_history.get(user_id, [])
