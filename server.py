from concurrent import futures
import grpc
import time
import pandas
import gRPC_project_pb2
import gRPC_project_pb2_grpc


db_name = "db.csv"


class SetKeyService(gRPC_project_pb2_grpc.setKeyServiceServicer):

    def set_key(self, request, context):
        data = pandas.read_csv(db_name)
        new_id = len(data)
        data = data.append({"key": request.key}, ignore_index=True)
        data.to_csv(db_name, index=False)
        return gRPC_project_pb2.Key(key_id=new_id)


class GetKeyService(gRPC_project_pb2_grpc.getKeyServiceServicer):

    def get_key(self, request, context):
        data = pandas.read_csv(db_name)
        if len(data) < request.key_id - 1:
            return gRPC_project_pb2.Key(key=None)
        return gRPC_project_pb2.Key(key=data.iloc[request.key_id].key)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    gRPC_project_pb2_grpc.add_setKeyServiceServicer_to_server(SetKeyService(), server)
    gRPC_project_pb2_grpc.add_getKeyServiceServicer_to_server(GetKeyService(), server)
    server.add_insecure_port("localhost:8081")
    server.start()
    print("Server started. Awaiting jobs...")
    try:
        while True:  # since server.start() will not block, a sleep-loop is added to keep alive
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
