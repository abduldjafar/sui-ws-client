datas= [
    {
		"jsonrpc": "2.0",
		"result": {
			"certificate": {
				"transactionDigest": "FKCiK6hvCQ7djV42wROqBQ8OOU0hgOhtAmNzo5j+tHI=",
				"data": {
					"transactions": [
						{
							"Call": {
								"package": {
									"objectId": "0x0000000000000000000000000000000000000002",
									"version": 1,
									"digest": "AQPKgwFrgFqEMKLlbdJC+cH66VJDerxcw1FVO2vPK90="
								},
								"module": "coin",
								"function": "join",
								"typeArguments": [
									"0x2::sui::SUI"
								],
								"arguments": [
									"0xb172e589d9765faf6b477131c06f0a0d4514aa8c",
									"0xf0a0e5ba7d6adc6aead4e4d91308a38562f99182"
								]
							}
						}
					],
					"sender": "0x9eeb58a4d618714b23066528ed6f641a05360683",
					"gasPayment": {
						"objectId": "0x78d5e42c4274c843fb2899259297e29548fa3285",
						"version": 3,
						"digest": "vIWGBAIXC10W4vYWBSYxv0hP/HAWXP4zObyPZ1V+GPU="
					},
					"gasBudget": 5000
				},
				"txSignature": "AG6sekflKTy/SSKsWbJv3YrqPX7m5h+lt3eba74DyIc9Cxr93EWuY1dqi2urTBuXiCl+JUEAD4N0Njg4svQqzwXachLur6X7txzp6fF0GdvfDDfepj7hTeW7Wp0B+CNOjg==",
				"authSignInfo": {
					"epoch": 0,
					"signature": "hD+mixHqQoR4lAXUr97Y543PC/JVFi4itaVP/Yamu3MHkZ0sJO5b/k8XMbFuO/eN",
					"signers_map": [
						58,
						48,
						0,
						0,
						1,
						0,
						0,
						0,
						0,
						0,
						2,
						0,
						16,
						0,
						0,
						0,
						0,
						0,
						1,
						0,
						3,
						0
					]
				}
			},
			"effects": {
				"status": {
					"status": "success"
				},
				"gasUsed": {
					"computationCost": 482,
					"storageCost": 32,
					"storageRebate": 48
				},
				"transactionDigest": "FKCiK6hvCQ7djV42wROqBQ8OOU0hgOhtAmNzo5j+tHI=",
				"mutated": [
					{
						"owner": {
							"AddressOwner": "0x9eeb58a4d618714b23066528ed6f641a05360683"
						},
						"reference": {
							"objectId": "0x78d5e42c4274c843fb2899259297e29548fa3285",
							"version": 4,
							"digest": "F5sDgeyVIx1jiVB5GTImIw2DSCiYvG4KoEzUrMvU0SU="
						}
					},
					{
						"owner": {
							"AddressOwner": "0x9eeb58a4d618714b23066528ed6f641a05360683"
						},
						"reference": {
							"objectId": "0xb172e589d9765faf6b477131c06f0a0d4514aa8c",
							"version": 4,
							"digest": "DnXpH+/ay/0UluOfVAfljU0djigOCLWIaOzeq15JXLQ="
						}
					}
				],
				"deleted": [
					{
						"objectId": "0xf0a0e5ba7d6adc6aead4e4d91308a38562f99182",
						"version": 2,
						"digest": "Y2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2M="
					}
				],
				"gasObject": {
					"owner": {
						"AddressOwner": "0x9eeb58a4d618714b23066528ed6f641a05360683"
					},
					"reference": {
						"objectId": "0x78d5e42c4274c843fb2899259297e29548fa3285",
						"version": 4,
						"digest": "F5sDgeyVIx1jiVB5GTImIw2DSCiYvG4KoEzUrMvU0SU="
					}
				},
				"events": [
					{
						"deleteObject": {
							"packageId": "0x0000000000000000000000000000000000000002",
							"transactionModule": "coin",
							"sender": "0x9eeb58a4d618714b23066528ed6f641a05360683",
							"objectId": "0xf0a0e5ba7d6adc6aead4e4d91308a38562f99182"
						}
					}
				],
				"dependencies": [
					"Q2FOPw51ffo/OPzrzvn0gzETcOjDVhcLPzuWe1IYcCw=",
					"RO6DGQrZS3aPPKzN2vNBzYJo6JJOminFTTHwSdjh3m0="
				]
			},
			"timestamp_ms": 1664814130380,
			"parsed_data": None
		},
		"id": "83800040-e479-4711-a0e5-fe08d3dbbd53"
	},
    {
		"jsonrpc": "2.0",
		"result": {
			"certificate": {
				"transactionDigest": "b3LCu3eR1ifvjCQmERuTK+uE53wPC/LxfpQ/vHPUhNI=",
				"data": {
					"transactions": [
						{
							"Call": {
								"package": {
									"objectId": "0x9502d6a899c64f851446d6369f20f2f2f18efcdd",
									"version": 1,
									"digest": "vblzWKrh9hAKTd6wMB1bMDFbknz6UrZWEGyOUvtFLEk="
								},
								"module": "movement2_module",
								"function": "do_update",
								"arguments": [
									"0xc8c5cba9004de41bf6876c27552385dd72b8d975",
									9999999827968,
									9999999827968,
									9999999827968,
									9999999827968,
									20
								]
							}
						}
					],
					"sender": "0x0ec2c415ecfdb5e55146e4d32675c1db38f4b261",
					"gasPayment": {
						"objectId": "0x0611f6300600f076639f75bd5ad8dd96862304b7",
						"version": 1068,
						"digest": "fd2rr8o+LjyiXa1yPns0hHgHd/gQQe0ortEas96s9ag="
					},
					"gasBudget": 2000
				},
				"txSignature": "AAOHMsRC6bY0hX/3s31xjSjSHD0LgACJXcvbRPyb8X6S9/zJFdL0POdF4Ep2rIvSKZSlAOsF3qQfK+sihkFErQhlK0XaVqP9wuY6aEXPvri3EN24NR/7p4cHZOzkVp57bw==",
				"authSignInfo": {
					"epoch": 0,
					"signature": "jAWICSJJF6HSv2Ho6eAab2c0kWd9sigYjFJ9edwKyEikGJkNRRcUoveMJiul1kYN",
					"signers_map": [
						58,
						48,
						0,
						0,
						1,
						0,
						0,
						0,
						0,
						0,
						2,
						0,
						16,
						0,
						0,
						0,
						1,
						0,
						2,
						0,
						3,
						0
					]
				}
			},
			"effects": {
				"status": {
					"status": "success"
				},
				"gasUsed": {
					"computationCost": 68,
					"storageCost": 34,
					"storageRebate": 34
				},
				"transactionDigest": "b3LCu3eR1ifvjCQmERuTK+uE53wPC/LxfpQ/vHPUhNI=",
				"mutated": [
					{
						"owner": {
							"AddressOwner": "0x0ec2c415ecfdb5e55146e4d32675c1db38f4b261"
						},
						"reference": {
							"objectId": "0x0611f6300600f076639f75bd5ad8dd96862304b7",
							"version": 1069,
							"digest": "XgXPmnU4S+jQybeJj84vm+qdKdePpA9hDKiLG526RUI="
						}
					},
					{
						"owner": {
							"AddressOwner": "0x0ec2c415ecfdb5e55146e4d32675c1db38f4b261"
						},
						"reference": {
							"objectId": "0xc8c5cba9004de41bf6876c27552385dd72b8d975",
							"version": 33,
							"digest": "iCaMwtdbCKLwSN2moSOM6wUTnh1UhEe4SBjAfQptLAg="
						}
					}
				],
				"gasObject": {
					"owner": {
						"AddressOwner": "0x0ec2c415ecfdb5e55146e4d32675c1db38f4b261"
					},
					"reference": {
						"objectId": "0x0611f6300600f076639f75bd5ad8dd96862304b7",
						"version": 1069,
						"digest": "XgXPmnU4S+jQybeJj84vm+qdKdePpA9hDKiLG526RUI="
					}
				},
				"events": [
					{
						"moveEvent": {
							"packageId": "0x9502d6a899c64f851446d6369f20f2f2f18efcdd",
							"transactionModule": "movement2_module",
							"sender": "0x0ec2c415ecfdb5e55146e4d32675c1db38f4b261",
							"type": "0x9502d6a899c64f851446d6369f20f2f2f18efcdd::movement2_module::PlayerStateUpdatedEvent",
							"fields": {
								"position": {
									"type": "0x9502d6a899c64f851446d6369f20f2f2f18efcdd::movement2_module::Vector2",
									"fields": {
										"x": 9999999827968,
										"y": 9999999827968
									}
								},
								"sequenceNum": 20,
								"velocity": {
									"type": "0x9502d6a899c64f851446d6369f20f2f2f18efcdd::movement2_module::Vector2",
									"fields": {
										"x": 9999999827968,
										"y": 9999999827968
									}
								}
							},
							"bcs": "AABwThgJAAAAAHBOGAkAAAAAcE4YCQAAAABwThgJAAAUAAAAAAAAAA=="
						}
					}
				],
				"dependencies": [
					"IeieMVQjAmtYrpN0kSdBeFvFcMxJ3pkFk9nydlbCZ1U=",
					"853mf/epFIOh2kCPI6+dYCEPDAFiLyj0pBsnFCKAQ78="
				]
			},
			"timestamp_ms": 1664893370672,
			"parsed_data": None
		},
		"id": "83800040-e479-4711-a0e5-fe08d3dbbd53"
	},
	{
		"jsonrpc": "2.0",
		"result": {
			"certificate": {
				"transactionDigest": "XGZzTX+qskZL43kZpFM5pALGBxr9cXtMo8FAK5LGlZs=",
				"data": {
					"transactions": [
						{
							"Call": {
								"package": {
									"objectId": "0x0000000000000000000000000000000000000002",
									"version": 1,
									"digest": "AQPKgwFrgFqEMKLlbdJC+cH66VJDerxcw1FVO2vPK90="
								},
								"module": "devnet_nft",
								"function": "mint",
								"arguments": [
									"Example NFT",
									"An NFT created by Sui Wallet",
									"ipfs://bafkreibngqhl3gaa7daob4i2vccziay2jjlp435cf66vhono7nrvww53ty"
								]
							}
						}
					],
					"sender": "0x33e079d8fee1b2b05039e067f1d50091a812af4f",
					"gasPayment": {
						"objectId": "0x4b498858c0135fad347934651d0dece7c5455a33",
						"version": 1,
						"digest": "ED2HGRJP34JsbDH7dCzMkVwIld1mf2E1Y3ZAmS5d2vU="
					},
					"gasBudget": 10000
				},
				"txSignature": "AOX+2M6kW37xiMZe92Hq3kTCMS10Yn5evHcM2Ng7XMbRw/oNy5BZGGmlhASI5HKZhgVfBKeNyWz+UM5981pq9wZmZUTdnvUo9Nlt4hlqUsbMKAOdD04KNTk2a2JN+7Im2g==",
				"authSignInfo": {
					"epoch": 0,
					"signature": "iguuDoStBYxKvb1S3wBXGKVwSy58JZTBruhwCj18oC3Na5ePcHIyfL6vdMwVY/ve",
					"signers_map": [
						58,
						48,
						0,
						0,
						1,
						0,
						0,
						0,
						0,
						0,
						2,
						0,
						16,
						0,
						0,
						0,
						0,
						0,
						2,
						0,
						3,
						0
					]
				}
			},
			"effects": {
				"status": {
					"status": "success"
				},
				"gasUsed": {
					"computationCost": 834,
					"storageCost": 40,
					"storageRebate": 16
				},
				"transactionDigest": "XGZzTX+qskZL43kZpFM5pALGBxr9cXtMo8FAK5LGlZs=",
				"created": [
					{
						"owner": {
							"AddressOwner": "0x33e079d8fee1b2b05039e067f1d50091a812af4f"
						},
						"reference": {
							"objectId": "0x331b660a2f3119f7280af02408220c50e4364595",
							"version": 1,
							"digest": "798PDJ60vfG7sxVnE58h76Feq7OcZTMtYB9smBGoZfc="
						}
					}
				],
				"mutated": [
					{
						"owner": {
							"AddressOwner": "0x33e079d8fee1b2b05039e067f1d50091a812af4f"
						},
						"reference": {
							"objectId": "0x4b498858c0135fad347934651d0dece7c5455a33",
							"version": 2,
							"digest": "Qo8mEt8DevN+uBWuSgLkNy1NIC+gwB5wbLTfQVMo/gg="
						}
					}
				],
				"gasObject": {
					"owner": {
						"AddressOwner": "0x33e079d8fee1b2b05039e067f1d50091a812af4f"
					},
					"reference": {
						"objectId": "0x4b498858c0135fad347934651d0dece7c5455a33",
						"version": 2,
						"digest": "Qo8mEt8DevN+uBWuSgLkNy1NIC+gwB5wbLTfQVMo/gg="
					}
				},
				"events": [
					{
						"moveEvent": {
							"packageId": "0x0000000000000000000000000000000000000002",
							"transactionModule": "devnet_nft",
							"sender": "0x33e079d8fee1b2b05039e067f1d50091a812af4f",
							"type": "0x2::devnet_nft::MintNFTEvent",
							"fields": {
								"creator": "0x33e079d8fee1b2b05039e067f1d50091a812af4f",
								"name": "Example NFT",
								"object_id": "0x331b660a2f3119f7280af02408220c50e4364595"
							},
							"bcs": "MxtmCi8xGfcoCvAkCCIMUOQ2RZUz4HnY/uGysFA54Gfx1QCRqBKvTwtFeGFtcGxlIE5GVA=="
						}
					},
					{
						"newObject": {
							"packageId": "0x0000000000000000000000000000000000000002",
							"transactionModule": "devnet_nft",
							"sender": "0x33e079d8fee1b2b05039e067f1d50091a812af4f",
							"recipient": {
								"AddressOwner": "0x33e079d8fee1b2b05039e067f1d50091a812af4f"
							},
							"objectId": "0x331b660a2f3119f7280af02408220c50e4364595"
						}
					}
				],
				"dependencies": [
					"K6Trp+DKu+505xz8yUpOTtIvOJDRDH5TrL7F3liDsxE="
				]
			},
			"timestamp_ms": 1664893422693,
			"parsed_data": None
		},
		"id": "83800040-e479-4711-a0e5-fe08d3dbbd53"
	},
	{
		"jsonrpc": "2.0",
		"result": {
			"certificate": {
				"transactionDigest": "K2CdNiTci9gknKtlTTbeaqpo4+YzmmgO2cTesl7DxT8=",
				"data": {
					"transactions": [
						{
							"TransferSui": {
								"recipient": "0xad10a0cfc0dd6d49bbd89cf7138a302ea71acfad",
								"amount": 10000000
							}
						}
					],
					"sender": "0xc4173a804406a365e69dfb297d4eaaf002546ebd",
					"gasPayment": {
						"objectId": "0x28ec9e04cbb5f6e5a4cd3e03afd3c6845aa4b257",
						"version": 2673,
						"digest": "C81HCqdz+JHoNiJXS9grpR8lYqdnAgQNOOl3n5TF7W8="
					},
					"gasBudget": 1000
				},
				"txSignature": "AIQye1TtICNUL6YYkbjIUrFIrjQ/gaO29thEHGNordmpAB4Wp8FsWbdtqLNrILvgQzT4YqwcAeOVcLxD3PHxUQ7UY+EceRWUXoasK3LYi4GQz62P97SOfriSwnWlzwo+gg==",
				"authSignInfo": {
					"epoch": 0,
					"signature": "s1lrkWI+CdIGcGi80Ow6anvuXfQNNOKQadtZ/QJiAvXVx/qVMx42CbiJkfm6p3+Z",
					"signers_map": [
						58,
						48,
						0,
						0,
						1,
						0,
						0,
						0,
						0,
						0,
						2,
						0,
						16,
						0,
						0,
						0,
						0,
						0,
						2,
						0,
						3,
						0
					]
				}
			},
			"effects": {
				"status": {
					"status": "success"
				},
				"gasUsed": {
					"computationCost": 45,
					"storageCost": 48,
					"storageRebate": 32
				},
				"transactionDigest": "K2CdNiTci9gknKtlTTbeaqpo4+YzmmgO2cTesl7DxT8=",
				"created": [
					{
						"owner": {
							"AddressOwner": "0xad10a0cfc0dd6d49bbd89cf7138a302ea71acfad"
						},
						"reference": {
							"objectId": "0xf37c06d6cef6a2e9be1fb17a60d72c2a990857c6",
							"version": 1,
							"digest": "1fUNay4ot6iZdd1+oKoiMg8sa5ayynY+Sec7G1wsuf4="
						}
					}
				],
				"mutated": [
					{
						"owner": {
							"AddressOwner": "0xc4173a804406a365e69dfb297d4eaaf002546ebd"
						},
						"reference": {
							"objectId": "0x28ec9e04cbb5f6e5a4cd3e03afd3c6845aa4b257",
							"version": 2674,
							"digest": "4xQ14R7zQo1OtqsHjzU2Rv3CLbyryWzWr/I7ySDxlnU="
						}
					}
				],
				"gasObject": {
					"owner": {
						"AddressOwner": "0xc4173a804406a365e69dfb297d4eaaf002546ebd"
					},
					"reference": {
						"objectId": "0x28ec9e04cbb5f6e5a4cd3e03afd3c6845aa4b257",
						"version": 2674,
						"digest": "4xQ14R7zQo1OtqsHjzU2Rv3CLbyryWzWr/I7ySDxlnU="
					}
				},
				"events": [
					{
						"transferObject": {
							"packageId": "0x0000000000000000000000000000000000000002",
							"transactionModule": "native",
							"sender": "0xc4173a804406a365e69dfb297d4eaaf002546ebd",
							"recipient": {
								"AddressOwner": "0xad10a0cfc0dd6d49bbd89cf7138a302ea71acfad"
							},
							"objectId": "0x28ec9e04cbb5f6e5a4cd3e03afd3c6845aa4b257",
							"version": 2673,
							"type": "Coin",
							"amount": 10000000
						}
					}
				],
				"dependencies": [
					"esJaE+DAH3qLapV4Fax3rzLXOmjuxTqWS5FU6lW8cbI="
				]
			},
			"timestamp_ms": 1664891997846,
			"parsed_data": None
		},
		"id": "83800040-e479-4711-a0e5-fe08d3dbbd53"
	},
	
]

for data in datas:
    transaction = data["result"]["certificate"]["data"]["transactions"][0]
    transaction_full_datas = data["result"]["certificate"]["data"]
    timestamp_ms = round((data["result"]["timestamp_ms"]/1000)%60)
    sender = transaction_full_datas["sender"]
    

    if "TransferSui" in transaction.keys():
        recipient = transaction["TransferSui"]["recipient"]
        amount = transaction["TransferSui"]["amount"]
        print(f"{sender} sent {amount} SUI to {recipient} {timestamp_ms}s ago")

    elif "Call" in transaction.keys():
        module = transaction["Call"]["module"]
        function = transaction["Call"]["function"]

        if module == "devnet_nft" and function == "mint":
            print(f"{sender} create a NFT {timestamp_ms}s ago")

        elif module == "movement2_module" and function == "do_update":
            print(f"{sender} update state in game at {timestamp_ms}s ago")
        
        elif module == "coin" and function == "join":
            print(f"{sender} join coin at {timestamp_ms}s ago")

