import grpc

import saludo_pb2
import saludo_pb2_grpc

canal = grpc.insecure_channel("localhost:50051")
stub = saludo_pb2_grpc.SaludadorStub(canal)

peticion = saludo_pb2.SaludoRequest(nombre="Teresa", matricula="20206615")
for respuesta in stub.SaludarVarios(peticion):
    print("Llego:", respuesta.mensaje)
print("Fin del stream")