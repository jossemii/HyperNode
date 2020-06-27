from flask import Flask
import buildImage
import os

if __name__ == "__main__":

    app = Flask(__name__)
    gateway_node_port = 8080

    def who_father_image_container_is(dependency):
        # 1. Miro de que puerto viene la peticion
        # 2. Miro que contenedor tiene asignado ese puerto en la subred docker0.
        # 3. Miro de que imagen proviene ese contenedor.
        # 4. Accedo al registro de father_image y obtengo el puerto de la dependencia.
        return 2, 4

    @app.route('/')
    def hello():
        return 'HELLO HYPER'

    @app.route('/<image>')
    def get(dependency):
        api_port, gateway_port = buildImage.ok(str(dependency)) # Si no esta construido, lo construye.
        pod_port = buildImage.select_port()
        father_container_id, dependency_port_from_father_container = who_father_image_container_is(dependency = dependency)
        os.system('docker stop '+father_container_id)
        os.system('docker run --detach -p 127.0.0.1:'+pod_port+':'+api_port+' -p 127.0.0.1:'+gateway_node_port+':'+gateway_port+' '+dependency+'.oci') # Ejecuta una instancia de la imagen con el puerto pod_port.
        os.system('docker run --detach -p 127.0.0.1:'+pod_port+':'+dependency_port_from_father_container+' '+father_container_id)

    @app.route('/<port_uri>')
    def delete(port_uri):
        pass

    app.run(host='0.0.0.0', port=8080)