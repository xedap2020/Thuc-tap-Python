from rest_framework.response import Response
from rest_framework import status as rest_status


class SuccessResponse(Response):
    def __init__(self, status=rest_status.HTTP_200_OK, message='succeed', data=[]):
        results = {"results": {
            "code": status,
            "message": message,
            'data': data
        }}

        super(SuccessResponse, self).__init__(data=results, status=status)


class ErrorResponse(Response):
    def __init__(self, status=rest_status.HTTP_404_NOT_FOUND, message='error', data={}):
        results = {"error": {
            "code": status,
            "message": message
        }}
        if data:
            results['error']['data'] = data

        super(ErrorResponse, self).__init__(data=results, status=status)


class ValidationErrorResponse(ErrorResponse):
    def __init__(self, status=rest_status.HTTP_422_UNPROCESSABLE_ENTITY, message='validation error', data={}):
        super(ValidationErrorResponse, self).__init__(status=status, message=data.get(next(iter(data)))[0] if data else None, data=data)
