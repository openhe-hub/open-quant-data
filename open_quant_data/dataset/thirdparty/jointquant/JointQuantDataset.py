from datetime import datetime
from typing import List, Dict

from loguru import logger
import pandas as pd
import numpy as np
import jqdatasdk as jq


class JointQuantDataset:
    def __init__(self, config: dict):
        self.username = config['thirdparty']['joint_quant']['username']
        self.password = config['thirdparty']['joint_quant']['password']
        jq.auth(self.username, self.password)

    def query_account_info(self):
        return jq.get_account_info()

    def get_price(self, stock_id: str, begin: datetime, end: datetime, frequency: str,
                  fields: List[str] = None, fq: str = 'pre') -> pd.DataFrame:
        return jq.get_price(security=stock_id, start_date=begin.strftime('%Y-%m-%d'),
                            end_date=end.strftime('%Y-%m-%d'), frequency=frequency,
                            fields=fields, fq=fq)

    def get_prices(self, stock_id: List[str], begin: datetime, end: datetime, frequency: str,
                   fields: List[str], fq: str) -> pd.DataFrame:
        return jq.get_price(stock_id=stock_id, begin=begin, end=end, frequency=frequency,
                            fields=fields, fq=fq)
