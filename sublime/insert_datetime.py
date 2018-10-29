import sublime
import sublime_plugin
import datetime

class InsertDatetime(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, self.view.sel()[0].begin(),
										 datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
