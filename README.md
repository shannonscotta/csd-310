# csd-310
Database Development



## Start up 

run `docker-compose -f "whatabook-docker-compose.yml" up -d --build` to build an image.

If you are using Visual Studio Code you can also do this through the gui by right clicking whatabook-docker-compose.yml in the file directory and selecting ***Compose Up***.



##  Trouble shooting

run `docker-compose -f "whatabook-docker-compose.yml" logs` to look for errors.



## Clean up 

run `docker-compose -f "whatabook-docker-compose.yml" down` to stop containers, remove containers, networks, volumes, and images created by up.

If you are using Visual Studio Code you can also do this through the gui by right clicking whatabook-docker-compose.yml in the file directory and selecting ***Compose Down***.

run  `docker system prune --all` to remove all unused containers, networks, and images.

run `docker ps -a` to list all the containers available locally. 

<!-- localhost root password 3306 enter -->
<!-- option control e to run your new query after connected to localhost and docker has been composed -->