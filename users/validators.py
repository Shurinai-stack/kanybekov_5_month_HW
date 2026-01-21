from datetime import date, datetime
from rest_framework.exceptions import ValidationError


def validate_user_age(request):
    token = request.auth

    if not token or not token.get("birthdate"):
        raise ValidationError(
            "Укажите дату рождения, чтобы создать продукт."
        )

    birthdate = datetime.strptime(
        token["birthdate"], "%Y-%m-%d"
    ).date()

    age = date.today().year - birthdate.year

    if age < 18:
        raise ValidationError(
            "Вам должно быть 18 лет, чтобы создать продукт."
        )
