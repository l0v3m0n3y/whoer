import requests
class Client():
	def __init__(self):
		self.api="https://whoer.net"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def geoip2_city(self):
		return requests.get(f"{self.api}/v2/geoip2-city",headers=self.headers).json()
	def geoip2_isp(self):
		return requests.get(f"{self.api}/v2/geoip2-isp",headers=self.headers).json()
	def ping_create(self,domain):
		return requests.get(f"{self.api}/ping/create?pingit={domain}",headers=self.headers).json()
	def ping_result(self,task_id):
		return requests.get(f"{self.api}/ru/ping/result?task_id={task_id}&servers=us5,hk2,it2,se2,ca2,nl4,th1,ru3,uk2,sg1,ch3,ua2,es1,pl2,ro1,de1,fr1,kr1,jp1,lv1",headers=self.headers).json()
	def ports(self):
		return requests.get(f"{self.api}/ports",headers=self.headers).json()