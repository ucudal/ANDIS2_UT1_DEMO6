# Universidad Católica del Uruguay

## Facultad de Ingeniería y Tecnologías

### Análisis y diseño de aplicaciones II

# Demo de facilidad de modificación y de despliegue

El contexto de esta demo es un sitio de *e-commerce* en el que hay usuarios que
compran productos mediante órdenes. La demo implementa una arquitectura de
microservicios, compuesta por varios servicios independientes llamados
`users-service` para los usuarios, `products-service` para los productos,
`orders-service` para las órdenes de compra, y finalmente `api-gateway` para
integrar en una única
[interfaz](https://github.com/ucudal/ANDIS_Conceptos/blob/main/4_Conceptos/4_Interfaz.md)
las interfaces de los servicios anteriores; la demo busca ilustrar en la
práctica los conceptos de [facilidad de
modificación](https://github.com/ucudal/ANDIS_Conceptos/blob/main/4_Conceptos/4_Facilidad_de_modificacion.md)
y de
[despliegue](https://github.com/ucudal/ANDIS_Conceptos/blob/main/4_Conceptos/4_Facilidad_de_despliegue.md)
en sistemas distribuidos modernos.

## Estructura del Proyecto

| Carpeta/Archivo      | Descripción                                      |
|----------------------|--------------------------------------------------|
| api-gateway/         | Puerta de entrada al sistema, enruta las peticiones a los microservicios correspondientes. |
| orders-service/      | Servicio de gestión de órdenes.                  |
| products-service/    | Servicio de gestión de productos.                |
| users-service/       | Servicio de gestión de usuarios.                 |
| commands.azcli       | Comandos útiles para despliegue y administración.|
| README.md            | Este archivo.                                    |

Para ejecutar esta demo usa los comandos que están [aquí](./commands.azcli). Con
el complemento [Azure CLI
Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azurecli)
es posible ejecutar los comandos directamente desde Visual Studio Code.

## Requisitos

- Python
- [Docker Desktop](https://docs.docker.com/desktop/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

## Actividades

Estudia los componentes de la demo y analiza cómo la forma en la que está
implementada podría facilitar o dificultar la facilidad de modificación y de despliegue.