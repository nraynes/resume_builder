from src.validation.ValidationStatus import ValidationStatus


class ValidationResult:
    def __init__(self, value, status, reason = ""):
        self._value = value
        self._status = ValidationStatus(status)
        if self._status == ValidationStatus.FAILED:
            self._reason = f"Value {value} failed validation for reason: {reason}"
        else:
            self._reason = f"Value {value} evaulated all conditions successfully."

    @property
    def value(self):
        return self._value

    @property
    def status(self):
        return self._status

    @property
    def reason(self):
        return self._reason

    @property
    def failed(self):
        if self.status is ValidationStatus.FAILED:
            return True
        return False

    @property
    def passed(self):
        if self.status is ValidationStatus.PASSED:
            return True
        return False
