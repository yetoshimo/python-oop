class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # {author: book_name}
        self.rented_books = {}  # {username: {book_name: days_to_return}}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return f"We could not find such user to remove!"
        self.user_records.remove(user)
        if user.username in self.rented_books:
            del self.rented_books[user.username]

    def change_username(self, user_id: int, new_username: str):
        _filter_users = [u for u in self.user_records if user_id == u.user_id]

        if _filter_users:
            user = _filter_users[0]

            if user.username != new_username:
                _get_username = user.username
                user.username = new_username
                if _get_username in self.rented_books:
                    _get_books = self.rented_books[_get_username]
                    del self.rented_books[_get_username]
                    self.rented_books[user.username] = _get_books
                return f"Username successfully changed to: {user.username} for userid: {user.user_id}"

            return f"Please check again the provided username - it should be different than the username used so far!"

        return f"There is no user with id = {user_id}!"
