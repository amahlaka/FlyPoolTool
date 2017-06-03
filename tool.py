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
    print(payout[1]["paidOn"]+" amount: 0."+str(payout[1]["amount"]).rjust(8, '0'))
    print(hashrate)
    print('0.'+str(stats["unpaid"]).rjust(8, '0'))
    time.sleep(10)
