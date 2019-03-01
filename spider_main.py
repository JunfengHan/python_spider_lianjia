# 入口文件
import url_manager
import html_downloader
import html_parser
import html_outputer

class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url):
		# 向url管理器中添加新的url
		self.urls.add_new_url(root_url)
		try:
			new_url = self.urls.get_new_url()
			# 下载html内容
			html_cont = self.downloader.download(new_url)
			# 解析html内容
			new_data = self.parser.parseurl(html_cont)
			# 将解析出的data输出
			self.outputer.collect_data(new_data)

		except:
			print('craw failed...')

if __name__ == "__main__":
	root_url = "https://wh.lianjia.com/ershoufang/pg1/"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)