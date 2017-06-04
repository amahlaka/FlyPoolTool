import json
import requests
import time

wallet = input("Please input your wallet address: ")

def getStats(user):
    """Return the list of all currencies sorted by profitability."""
    url = "http://zcash.flypool.org/api/miner_new/"+user
    response = requests.get(url)
    output = response.json()
    return(output)

while(True):
    stats = getStats(wallet)
    hashrate = stats["hashRate"]
    payout = stats["payouts"]
    unpaid = str(stats["unpaid"]).rjust(9, '0')
    print(payout[1]["paidOn"])
    print(hashrate)
    print(str(stats["avgHashrate"])+'H/s')
    fxd = unpaid[:-8]+'.'+unpaid[-8:]

    print(fxd)
    time.sleep(10)
