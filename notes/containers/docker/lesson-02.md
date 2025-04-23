# Docker CLI Fundamentals

## 1. Core Concepts

- **Docker CLI and Docker Engine:** The Docker CLI is a tool that allows users to launch commands through the terminal. These commands are understood by the Docker Engine, which is the motor that executes containers. The Docker CLI acts as a client to the API exposed by the Docker Engine.
- **Containers and Images:** Containers are instances of applications that you want to execute. Images are the blueprints that tell Docker what to execute.
- **Container Registry (Docker Hub):** Images are stored in container registries. Docker Hub is a default container registry provided by the Docker company, which includes both free and paid tiers. Anyone can upload images to Docker Hub or other registries, so it's important to be cautious and ensure the images are safe and reliable.
- **Trusted Content on Docker Hub:** To help identify reliable images, Docker Hub provides filters like official Docker images, images from verified publishers, and images sponsored by Docker. The lesson also mentions the possibility of analyzing images for vulnerabilities.
- **Image Layers:** Images are built in layers. Docker optimizes image downloads by reusing layers that are common across different images, saving time and disk space.
- **Container Isolation and Port Mapping:** By default, containers are isolated from each other and from the host machine. To access a service running inside a container (like a web server or database) from the host machine, you need to **map a local port to the container's listening port**. This is done using the `-p` or `--publish` parameter.
- **Detached Mode:** When you run a container, it can stay attached to the terminal, showing its logs. To free up your terminal while the container runs in the background, you can run it in **detached mode** using the `-d` or `--detach` parameter.
- **Container Logs:** You can view the logs of a running or stopped container using the `docker logs` command. You can also connect to the logs in real-time using the `-f` parameter. Docker Desktop also provides an easy way to view logs through its interface.
- **Naming Containers:** Docker automatically assigns random, funny names to containers. You can assign a **custom, memorable name** using the `--name` parameter when running a container. This name can then be used instead of the container ID for commands like `docker logs` or `docker stop`.
- **Executing Commands Inside Containers:** You can execute commands directly inside a running container using the `docker exec` command. Docker Desktop provides an interactive terminal for this. You can also connect to the container's terminal interactively using `docker exec -it` followed by the desired shell (e.g., `bash`).
- **Listing Containers:** The `docker ps` command shows only **running** containers. Adding the `-a` parameter (`docker ps -a`) shows **all** containers, including those that have stopped.
- **Managing Containers:** Containers can be **stopped** (`docker stop`), **started** (`docker start`), and **removed** (`docker rm`). A container must typically be stopped before it can be removed. However, you can **force removal** of a running container using the `-f` parameter with `docker rm`.
- **Managing Images:** Images can be **removed** using the `docker rmi` command.
- **Environment Variables:** Some containers require **environment variables** to be set for configuration (like accepting an EULA or setting a password). These can be passed to a container when running it using the `-e` parameter.

## 2. Practical Steps

Verify Docker CLI installation.

```bash
docker version
```

View the main Docker commands.

```bash
docker --help
```

Run the `hello-world` container. Docker will download the image if not found locally, run the container, display a message, and the container will exit.

```bash
docker run hello-world
```

List images downloaded on your machine.

```bash
docker images
```

Search for an image (e.g., `nginx`). (The lesson notes that searching via `dockerhub.com` or Command+K in Docker Desktop is generally preferred due to richer information).

```bash
docker search nginx
```

Run the `nginx` container. This will download the image (showing layers being downloaded) if not local and then start the container, which typically stays running. It will attach to the terminal, showing logs.

```bash
docker run nginx
```

Stop the attached container (press Ctrl+C).

Clear the terminal.

```bash
clear
cls # for Windows
```

Run the `nginx` container again, this time mapping local port 8080 to the container's port 80. The container will still be attached to the terminal.

```bash
docker run -p 8080:80 nginx
```

Stop the attached container (press Ctrl+C).

Run the `nginx` container with a custom name (`web`), map ports, and run in detached mode (`-d`). The command parameters usually go before the image name.

```bash
docker run --name web -d -p 8080:80 nginx
```

View the logs of the container named `web`.

```bash
docker logs web
```

View the logs of the container named `web` and stay connected to see new logs in real-time. (Press Ctrl+C to disconnect)

```bash
docker logs -f web
```

Execute a command (`cat /etc/os-release`) inside the `web` container to see its operating system.

```bash
docker exec web cat /etc/os-release
```

Connect interactively to the terminal (bash shell) of the `web` container. (Type `exit` to disconnect)

```bash
docker exec -it web bash
```

List only running containers.

```bash
docker ps
```

List all containers, including stopped ones.

```bash
docker ps -a
```

Remove a stopped container using its ID or name. (Replace `<container_id_or_name>` with the actual ID or name)

```bash
docker rm <container_id_or_name>
```

Attempt to remove the running container named `web` (this will show an error).

```bash
docker rm web
```

Stop the running container named `web`.

```bash
docker stop web
```

Remove the now stopped container named `web`.

```bash
docker rm web
```

Start a stopped container (e.g., the Hello World container) using its ID or name. (Replace `<container_id_or_name>` with the actual ID or name)

```bash
docker start <container_id_or_name>
```

Force-remove a running container using its ID or name. (Replace `<container_id_or_name>` with the actual ID or name)

```bash
docker rm -f <container_id_or_name>
```

List the IDs (`-q`) of all containers (`-a`).

```bash
docker ps -a -q
```

Remove all containers using a combined command. This command gets the IDs of all containers and passes them to `docker rm`, forcing (`-f`) removal even if they are running.

```bash
docker rm -f $(docker ps -a -q)
```

List images.

```bash
docker images
```

Remove an image using its name or ID (e.g., `httpd`).

```bash
docker rmi httpd
```

List the IDs (`-q`) of all images.

```bash
docker images -q
```

Remove all images using a combined command. This command gets the IDs of all images and passes them to `docker rmi`.

```bash
docker rmi $(docker images -q)
```

## 3. Use Case

Run a Microsoft SQL Server container, name it `db`, run detached, map local port 1433 to container port 1433, and set environment variables (`-e`) for EULA acceptance and the SA password. (Replace `<your_password>` with a strong password)

```bash
docker run --name db -d -p 1433:1433 -e ACCEPT_EULA=Y -e SA_PASSWORD='<your_password>' mcr.microsoft.com/mssql/server:2022-latest
```

Execute a SQL command inside the running `db` container using `sqlcmd` to verify data (e.g., selecting heroes after inserting them via Azure Data Studio). (Replace `<your_password>` with the SA password used above and `HeroesDB` with the database name)

```bash
docker exec db /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P '<your_password>' -d HeroesDB -Q "SELECT * FROM Heroes"
```
