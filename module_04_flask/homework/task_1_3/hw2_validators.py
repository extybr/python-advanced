"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
from typing import Optional
from flask_wtf import FlaskForm
from wtforms import Field
from wtforms.validators import ValidationError


class NumberLength:
    def __init__(self, minimum: int, maximum: int, message: Optional[str] = None):
        self.minimum = minimum
        self.maximum = maximum
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        data = field.data
        if len(str(data)) > 0 and data is not None and self.minimum <= data <= self.maximum:
            return
        if self.message is not None:
            message = self.message
        else:
            message = field.gettext("Число должно быть между %(minimum)s and %(maximum)s.")
        raise ValidationError(message % dict(minimum=self.minimum, maximum=self.maximum))
