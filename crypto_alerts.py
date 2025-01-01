import requests
url = "http://api.coinlayer.com/live?access_key=77b98b1e1175f96413e3cf91492e40ee"
params = {
    "symbols" : "XRP",
    "target" : "USD"
}

threshold = {
    "low" : 2.00,
    "exceeded": 3.00,
    "target": 5.00
}

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
    return "Error fetching XRP rate."

send_xrp_alert()