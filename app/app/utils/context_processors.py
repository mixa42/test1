from django.template import RequestContext
from django.template.context_processors import request

# request_context = RequestContext(request)
# request_context.push({"localisation": "ru"})

def get_client_ip_address(request):
    '''
        информация о браузере клиента
    '''
    req_headers = request.META
    x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for_value:
        ip_addr = x_forwarded_for_value.split(',')[-1].strip()
    else:
        ip_addr = req_headers.get('REMOTE_ADDR')
    return {'client_ip': ip_addr}

