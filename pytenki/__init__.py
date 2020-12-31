"""
Copyright 2020 Nils Müller

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

pytenki is a Python client for wttr.io that tries to stick as closely to the
standard library as possible. :)

"""
__version__ = "0.1.0"

import sys
import urllib.request


class WttrClient:
    base_url = "https://wttr.in"
    headers = {"User-Agent": "curl"}

    def get(self, lang="en"):
        headers = {**self.headers, "Accept-Language": lang}
        req = urllib.request.Request(url=self.base_url, headers=headers)
        resp = urllib.request.urlopen(url=req)
        return resp.read()

    def write(self, *args, **kwargs):
        data = self.get(lang=kwargs.get("lang", ""))
        output = kwargs.get("output", sys.stdout)
        output.buffer.write(data)


if __name__ == "__main__":
    client = WttrClient()
    client.write()
