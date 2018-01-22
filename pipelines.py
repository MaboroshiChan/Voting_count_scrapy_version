

import re
class Count:
    def __init__(self, raw, data):
        self.load = raw  ##[]
        self.data = data  ##[[]]

    def CountCont(self):
        Cont = re.findall(".*: (.*)\[\[棄權]](.*).*", self.load)
        return Cont

    def getCont(self, Cont):
        vote = []
        for i in range(len(Cont)):
            vote.append({'left': 0, 'right': 0})
        return vote

    def start(self, vote):
        plusOneleft = re.findall('(\d*):\s\[\[(.*)]]', self.data)
        plusOneright = re.findall('(\d*):.*\[\[(.*)]]\n', self.data)
        for Contestor in plusOneleft:
            number1 = int(Contestor[0])
            vote[number1 - 1]['left'] += 1
        for Contestor in plusOneright:
            try:
                number2 = int(Contestor[0])
                vote[number2 - 1]['right'] += 1
            except:
                vote[0]['right'] += 1
        return vote

    def result(self, Cont, vote):
        result=""
        for i in range(len(Cont)):
            result += "Area" + str(i + 1) + ":\n" + Cont[i][0] + " " + str(vote[i]['left']) + "\n" + Cont[i][
                1] + " " + str(vote[i]['right']) + "\n\n"
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




