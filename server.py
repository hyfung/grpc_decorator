import ping_pb2, ping_pb2_grpc, grpc
from concurrent import futures
import interceptor
import time, functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result  # Return the result of the original function
    return wrapper

def reject(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return ping_pb2.Message(args="REJECTED")
    return wrapper

class PingServicer(ping_pb2_grpc.PingServicer):
    def __init__(self):
        return None

    @decorator
    def Ping(self, request, context):
        print(context.peer())
        return ping_pb2.Message(args="Pong")

    @reject
    def Bang(self, request, context):
        return ping_pb2.Message(args="Bong")

interceptors = (
    interceptor.MyInterceptor(),
    )

server = grpc.server(
    futures.ThreadPoolExecutor(max_workers=10),
    interceptors=interceptors
    )

ping_pb2_grpc.add_PingServicer_to_server(PingServicer(), server)

server.add_insecure_port("127.0.0.1:50051")
server.start()
server.wait_for_termination()
