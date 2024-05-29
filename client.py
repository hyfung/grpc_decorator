import ping_pb2, ping_pb2_grpc, grpc
from concurrent import futures

channel = grpc.insecure_channel("127.0.0.1:50051")

ping_stub = ping_pb2_grpc.PingStub(channel)

message = ping_pb2.Message(args="Ping")

response = ping_stub.Ping(message)
print(response)

message = ping_pb2.Message(args="Bang")

response = ping_stub.Bang(message)
print(response)
