import datetime

def simpleMiddleWare(get_response):
    #one time configuration and initialization
    def middleware(request):
        print(f"Before request [{datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S')}] Request URL: {request.path}")
        #Code to be exceted for each request before 
        # the view and later (middleware are called)
        response = get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        print(f"After Request [{datetime.datetime.now().strftime('%y/%m/%d %S:%M:%H')}] Response Status: {response.status_code}")
        return response
    
    return middleware