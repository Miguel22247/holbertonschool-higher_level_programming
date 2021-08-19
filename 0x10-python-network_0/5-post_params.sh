#!/bin/bash
# Script that takes a URL
curl -s -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" $1
