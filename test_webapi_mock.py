import json

import requests
import responses
import vcr


def fetch_address(zipcode: str) -> str:
    url = 'https://zipcloud.ibsnet.co.jp/api/search'
    params = {'zipcode': zipcode}

    response = requests.get(url, params=params)

    result = response.json()['results'][0]

    都道府県名 = result['address1']
    県名 = result['address2']
    市区町村名 = result['address3']

    return f'{都道府県名}{県名}{市区町村名}'


@vcr.use_cassette('fixtures/vcr_cassettes/7830060.yaml', filter_headers=['Authorization'])
def test_7830060は高知県南国市蛍が丘_vcrpyを利用する場合():
    zipcode = '7830060'

    assert fetch_address(zipcode) == '高知県南国市蛍が丘'


@responses.activate
def test_7830060は高知県南国市蛍が丘_responsesで完全にモックする場合():
    zipcode = '7830060'

    real_json = """{
	"message": null,
	"results": [
		{
			"address1": "高知県",
			"address2": "南国市",
			"address3": "蛍が丘",
			"kana1": "ｺｳﾁｹﾝ",
			"kana2": "ﾅﾝｺｸｼ",
			"kana3": "ﾎﾀﾙｶﾞｵｶ",
			"prefcode": "39",
			"zipcode": "7830060"
		}
	],
	"status": 200
}"""

    responses.add(responses.GET,
                  f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}',
                  json=json.loads(real_json))

    assert fetch_address(zipcode) == '高知県南国市蛍が丘'


@responses.activate
def test_7830060は高知県南国市蛍が丘_responsesで必要な部分だけモックする場合():
    zipcode = '7830060'

    responses.add(responses.GET,
                  f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}',
                  json={'results': [
                      {
                          'address1': '高知県',
                          'address2': '南国市',
                          'address3': '蛍が丘',
                      }
                  ]})

    assert fetch_address(zipcode) == '高知県南国市蛍が丘'
