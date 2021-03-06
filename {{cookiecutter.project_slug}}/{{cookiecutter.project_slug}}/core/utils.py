import logging
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        data = response.data
        response.data = {}
        errors = []
        for field, value in data.items():
            if isinstance(value, list):
                errors.append("{} : {}".format(field, " ".join(value)))
            else:
                errors.append("{} : {}".format(field, value))

        response.data['errors'] = errors
        response.data['status_code'] = response.status_code
        try:
            response.data['exception'] = exc.get_full_details()
        except Exception as e:
            # response.data['exception'] = exc
            logger.info("=======exc======== %s" % exc)
            pass

    return response
