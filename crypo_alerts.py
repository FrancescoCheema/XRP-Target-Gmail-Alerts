import requests
url = "http://api.coinlayer.com/live?access_key=77b98b1e1175f96413e3cf91492e40ee"
params = {
    "symbols" : "XRP",
    "target" : "USD"
}

threshold = {
    "XRP" : 2.00
}

def send_xrp_alert():
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        rates = data.get("rates", {})
        xrp_rate = rates.get("XRP")

        if xrp_rate is not None:
            if xrp_rate < threshold["XRP"]:
                print(f"XRP rate is currently at {xrp_rate} it is now below the threshold")
            elif xrp_rate > 3.00 :
                print(f"XRP has exceeded the threshold. Currently at {xrp_rate}")
            elif xrp_rate > 5.00 :
                print(f"XRP has reached the target. Currently at {xrp_rate}")
            else:
                print("XRP is stable")
                exit()

send_xrp_alert()