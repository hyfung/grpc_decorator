import grpc

class MyInterceptor(grpc.ServerInterceptor):
    def __init__(self):
        pass

    def intercept_service(self, continuation, handler_call_details):
        services = [
            
        ]
        print("Interceptor invoked")
        # client_ip = handler_call_details.peer
        # print(handler_call_details.peer())
        return continuation(handler_call_details)
