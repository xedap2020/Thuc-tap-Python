class SecondarySchoolException(Exception):
    message = 'Exception'

    def __init__(self, message=None):
        if message:
            self.message = message

    def get_message(self):
        return self.message


class CreateFail(SecondarySchoolException):
    message = 'Create failed.'


class UpdateFail(SecondarySchoolException):
    message = 'Update failed.'


class DeleteFail(SecondarySchoolException):
    message = 'Delete failed.'


class NotFound(SecondarySchoolException):
    message = 'Not found.'

class BadRequest(SecondarySchoolException):
    message = 'Invalid parameters.'