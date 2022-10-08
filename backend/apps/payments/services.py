import urllib.parse

import httpx


API_BASE_URL = "https://hackathon.lsp.team/hk"


def new_wallet():
	url = urllib.parse.urljoin(API_BASE_URL, '/v1/wallets/new')
	headers={
		"Accept": "application/json"
	}
	wallet_json = httpx.post(url, headers=headers).json()
	return wallet_json['privateKey'], wallet_json['publicKey']


def new_transaction(sender, receiver, amount):
	url = urllib.parse.urljoin(API_BASE_URL, '/v1/transfers/matic')
	headers = {
		"Content-Type": "application/json",
		"Accept": "application/json"
	}
	data = {
		"fromPrivateKey": sender,
		"toPublicKey": receiver,
		"amount": amount
	}
	transaction_json = httpx.post(url, data=data).json()
	return transaction_json['transactionHash']