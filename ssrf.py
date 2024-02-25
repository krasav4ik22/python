import request
import requests, urlparse

# UnSafe
def fetch_url(request):
    url = request.GET.get('url')
    pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    
    if re.match(pattern, url):
        response = requests.get(url)
        return response.text
    else:
        return "Invalid URL"
    
#Unsafe
def fetch_url(request):
    url = request.GET.get('url')
    response = requests.get(url)
    return response.text


ALLOWED_DOMAINS = ['example.com', 'api.example.com']

#Safe
def fetch_url(request):
    url = request.GET.get('url')
    parsed_url = urlparse(url)
    
    if parsed_url.hostname in ALLOWED_DOMAINS:
        response = requests.get(url)
        return response.text
    else:
        return "Access denied"
    


