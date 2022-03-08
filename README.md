# csd-310
Database Development
<br>
<br/>

**Notes to users**
- Valid User ID's: `1` || `2` || `3`
- Every User has the same book by John Steinbeck initially added to their wishlist


## Start up Method 1

run `01_whatabook_db_init.sql` in your db.

run `whatabook.py`. 

<br>

## Start up Method 2

run `docker-compose -f "whatabook-docker-compose.yml" up -d --build` to build an image.

run `whatabook.py`.

Hint: If you are using Visual Studio Code you can also do this through the gui by right clicking whatabook-docker-compose.yml in the file directory and selecting ***Compose Up***.

<br>

##  Trouble shooting Method 2

run `docker-compose -f "whatabook-docker-compose.yml" logs` to look for errors.

<br>

## Clean up Method 2

run `docker-compose -f "whatabook-docker-compose.yml" down` to stop containers, remove containers, networks, volumes, and images created by up.

Hint: If you are using Visual Studio Code you can also do this through the gui by right clicking whatabook-docker-compose.yml in the file directory and selecting ***Compose Down***.

run  `docker system prune --all` to remove all unused containers, networks, and images.

run `docker ps -a` to list all the containers available locally. 

<!-- localhost root password 3306 enter -->
<!-- option control e to run your new query after connected to localhost and docker has been composed -->
