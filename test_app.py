import pytest
import requests

url = 'http://127.0.0.1:5000'
m = {'file': open('images.jpg','rb')}
def test_base():

    r = requests.post(url+'/predict', files = m)

    #response = client.get(url)

    assert(r.status_code==200)
