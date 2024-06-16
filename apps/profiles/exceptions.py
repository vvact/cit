from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = 403
    default_detail = "You can't edit a profile that doesn't belong to you"


class NotYourProfile(APIException):
    status_code = 403
    default_detail = "You can't edit a profile that doesn't belong to you"
