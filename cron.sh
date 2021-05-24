#!/usr/bin/env bash

bash ./getResults.sh

python3 ./parseResults.py > current_results.json

diff=$(diff current_results.json previous_results.json)
if [ "$diff" != "" ]; then
    osascript -e 'display notification "New Car results!" with title "New Car Results"'
    osascript -e 'tell application "Messages" to send "New Car Results!" to buddy "aaron@gelter.com"'
    cp current_results.json previous_results.json
fi

rm -f current_results.json combined_results.json