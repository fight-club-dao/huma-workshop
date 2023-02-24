from typing import Any, Dict, List
import requests
import config


def underwrite(huma_pool, **kwargs):
    """
    The interface function between an EA and Huma EA service
    :param huma_pool: the object that represents huma pool contract
    :param **kwargs
        poolAddress:        str: the address for the destiny huma pool
        borrowerWalletAddress:      str: the borrower's wallet address
    :return: returns corresponding fields to UI
    """

    borrower_wallet_address = kwargs["borrowerWalletAddress"]  # noqa
    result = {
            "declined": True
        }
    """
    your code here
    the function should return result in following format
        # approved case example
        # amount is the credit limit
        result = {
            "creditLimit": int(100*10**6),
            "intervalInDays": 30,
            "remainingPeriods": 12,
            "aprInBps": 0
        }
        # declined case example
        result = {
            "declined": True,
            "reason": "accountTooNew"
        }
    """
    return result  # noqa
