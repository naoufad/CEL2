
class IPMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        
        def __call__(self, request):
            # Code to be executed for each request before
            # the view (and later middleware) are called.
            if not request.META.get('REMOTE_ADDR',None):
                try:
                    request.META['REMOTE_ADDR'] = request.META['HTTP_X_REAL_IP']
                except:
                    request.META['REMOTE_ADDR'] = '1.1.1.1'
                    
        response = self.get_response(request)
                    
        return response



                                                                                            
