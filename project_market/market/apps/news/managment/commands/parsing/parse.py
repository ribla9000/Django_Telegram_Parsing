import re
from bs4 import BeautifulSoup as bs
from aiohttp import ClientSession
from .text_changer import text_validator
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from news.models import News

yandex_url = "https://t.me/s/market_marketplace"
ozon_url = "https://t.me/s/ozonmarketplace"


async def check_all_news(data_tg, tag_):
	soup = bs(data_tg, "html.parser")
	response = {}
	item, link = "", ""
	count = 0
	tg_message = soup.find_all("div", class_="tgme_widget_message_bubble")
	tg_footer = soup.find_all("div", class_="tgme_widget_message_footer compact js-message_footer")
	for data_message, data_footer in zip(tg_message[::-1], tg_footer[::-1]):
		link = ""
		count += 1
		if count == 11:
			break
		tg_content = data_message.find_all("a", class_="tgme_widget_message_photo_wrap", href=True)
		title_author = data_message.find("a", class_="tgme_widget_message_owner_name").find("span").get_text()
		for data_content in tg_content:
			content = re.findall(r"https://cdn4.*.*.jpg", str(data_content))[0]
			link += content + "\n\n"
		response["message"], response["detail"] = data_message.get_text().split(), data_footer.get_text().split()
		response["date"] = data_message.find("a", class_="tgme_widget_message_date").find("time")
		response_list = [elem for elem in response["message"] if elem not in response["detail"]]
		item = await text_validator(" ".join(response_list).replace(title_author, "")) + "\n"
		if not News.objects.filter(description=item).exists():
			News(
				tag=tag_,
				title=title_author,
				description=item,
				detail=response["detail"],
				content=link,
				date=str(response["date"]["datetime"]),
			).save()

	return


async def main():
	async with ClientSession() as session:
		async with session.get(ozon_url) as response_ozon, session.get(yandex_url) as response_yandex:
			data_ozon, data_yandex = await response_ozon.text(), await response_yandex.text()
			await check_all_news(data_yandex, "[YANDEX]")
			await check_all_news(data_ozon, "[OZON]")
	return


async def run():
	return await main()
