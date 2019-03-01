# 解析html
from urllib.parse import urljoin
import re
from bs4 import BeautifulSoup

class HtmlParser(object):

	def _get_list_data(self, soup):
		res_datas = []
		res_data = {}

		# 解析具体的html页面信息
		sell_list = soup.find('ul', class_="sellListContent").find_all("li")

		for sell_item in sell_list:
			sell_info = sell_item.find('div', class_='info')
			# 具体字段
			res_data['title'] = sell_info.find('div', class_='title').find('a').get_text()
			res_data['flood'] = sell_info.find('div', class_='flood').find('div', class_='positionInfo').get_text()
			res_data['district'] = sell_info.find('div', class_='flood').find('div', class_='positionInfo').find('a').get_text()

			res_datas.append(res_data)

		return res_datas

	def parseurl(self, html_cont):
		if html_cont is None:
			return

		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
		new_data = self._get_list_data(soup)
		return new_data
