from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from .managment.commands.parsing import parse
from .models import News
import json
import asyncio


def response_data():
	response = News.objects.values()
	return {
		"error": None,
	    "status": True,
	    "payload": list(response),
	    }


def run_parser(func):
	try:
		loop = asyncio.get_event_loop()
	except RuntimeError:
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
	return loop.run_until_complete(func)


def parse_news(request):
	run_parser(parse.run())
	response = JsonResponse(response_data(), json_dumps_params={'ensure_ascii': False, 'separators': (",", ":"), "indent": 1}, safe=False)
	return HttpResponse(response, content_type="application/json")
# Create your views here.
