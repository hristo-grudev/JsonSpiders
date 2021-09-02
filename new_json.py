import json


class CreateNews:
	def __init__(self, for_iteration, data_dict):
		self.for_iteration = for_iteration
		self.data_dict = data_dict

	@staticmethod
	def format_xpath(xpath):
		string_for_remove = ["concat( ' ', ", " ' ' ), concat( ' ', ", ", ' ' )"]
		for s in string_for_remove:
			xpath = xpath.replace(s, '')

		return xpath

	def parse_data(self):
		for key in self.for_iteration:
			print(f"Enter {key}:")
			data = input().replace('"', "'")
			self.data_dict["scrapy_arguments"][key] = CreateNews.format_xpath(data)
			if key == "body_xpath":
				self.data_dict["scrapy_arguments"][
					key] += "/node()[not(descendant-or-self::ins | descendant-or-self::noscript | self::meta | self::div)]"

			if data == '':
				del self.data_dict["scrapy_arguments"][key]

		return self.data_dict


class CreateFile:
	def __init__(self, name, data_dict):
		self.name = name
		self.data_dict = data_dict

	def create_file(self):
		with open(f'{self.name}.json', 'w', encoding="utf-8") as outfile:
			json.dump(self.data_dict, outfile, indent=4, ensure_ascii=False)


for_iter = {
	"start_urls": "",
	"menu_xpath": "",
	"articles_xpath": "",
	"title_xpath": "",
	"body_xpath": "",
	"pubdate_xpath": "",
	"author_xpath": ""
}

data_dict = {"scrapy_arguments":
	{
		"start_urls": "",
		"menu_xpath": "",
		"articles_xpath": "",
		"title_xpath": "",
		"body_xpath": "",
		"pubdate_xpath": "",
		"author_xpath": "",
		"link_id_regex": None
	}
}

data = CreateNews(for_iter, data_dict)
news = data.parse_data()

new_file = CreateFile('new_file', news)
new_file.create_file()