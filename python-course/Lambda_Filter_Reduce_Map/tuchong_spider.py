#_*_ coding:utf-8 _*_
import urllib2
from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
import sys
import time
import os
import json

reload(sys)
sys.setdefaultencoding('utf8')

def getDeeperData(url):
	driver=webdriver.PhantomJS(executable_path='./phantomjs.exe')
	driver.get(url)
	tempdata=driver.page_source
	bsObj=BeautifulSoup(str(tempdata),"lxml")
	if bsObj!=None:
		return bsObj
	else:
		print "Get bsObj Error!"
		return None



def getData(keyword,page):

	imageUrl=[]
	urlList=getOuterUrl(keyword,str(page))

	for url in urlList:
		print "Now getting the url:"+url+'\n'
		print "Will Saving in "+str(page)+" Directory\n"
		imageUrl+=getImageList(getDeeperData(url))

	
	saveImage(imageUrl,str(page))

	del imageUrl[:]

		
def getOuterUrl(book_tag,page):
	url="https://tuchong.com/rest/tags/"+urllib.quote(book_tag)+"/posts?page="+page+"&count=20&order=weekly"
	jsonStr=urlopen(url).read()
	jsonObj=json.loads(jsonStr)
	urlCache=[]
	for num in range(len(jsonObj['postList'])):
		urlCache.append(jsonObj['postList'][num]['url'])
	return urlCache


def getImageList(bsObj):
	print "Get ImageUrl!\n"
	pagelist=bsObj.findAll('img',{'class':'multi-photo-image'})
	if bsObj==None:
		print "bsObj is None Retuen!"
		return
	imageLists=[x.attrs["src"] for x in pagelist]
	
	return imageLists

	

def saveImage(imageList,savaDirName):
	abspath=os.path.abspath(".")
	savePath=abspath+'\\'+savaDirName
	if not os.path.exists(savePath):
		os.makedirs(savePath,0777)

	for imglst in imageList:
		urllib.urlretrieve(imglst,savePath+'\\'+imglst.split('/')[-1])




if __name__=='__main__':
	count=23
	while True:
		getData("私房",count)
		count+=1
		if count==100:
			break




