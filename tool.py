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


def clearScreen():
    """Check os and clear the screen."""
    import platform
    import os
    osystem = platform.system()

    if(osystem == "Windows"):
        os.system('cls')
    if(osystem == "Linux" or osystem == "Darwin" ):
        os.system('clear')
    return
def updateDelay():
    times = 10
    while (times > 0):
        print('.', sep=' ', end='', flush=True)
        time.sleep(1)
        times = times - 1
    print(" Updating")
    return


while(True):
    stats = getStats(wallet)
    hashrate = stats["hashRate"]
    payout = stats["payouts"]

    unpaid = str(stats["unpaid"]).rjust(9, '0')
    paid = str(payout[1]["amount"]).rjust(9, '0')
    paidf = paid[:-8]+'.'+paid[-8:]
    clearScreen()
    print('------------------------------------------------------------')
    print("Latest Payout: "+payout[1]["paidOn"]+" Amount: "+paidf)
    print("Reported Hashrate: "+hashrate)
    print("Effective Hashrate: "+str(stats["avgHashrate"])+'H/s')
    fxd = unpaid[:-8]+'.'+unpaid[-8:]

    print("Unpaid: "+fxd)
    print('------------------------------------------------------------')
    updateDelay()
