# 输出html

class HtmlOutputer(object):
	def __init__(self):
		self.datas = []

	def collect_data(self, data):
		if data is None:
			return
		self.datas.append(data)

	# 这里输出结果
	def output_data(self):
		return self.datas