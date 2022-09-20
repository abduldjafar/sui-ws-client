export GOOGLE_APPLICATION_CREDENTIALS=/Users/abdulharisdjafar/Downloads/sui-data-ingestion-devnet-1c09ed59224f.json
export PUB_SUB_TOPIC=sui-dev
export PUB_SUB_PROJECT=sui-data-ingestion-devnet
export PUB_SUB_SUBSCRIPTION=sui-pull-raw-data
export CH_HOST=localhost
export CH_PASSWORD=""
export CH_USER=default
python main.py -ws 34.70.238.35  -wp 9001 -e subscribe