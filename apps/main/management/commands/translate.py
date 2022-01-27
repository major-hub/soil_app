from django.core.management.base import BaseCommand
import requests
import polib


class Command(BaseCommand):
    help = 'Translate backend messages into three languages'

    def handle(self, *args, **options):
        self.gettext()

    def gettext(self, path=None):
        for code in ['uz', 'ru']:
            path = f'locale/{code}/LC_MESSAGES/django.po'
            po = polib.pofile(path)
            for entry in po[:9]:
                translated_text = self.translate(text=entry.msgid)
                entry.msgstr = translated_text
            po.save()

    def translate(self, text):
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
        data = {'target': 'uz', 'source': 'en', 'q': text}
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'accept-encoding': "application/gzip",
            'x-rapidapi-key': "9308132bdfmsh53dcf8575a26e84p1bcf9djsn83d4f3136c65",
            'x-rapidapi-host': "google-translate1.p.rapidapi.com"
        }
        response = requests.request("POST", url, data=data, headers=headers)
        result = response.json()['data']['translations'][0]['translatedText']
        return result

    def translate_google_json(self, text):
        url = "https://google-translate20.p.rapidapi.com/translate"
        payload = "text=The%20POST%20method%20has%20several%20advantages%20over%20GET%3A%20it%20is%20more%20secure%20because%20most%20of%20the%20request%20is%20hidden%20from%20the%20user%3B%20Suitable%20for%20big%20data%20operations.&tl=ru&sl=en"
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': "d141769529mshe4d869cfaae484ep13ce48jsn82e9e32b15a4",
            'x-rapidapi-host': "google-translate20.p.rapidapi.com"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
