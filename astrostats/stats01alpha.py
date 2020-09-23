#!/usr/bin/env python3

import requests


def main():
    # create r, which is our request object
    r = requests.get("http://api.open-notify.org/astros.json").json()  ## r = r.json
    
    for astrostat in r.json()["people"]:
       (astrostat.get("name", "craft"))
       

        print(f"")
main()
