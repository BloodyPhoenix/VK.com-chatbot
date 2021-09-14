from pony.orm import Database, Required, Json
from settings import DB_CONFIG

db = Database()
db.bind(**DB_CONFIG)


class UserState(db.Entity):
    """Состояние пользователя внутри сценария"""
    user_id = Required(int, unique=True)
    scenario_name = Required(str)
    current_step = Required(str)
    context = Required(Json)


class Registration(db.Entity):
    """База зарегистрированных пользователей"""
    user_name = Required(str)
    user_email = Required(str)


db.generate_mapping(create_tables=True)
