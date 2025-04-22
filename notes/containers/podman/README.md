# Podman

## Resources

- [Podman documentation](https://podman.io/docs)
- [Quay](https://quay.io/)
- [Docker Hub](https://hub.docker.com/search)

## Installation

- Install Podman CLI for Linux

  ```shell
  sudo apt-get update
  sudo apt-get -y install podman
  ```

- Verify the version

  ```shell
  podman --version
  ```

- Optionally you can create an alias for podman

  ```shell
  alias docker='podman'
  ```

## Basic Commands

```shell
podman --help
```

```shell
# From DockerHub
podman run hello-world

# From Quay
podman run quay.io/podman/hello
```

```shell
podman images
```

Images come from Container registries (Docker Hub, Quay)

```shell
podman search docker.io/nginx
podman search quay.io/nginx
```

Run nginx

```shell
podman run docker.io/nginx
```

Configure ports

```shell
podman run --publish 8080:80 nginx
podman run -p 8080:80 nginx
```

Detach mode

```shell
podman run --publish 8080:80 --detach nginx
podman run -p 8080:80 -d nginx
```

See logs

```shell
#
podman logs <container_id | container_name>

#
podman logs -f <container_id | container_name>
```

Give a name

```shell
podman run --name web --publish 8080:80 --detach nginx
```
