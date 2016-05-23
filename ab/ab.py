"""
 这是一个ab的替代程序，但是实现的功能不完善
"""

import threading
import time
import http.client


 

class RequestThead(threading.Thread):
	#构造函数
	def __init__(self,thread_name):
		threading.Thread.__init__(self)
		self.test_count = 0
		self.error_count = 0
		self.size = 0

	#线程运行的主函数s
	def run(self):
		i = 0
		while i< TEST_COUNT:
			self.test_performance()
			i +=1
	#测试请求函数		
	def test_performance(self):
		conn = http.client.HTTPConnection(SERVER_NAME)
		try:
			conn.request("get","/")
			rsps = conn.getresponse()
			rsps.getheaders() 
			if rsps.status ==200:
				#读取返回的数据
				data = rsps.read()
			self.size += (int)(rsps.getheader("content-length")) 
			#print (self.size)
			self.test_count += 1
		except:
			print('error')
			self.error_count += 1
			#continue
		conn.close()
		
if __name__ == "__main__":
	#需要测试的服务器
	SERVER_NAME = input("http://")
	#发送请求的数量
	thread_count = (int)(input("-n: "))
	#每次发送请求的数量
	TEST_COUNT = (int)(input("-c: "))
	#测试开始时间
	start_time = time.time()
	threads = []
	count = 0
	i = 0
	while i < thread_count/TEST_COUNT:
		t = RequestThead("thread"+ str(i))
		threads.append(t)
		t.start()
		i +=1
	TEST_COUNT = thread_count%TEST_COUNT
	t = RequestThead("thread"+ str(i))
	threads.append(t)
	t.start()
	word = ""

	while True:
		word = input("cmd:\n")
		if word =="s":
			time_span = time.time()-start_time
			all_count  = 0
			error = 0
			total = 0
			html = 0
			for t in threads:
				all_count += t.test_count
				error += t.error_count
				html += t.size
			print("server port",80)
			print("html transferred:",html)
			print("time for test: " ,time_span,"seconds")
			print("complete requests:  ",all_count)
			print("failed requests: ",error)
			print("%s Request/Second" %str(all_count/time_span))
			print("transfer rate: %s bytes/Second"%str(html/time_span),)
		elif word == "e":
			TEST_COUNT = 0
			for t in threads:
				t.join(0)
			break
			
		