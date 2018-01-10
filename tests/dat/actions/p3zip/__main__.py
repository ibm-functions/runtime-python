#!/usr/bin/env python

import netifaces

def main(args):
    networkif = netifaces.interfaces()
    print ("Networkinterfaces: \n %s" %networkif )
    networkinfo = netifaces.ifaddresses('eth0')[netifaces.AF_INET]
    print ("Networkinfo eth0: \n %s" %networkinfo )
    return {"Networkinfo: ": networkinfo}

def naim(args):
    return main(args)

if __name__ == "__main__":
    # execute only if run as a script
    print(main({}))

