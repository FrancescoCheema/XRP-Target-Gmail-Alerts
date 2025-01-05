import requests
import os

"""Added API, exported key to venv environment"""
access_key = os.getenv("ACCESS_KEY")
url = f"http://api.coinlayer.com/live?access_key={access_key}"
params = {
    "symbols" : "XRP",
    "target" : "USD"
}

"""Added thresholds, for when XRP is low, Exceedex, or reaches target"""
threshold = {
    "low" : 2.00,
    "exceeded": 3.00,
    "target": 5.00
}

"""get API response in real-time, specifically for XRP and print alerts based off thresholds, XRP price"""
def send_xrp_alert():
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        rates = data.get("rates", {})
        xrp_rate = rates.get("XRP")

        if xrp_rate is not None:
            if xrp_rate < threshold["low"]:
                return f"XRP rate is currently at {xrp_rate}. It is now below the threshold."
            elif xrp_rate < threshold["exceeded"]:
                return f"XRP has exceeded the threshold. Currently at {xrp_rate}."
            elif xrp_rate < threshold["target"]:
                return f"XRP has reached the target. Currently at {xrp_rate}."
            else:
                return f"XRP is stable, current rate: {xrp_rate}."
        else:
            raise Exception(f"failed to fetch, status error: {response.status_code}")



try:
    print(send_xrp_alert())
except Exception as e:
    print(f"error {e}")