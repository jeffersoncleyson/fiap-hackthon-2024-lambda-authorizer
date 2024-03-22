import json

class ResponseLambdaFormatterUtils:

  def __init__(self) -> None:
     pass

  @staticmethod
  def get_response_message(effect: str, resource: str, sid: str):
        return {
            "principalId": "user",
            "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": "execute-api:Invoke",
                        "Effect": effect,
                        "Resource": resource,
                    },
                ],
            },
            "context": {
                "xsid": sid,
            },
        }