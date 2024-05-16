from typing import Tuple, Union

class Reimbursement:
    def __init__(self):
        self.ads = {
            '0011': {'cost_share_rate': 0.50, 'allowed_spend': 200, 'count': 0},
            '1011': {'cost_share_rate': 1.00, 'allowed_spend': (1000, 2000), 'count': 0},
            '1111': {'cost_share_rate': 0.75, 'allowed_spend': 500, 'count': 0},
            '1010': {'cost_share_rate': 0.90, 'allowed_spend': 750, 'count': 0},
        }
        self.ad_details = []

    def add_ad(self, ad_type: str, count: int, spend: float) -> None:
        if ad_type in self.ads:
            self.ads[ad_type]['count'] += count
            self.ad_details.append({'ad_type': ad_type, 'count': count, 'spend': spend})
        else:
            raise ValueError("Invalid Ad Type")

    def print_ads(self) -> None:
        for ad_type, info in self.ads.items():
            print(f"Ad Type: {ad_type}, Count: {info['count']}")

    def total_reimbursement(self) -> float:
        total = 0.0
        for ad in self.ad_details:
            ad_type = ad['ad_type']
            count = ad['count']
            spend = ad['spend']
            if ad_type == '1011':
                spend = min(count * spend, self.ads[ad_type]['allowed_spend'][1])
            else:
                spend = min(count * spend, self.ads[ad_type]['allowed_spend'])
            total += spend * self.ads[ad_type]['cost_share_rate']
        return total

    def get_ads(self):
        return self.ad_details
