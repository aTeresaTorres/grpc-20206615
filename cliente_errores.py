import grpc

import saludo_pb2
import saludo_pb2_grpc

canal = grpc.insecure_channel("localhost:50051")
stub = saludo_pb2_grpc.SaludadorStub(canal)

# 1) Matricula valida
r = stub.SaludarUno(saludo_pb2.SaludoRequest(nombre="Teresa", matricula="20206615"))
print("(1)", r.mensaje)

# 2) Matricula con una X al final: el servidor debe rechazarla
try:
    stub.SaludarUno(saludo_pb2.SaludoRequest(nombre="Teresa", matricula="20206615X"))
except grpc.RpcError as e:
    print("(2) Error:", e.code().name, "-", e.details())

# 3) Streaming con tiempo limite de 2 segundos
try:
    for r in stub.SaludarVarios(saludo_pb2.SaludoRequest(nombre="Teresa", matricula="20206615"), timeout=2):
        print("(3) Llego:", r.mensaje)
except grpc.RpcError as e:
    print("(3) Error:", e.code().name, "-", e.details())