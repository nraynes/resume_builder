import re
from src.validation.ValidationResult import ValidationResult
from src.enums.Degree import Degree
from datetime import datetime


class Validate:
    isodateformat = "%Y-%m-%dT%H:%M:%S.%f"
    epoch = "1970-01-01T00:00:00.000000"

    @classmethod
    def string(cls, value):
        """Validates whether a supplied value is a string or not.

        Args:
            value: A value to be evaluated.

        Returns:
            ValidationResult: An object with the result of whether the value passed or failed validation by meeting all of the conditions.
        """
        if not isinstance(value, str):
            return ValidationResult(value, 0, "Value is not a string.")
        return ValidationResult(value, 1)

    @classmethod
    def bool(cls, value):
        """Validates whether a supplied value is a valid boolean or not.

        Args:
            value: A value to be evaluated.

        Returns:
            ValidationResult: An object with the result of whether the value passed or failed validation by meeting all of the conditions.
        """
        if not isinstance(value, bool):
            return ValidationResult(value, 0, "Value is not a valid bool.")
        return ValidationResult(value, 1)

    @classmethod
    def email(cls, value):
        """Validates whether a supplied value is a valid email or not.

        Args:
            value: A value to be evaluated.

        Returns:
            ValidationResult: An object with the result of whether the value passed or failed validation by meeting all of the conditions.
        """
        string_validation = cls.string(value)
        if string_validation.failed:
            return string_validation
        elif re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value) is None:
            return ValidationResult(value, 0, "Value is not a valid email address.")
        return ValidationResult(value, 1)

    @classmethod
    def phoneNumber(cls, value):
        """Validates whether a supplied value is a valid phone number or not.

        Args:
            value: A value to be evaluated.

        Returns:
            ValidationResult: An object with the result of whether the value passed or failed validation by meeting all of the conditions.
        """
        string_validation = cls.string(value)
        if string_validation.failed:
            return string_validation
        elif re.search(r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$", value) is None:
            return ValidationResult(value, 0, "Value is not a valid phone number.")
        return ValidationResult(value, 1)

    @classmethod
    def degree(cls, value):
        """Validates whether a supplied value is a valid degree type or not.

        Args:
            value: A value to be evaluated.

        Returns:
            ValidationResult: An object with the result of whether the value passed or failed validation by meeting all of the conditions.
        """
        string_validation = cls.string(value)
        if string_validation.failed:
            return string_validation
        try:
            e = Degree[value]
        except KeyError:
            return ValidationResult(value, 0, "Value is not a valid degree type.")
        return ValidationResult(value, 1)

    @classmethod
    def date(cls, value):
        """Validates whether a supplied value is a valid date or not.

        Args:
            value: A value to be evaluated.

        Returns:
            ValidationResult: An object with the result of whether the value passed or failed validation by meeting all of the conditions.
        """
        string_validation = cls.string(value)
        if string_validation.failed:
            return string_validation
        try:
            datetime.strptime(value, cls.isodateformat)
        except ValueError:
            return ValidationResult(value, 0, "Value is not a valid date.")
        return ValidationResult(value, 1)
