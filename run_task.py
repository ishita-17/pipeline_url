from tasks import url_access
import requests

if __name__ == "__main__":
    url = "https://jionews.com/xpressnews/apis/v1.1/feeds/stream?langIds=1&catId=0&limit=10&epoch=0"
    url_access.delay(url)
    