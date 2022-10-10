class BaseException(Exception):
            pass


class AppException(BaseException):
    """Custom Exception for the Service."""

    def __init__(self, msg=None, status_code=500):
        if msg is None:
            msg = {
                "body": {"message": "Internal Service error"},
            }

        self.message = msg
        self.status_code = status_code
        super(AppException, self).__init__(msg)


class ControllerException(BaseException):
    """Custom Exception for the Controller."""

    def __init__(self, msg=None, status_code=500):
        if msg is None:
            msg = {
                "body": {"message": "Controller error"},
            }

        self.message = msg
        self.status_code = status_code
        super(ControllerException, self).__init__(msg)
