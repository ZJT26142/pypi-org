import data.db_session as db_session
from data.users import User


def get_user_count() -> int:
    return 200
    session = db_session.create_session()
    return session.query(User).count()