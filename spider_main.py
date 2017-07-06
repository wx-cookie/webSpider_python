#!usr/bin/env python
#-*- coding: utf-8 -*-

import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()


	def craw(self, root_url):
		self.urls.add_new_url(root_url)
		count = 1
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print 'craw %d:%s' %(count, new_url)
				html_content = self.downloader.downloader(new_url)
				#print '1'
				new_urls, new_data = self.parser.parse(new_url, html_content)
				#print new_urls
				self.urls.add_new_urls(new_urls)
				#print '3'
				self.outputer.collect_data(new_data)
			except Exception, e:
				print e

			if count == 20:
				break
			count = count+1
			

		self.outputer.output_html()

if __name__=='__main__':
	root_url = 'http://baike.baidu.com/view/4072022.htm'
	spider = SpiderMain()
	spider.craw(root_url)