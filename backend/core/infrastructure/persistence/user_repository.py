from .django_models import UserModel
from ...domain.entities.user import User
from ...domain.ports.user_repository import UserRepository


class DjangoUserRepository(UserRepository):

    def get_all(self):
        return [
            User(
                id=u.id,
                username=u.username,
                email=u.email,
                role=u.role,
                employee_id=u.employee.id if u.employee else None
            )
            for u in UserModel.objects.all()
        ]

    def get_by_id(self, user_id: int):
        u = UserModel.objects.get(id=user_id)
        return User(
            id=u.id,
            username=u.username,
            email=u.email,
            role=u.role,
            employee_id=u.employee.id if u.employee else None
        )

    def get_by_username(self, username: str):
        u = UserModel.objects.get(username=username)
        return User(
            id=u.id,
            username=u.username,
            email=u.email,
            role=u.role,
            employee_id=u.employee.id if u.employee else None
        )

    def save(self, user: User):
        if user.id:
            u = UserModel.objects.get(id=user.id)
            u.username = user.username
            u.email = user.email
            u.role = user.role
        else:
            u = UserModel.objects.create(
                username=user.username,
                email=user.email,
                role=user.role
            )

        u.save()
        user.id = u.id
        return user

    def delete(self, user_id: int):
        UserModel.objects.filter(id=user_id).delete()