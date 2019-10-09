import aiohttp_jinja2
from aiohttp.web_urldispatcher import View


class WelcomeView(View):
    @aiohttp_jinja2.template('subpage/welcome.html')
    async def get(self):
        return {'name': 'RaspManager'}