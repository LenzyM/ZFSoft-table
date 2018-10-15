#-*-coding:utf-8-*-
import os
import re
from lxml import etree
import requests
import sys
import urllib
from bs4 import BeautifulSoup
def func(studentnumber,password,name):
	s = requests.session()
	url = "http://202.115.80.211/default2.aspx"
	response = s.get(url)
	selector = etree.HTML(response.content)
	__VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]
	#获取验证码并下载到本地
	imgUrl = "http://202.115.80.211/CheckCode.aspx?"
	imgresponse = s.get(imgUrl, stream=True)
	print (s.cookies)
	image = imgresponse.content
	DstDir = os.getcwd()+"\\"
	print("保存验证码到："+DstDir+"code.jpg"+"\n")
	try:
		with open(DstDir+"code.jpg" ,"wb") as jpg:
			jpg.write(image)
	except IOError:
		print("IO Error\n")
	finally:
		jpg.close
	#手动输入验证码
	code = input("验证码是")
	code=str(code)
	#构建post数据
	data = {
	"__VIEWSTATE":__VIEWSTATE,
	"txtUserName":studentnumber,
	"TextBox2":password,
	"txtSecretCode":code,
	"Button1":"",
	}
	#提交表头，里面的参数是电脑各浏览器的信息。模拟成是浏览器去访问网页。
	headers = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
	}
	#登陆教务系统
	response = s.post(url,data=data,headers=headers)
	print ("成功进入")

	#得到登录信息，个人感觉有点多余。
	'''def getInfor(response,xpath):
		content = response.content.decode('gb2312') #网页源码是gb2312要先解码
		selector = etree.HTML(content)
		infor = selector.xpath(xpath)[0]
		return infor
	#获取学生基本信息
	text = getInfor(response,'//*[@id="xhxm"]/text()')
	text = text.replace(" ","")
	print (text)'''



	#获取课表，kburl是课表页面url,为什么有个Referer参数,这个参数代表你是从哪里来的。就是登录后的主界面参数。这个一定要有。
	kburl = "http://202.115.80.211/xskbcx.aspx?xh="+studentnumber+"&xm="+name+"%E6%9D%8E%E8%88%9F&gnmkdm=N121603"
	headers = {
	"Referer":"http://202.115.80.211/xs_main.aspx?xh="+studentnumber,
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
	 }
	response = s.get(kburl,headers=headers)
	#html代表访问课表页面返回的结果就是课表。下面做的就是解析这个html页面。
	html = response.content.decode("gb2312","ignore")
	selector=etree.HTML(html)
	content = selector.xpath('//*[@id="Table1"]/tr/td/text()')
	doc=open(name+'.txt','w')
	for each in content:
		if each.startswith('周'):
			print (each)
			print(each,file=doc)
	doc.close()
f=open("pswd.txt",'r')
for x in range(10):
	id=f.readline().strip()
	password=f.readline().strip()
	name=f.readline().strip()
	func(id,password,name)