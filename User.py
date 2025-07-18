from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str

def get_user_info(user: User) -> str:
        return f'Возраст пользователя {user.name} - {user.age}, ' \
            f'а email - {user.email}'


user_1 = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
print(get_user_info(user_1))