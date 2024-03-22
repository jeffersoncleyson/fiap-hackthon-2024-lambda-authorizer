import jwt
from datetime import datetime, timezone
from src.framework.adapters.input.rest.response_lambda_formatter_utils import (
    ResponseLambdaFormatterUtils,
)


class AuthorizerUseCase:

    def __init__(self, secret: str):
        self.secret = secret

    def process(self, event: dict):
        identity_source = event["identitySource"][0]

        token_header = str(identity_source).split("Bearer ")

        if len(token_header) != 2:
            return ResponseLambdaFormatterUtils.get_response_message(
                "Deny", event["routeArn"], ""
            )

        try:
            decoded = jwt.decode(token_header[1], self.secret, algorithms="HS256")

            exp_tkn = int(decoded.get("exp"))
            iat = int(datetime.now(tz=timezone.utc).timestamp())

            if iat > exp_tkn:
                return ResponseLambdaFormatterUtils.get_response_message(
                    "Deny", event["routeArn"], ""
                )

            return ResponseLambdaFormatterUtils.get_response_message(
                "Allow", event["routeArn"], decoded.get("sid")
            )
        except:
            return ResponseLambdaFormatterUtils.get_response_message(
                "Deny", event["routeArn"], ""
            )
