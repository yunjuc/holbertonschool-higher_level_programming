#!/bin/bash
# Send a post request with data 
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
