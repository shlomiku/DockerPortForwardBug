# DockerPortForwardBug
This is a project to demonstrate these bugs:

https://github.com/docker/docker/issues/21699

https://github.com/docker/docker/issues/22325

the effect of the bug can be demonstrated here: 
https://www.youtube.com/watch?v=3iIstDEb8eY

to run the project run this command:
docker-compose.exe -f dev.yml up

then go here:
http://192.168.99.100:8888/
(change ip to yours. I am running docker on a windows machine)
