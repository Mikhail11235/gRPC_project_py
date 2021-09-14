import grpc
import gRPC_project_pb2
import gRPC_project_pb2_grpc


def run():
    _message_name = int(input("Choose the service (0 - set key; 1 - get key):\n"))
    with grpc.insecure_channel("localhost:8081") as chanel:
        if _message_name == 0:
            stub = gRPC_project_pb2_grpc.setKeyServiceStub(chanel)
            response = stub.set_key(gRPC_project_pb2.Key(key=input("Enter key:\n")))
            print("key was added with key_id: %s" % response.key_id)
        elif _message_name == 1:
            stub = gRPC_project_pb2_grpc.getKeyServiceStub(chanel)
            response = stub.get_key(gRPC_project_pb2.Key(key_id=int(input("Enter key id:\n"))))
            if not response.key:
                print("Error: Invalid key_id")
            else:
                print("key: %s" % response.key)
        else:
            run()


run()
