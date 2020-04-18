"""
Online Lookup exceptions

The base class is OnlineLookupError

LookupVerification:
    raised when there is an issue verifying login credentials
    param api: Which API are you using?
"""


# importorator
__all__ = ['OnlineLookupError', 'LookupVerificationError',
           'LookupResultError', 'LookupActiveError']


# base exception
class OnlineLookupError(LookupError):
    def __init__(self, api):
        self.api = api


# verification error
class LookupVerificationError(OnlineLookupError):
    def __init__(self, api):
        super().__init__(api)


# result error
class LookupResultError(OnlineLookupError):
    def __init__(self, api):
        super().__init__(api)


# inactive error
class LookupActiveError(OnlineLookupError):
    def __init__(self, api):
        super().__init__(api)
