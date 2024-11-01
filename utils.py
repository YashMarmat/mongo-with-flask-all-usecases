from flask import jsonify


def json_response_err(field_name, field_error, error_msg, status_code=404):
    return (
        jsonify(
            {
                "msg:": error_msg,
                "errors": [
                    {
                        field_name: [field_error],
                    }
                ],
            }
        ),
        status_code,
    )
