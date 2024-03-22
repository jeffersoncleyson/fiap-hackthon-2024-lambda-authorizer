import logging
from src.application.utils.environment import EnvironmentUtils
from src.application.utils.environment_constants import EnvironmentConstants
from src.framework.adapters.input.rest.response_lambda_formatter_utils import (
    ResponseLambdaFormatterUtils,
)
from src.application.usecases.authorizer_use_case import AuthorizerUseCase

logger = logging.getLogger()
logger.setLevel(logging.INFO)

secret = EnvironmentUtils.get_env(EnvironmentConstants.SECRET.name)
signin_use_case = AuthorizerUseCase(secret)


def lambda_handler(event, context):

    identity_source = event["identitySource"][0]

    token_header = str(identity_source).split("Bearer ")

    if len(token_header) != 2:
        return ResponseLambdaFormatterUtils.get_response_message("Deny", event["routeArn"], "")

    return signin_use_case.process(event)
