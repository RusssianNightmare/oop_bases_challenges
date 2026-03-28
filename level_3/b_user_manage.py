"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def __init__(self):
        super().__init__()
    def get_users(self):
        return super().get_users()
    def ban_username(self, username):
        if username in self.usernames:
            self.usernames.remove(username)
        else:
            print('Такого пользователя не существует')



class SuperAdminManager(AdminManager):
    def __init__(self):
        super().__init__()
    def ban_all_users(self):
        return self.usernames.clear()
    def get_users(self):
        return super().get_users()
if __name__ == '__main__':
    user = UserManager()
    user.add_user("anna")
    user.add_user("artem")
    user.add_user("ivan")
    print(user.get_users())

    admin = AdminManager()
    admin.add_user('anna')
    admin.add_user('gleb')
    admin.add_user('ivan')
    admin.ban_username('anna')
    print(admin.get_users())

    manager = SuperAdminManager()
    manager.add_user('anna')
    manager.add_user('ivan')
    manager.add_user('artem')
    manager.ban_all_users()
    print(manager.get_users())
