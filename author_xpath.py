import pyperclip


def format_xpath(xpath):
	string_for_remove = ["concat( ' ', ", " ' ' ), concat( ' ', ", ", ' ' )"]
	for s in string_for_remove:
		xpath = xpath.replace(s, '')

	return xpath


while True:
	data = input().replace('"', "'")
	xpath = format_xpath(data)
	pyperclip.copy(f',\n"author_xpath": "{xpath}"')
