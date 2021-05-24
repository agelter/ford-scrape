#!/usr/bin/env bash

cd /Users/agelter/src/bimmer-scrape || true

source venv/bin/activate

rm -f ./dealercom_results.json ./dealeron_results.json ./dealerinspire_results.json

(
    cd dealers || true
    scrapy crawl ford_dealercom -o ../dealercom_results.json
    scrapy crawl ford_dealeron -o ../dealeron_results.json
    #scrapy crawl ford_dealerinspire -o ../dealerinspire_results.json
)

/usr/local/bin/jq -s 'flatten' dealercom_results.json dealeron_results.json > combined_results.json

rm -f ./dealercom_results.json ./dealeron_results.json ./dealerinspire_results.json

deactivate