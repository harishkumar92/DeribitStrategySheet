from deribit_api import RestClient

def create_client(key, secret):
	client = RestClient(key, secret)
	client.index()
	client.account()
	return client

def get_index_price(client):
	return client.get_index_price


def straddle():
	pass



if __name__ == '__main__':
	key = r'2R6Snex45F1yY'
	secret = r'BR5E3VKV3RVBLDG2CRLHI2DDPOVX34QG'
	client = create_client(key, secret)
