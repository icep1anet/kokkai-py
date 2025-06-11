from typing import Union
from urllib.parse import quote

import requests
from kokkai_params import KokkaiParams
from kokkai_response import KokkaiMeetingResponse, KokkaiSpeechResponse

BASE_URL = "http://kokkai.ndl.go.jp/api/"


class KokkaiAPI:
    def __init__(self):
        self.BASE_URL = BASE_URL
        self._safe = ":/?=&"

    def _encode(self, url: str):
        url = quote(url, safe=self._safe)
        return url

    def api_call(
        self, url: str, api_type: str
    ) -> Union[KokkaiMeetingResponse, KokkaiSpeechResponse]:
        url = self._encode(url)
        response = requests.get(url)
        if api_type == "meeting":
            data = response.json()
            return KokkaiMeetingResponse(**data)
        elif api_type == "speech":
            data = response.json()
            return KokkaiSpeechResponse(**data)
        else:
            return

    def meeting_list(self, params: KokkaiParams) -> KokkaiMeetingResponse:
        url = self.BASE_URL + "meeting_list"
        if params.to_query():
            url += f"?{params.to_query()}"
        return self.api_call(url, api_type="meeting")

    def meeting(self, opts) -> KokkaiMeetingResponse:
        url = self.BASE_URL + "meeting"
        if opts:
            url += "?"
            for key, value in opts.items():
                url += f"{key}={value}&"
        return self.api_call(url, api_type="meeting")

    def speech(self, params: KokkaiParams) -> KokkaiSpeechResponse:
        url = self.BASE_URL + "speech"
        if params.to_query():
            url += f"?{params.to_query()}"
        return self.api_call(url, api_type="speech")
