# sui-ws-client

## Description
Streaming transactions data throuught websocket to some destionation using python

## Destination
- [x] pubsub (google cloud platform)
- [ ] kafka
- [ ] cloud storage
- [ ] bigquery (google cloud platform)



## How To run 
1. setup environment variable
    ```
    pubsub (google cloud platform)
    export GOOGLE_APPLICATION_CREDENTIALS=key.json
    export PUB_SUB_TOPIC=sui-dev
    export PUB_SUB_PROJECT=sui-data-ingestion-devnet
    export PUB_SUB_SUBSCRIPTION=sui-dev-sub
    ```
2. install dependencies with `pip install -r req.txt`
3. run with `python main.py -ws sui.websocket.server -wp 9001`
