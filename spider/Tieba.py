# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from Counting.items import CountingItem
import re
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

class mySpider(CrawlSpider):
	name = 'count'
	allowed_domains = ["tieba.baidu.com"]
	start_urls = ['https://tieba.baidu.com/p/5475081737?pn='+str(i) for i in range (1,19)]

	def parse(self,response):
		page = response.body
		page = page.decode('utf-8')
		pattern = re.compile('d_post_content j_d_post_content ">(.*?)</div>', re.S)
		items = re.findall(pattern, page)
		filename = 'res.txt'
		data = CountingItem()
		data['content'] = []
		for item in items:
			A = Tool.replace(self=Tool,x=item)
			data['content'].append(str(A))
		return data
