# Podman

## Table of Contents

- [Installation](#1-installation)
- [Basic Commands](#2-basic-commands)
- [Custom Images](#3-custom-images)

## Resources

- [Podman documentation](https://podman.io/docs)
- [Quay](https://quay.io/)
- [Docker Hub](https://hub.docker.com/search)
- [Docker extension](https://marketplace.visualstudio.com/items/?itemName=ms-azuretools.vscode-docker)

## Core Concepts

- Podman is rootless by default, which increases security.
- Podman can be used as a drop-in replacement for Docker, especially for development.
- Pair it with Podman Desktop for GUI management, and podman-compose for `docker-compose`-like orchestration.

## Installation

Install Podman on a Debian-based Linux distribution:

```bash
sudo apt-get update
sudo apt-get -y install podman
```

Verify the installation:

```bash
podman --version
```

Optional: Alias Podman as `docker` if you're used to Docker commands.

```bash
alias docker='podman'
```

This allows you to use `docker` commands and run Podman in the background.

## Basic Commands

### View Podman Help

```bash
podman --help
```

Shows a list of available commands and options.

### Run a Test Container

From Docker Hub:

```bash
podman run hello-world
```

From Quay.io (Podman's default registry):

```bash
podman run quay.io/podman/hello
```

### View Local Images

```bash
podman images
```

> [!TIP]
> You have to add images registries to avoid using `command docker.io/image`. For that, you have to add `unqualified-search-registries = ["docker.io", "quay.io"]` in the `/etc/containers/registries.conf`

Lists all downloaded images.

Images are fetched from container registries such as Docker Hub or Quay.io.

### Search for Images

Search on Docker Hub:

```bash
podman search docker.io/nginx
```

Search on Quay:

```bash
podman search quay.io/nginx
```

### Pull Images

```bash
# podman pull <image_name>
podman pull docker.io/nginx:latest
```

### Run a Web Server Container

Pull and run the official `nginx` image:

```bash
podman run docker.io/nginx
```

### Expose Container Ports

Map a container port to a host port:

```bash
podman run --publish <host_port>:<container_port> nginx
```

Example:

```bash
podman run -p 8080:80 nginx
```

The `-p` or `--publish` flag maps host and container ports.

### Run in Detached Mode

Run the container in the background (like a service):

```bash
podman run -p 8080:80 -d nginx
```

Or with long options:

```bash
podman run --publish 8080:80 --detach nginx
```

### View Logs from a Container

Show logs of a running or exited container:

```bash
podman logs <container_id | container_name>
```

Follow logs in real time:

```bash
podman logs -f <container_id | container_name>
```

### Assign a Name to a Container

Naming your containers makes them easier to manage:

```bash
podman run --name web -p 8080:80 -d nginx
```

### Execute Commands in a Running Container

Run a command inside the container:

```bash
podman exec <container_id | container_name> cat /etc/os-release
```

Open an interactive shell inside the container:

```bash
podman exec -it <container_id | container_name> bash
```

### Manage Containers

List running containers:

```bash
podman ps
```

List all containers (including stopped ones):

```bash
podman ps -a
```

Stop a container:

```bash
podman stop <container_id | container_name>
```

Start a stopped container:

```bash
podman start <container_id | container_name>
```

Remove a container:

```bash
podman rm <container_id | container_name>
```

Force remove a container (even if it's running):

```bash
podman rm -f <container_id | container_name>
```

Remove all containers:

```bash
podman rm -f $(podman ps -aq)
```

### Manage Images

List all images:

```bash
podman images
```

List only image IDs:

```bash
podman images -q
```

Remove a specific image:

```bash
podman rmi <image_id | image_name>
```

Remove all images:

```bash
podman rmi $(podman images -q)
```

### Add Environment Variables

You can pass environment variables when running containers:

```bash
podman run -e ACCEPT_EULA=Y -e VAR_NAME=value <image_name>
```

Example:

```bash
podman run -e ACCEPT_EULA=Y -e SECRET_KEY=abc123 my-app-image
```

## 3. Custom Images

Create a `Dockerfile` file or `Containerfile`. For instance

```dockerfile
FROM nginx:latest
WORKDIR /usr/share/nginx/html
COPY ./site .
EXPOSE 80
```

> [!NOTE]
> If you don't configure the `unqualified-search-registries`, you must to edit your Dockerfile/Containerfile with the source image registry `FROM docker.io/library/nginx:latest`

Build the docker image

```shell
# podman build --tag <name>:<version>
podman build -t star-wars-app:v1 .
```

Verify the Built Image

```shell
podman images
```

Run a Container from the Custom Image

```shell
podman run --name web -p 8080:80 -d star-wars-app:v1
```

Access the Application in the Container. Open `127.0.0.1:8080/index.html` in your browser
