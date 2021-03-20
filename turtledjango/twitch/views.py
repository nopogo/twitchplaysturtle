# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView
import websocket

class IndexView(TemplateView):
	template_name= "index.html"


async def websocket_view(socket: websocket):
	await socket.accept() 
	while True:
		message = await socket.receive_text()
		await socket.send_text(message)