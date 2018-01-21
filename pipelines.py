# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
class Count:
    def __init__(self, raw, data):
        self.load = raw  ##[]
        self.data = data  ##[[]]

    def CountCont(self):
        Cont = re.findall(".*: (.*)\[\[弃权]](.*).*", self.load)
        return Cont

    def getCont(self, Cont):
        vote = {}
        for i in range(len(Cont)):
            vote[Cont[i][0]] = 0
            vote[Cont[i][1]] = 0
        return vote

    def start(self, vote):

        plusOne = re.findall('.*\[\[(.*)]].*', self.data)
        for name in plusOne:
            if name in vote:
                vote[name] += 1
        return vote

    def result(self,Cont, vote):
        result = ""
        for i in range(len(Cont)):
            result += ("Area" + str(i + 1) + ":\n"
            +Cont[i][0] + " " + str(vote[Cont[i][0]])
            +"\n" + Cont[i][1] +" " + str(vote[Cont[i][1]]) + "\n\n")
        return result
class CountPipeline(object):
    def open_spider(self, spider):
        pass
    def close_spider(self, spider):
        F = open('C:\py project\CrawlingCount\Counting\Counting\contests.txt', encoding='utf-8')
        A = F.read()

        G = open('C:\py project\CrawlingCount\Counting\Counting\les.txt', encoding='utf-8')
        B = G.read()
        Example = Count(raw=A, data=B)
        Cont = Count.CountCont(self=Example)
        vote = Count.getCont(self=Example, Cont=Cont)
        vote = Count.start(self=Example, vote=vote)
        result = Count.result(self=Example, Cont=Cont, vote=vote)
        res = bytes(result, 'utf-8')
        filename = "finalres.txt"
        with open(filename, 'wb') as f:
            f.write(res)
    def process_item(self, item, spider):
        filename = "les.txt"
        with open(filename, 'ab') as f:
            for itemss in item['content']:
                T = bytes(itemss, 'utf-8')
                f.write(T)
        return item


