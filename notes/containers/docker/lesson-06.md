# Persistir datos en Docker

This tutorial explores methods for **persisting data** in **Docker containers**. While containers are designed to be ephemeral and can "die" at some point, the data they work with often needs to survive. The video demonstrates how to prevent data loss and how these persistence methods integrate into real applications, using examples and the Tour of Heroes application.

## 1. Core Concepts

- **Data Persistence:** The ability for data to outlive the **container** that created or used it. This is crucial because containers can be stopped, removed, or replaced.
- **Bind Mounts:** A type of data persistence that maps a directory on the **Host** machine (your local computer where Docker is running) directly to a directory inside the **Container**. Any changes made in the Host directory are instantly reflected in the Container, and vice-versa. This method is tightly coupled to the specific Host filesystem path.
  - **Use Cases:** Highly useful for **development environments** where you are actively modifying code on your Host and want the changes to be immediately available inside the container for testing. Also used in scenarios like **monitoring** where containers might need access to Host logs.
  - **Portability:** Less portable because the Host path needs to exist and be the same on any machine running the container.
  - **Access Modes:** Can be configured for **read/write** (`rw`) or **read-only** (`ro`) access.
- **Volumes:** A type of data persistence managed directly by **Docker**. Docker handles where the volume data is stored on the **Host**, abstracting the specific path from the user.
  - **Use Cases:** Recommended for most general data persistence needs, especially for application data like databases.
  - **Portability:** More portable than Bind Mounts because Docker manages the underlying storage location. You only need to refer to the volume by its name.
  - **Lifecycle:** **Volumes do not die** when the container using them is removed. They persist until explicitly removed.
  - **Management:** Volumes can be named, inspected to find their location, their content can be explored, and they can be cloned. Data can be copied into a volume within a container using `docker cp`. Paid Docker subscriptions may offer export/backup features.
- **Tempfs Mounts:** A type of temporary data storage that occupies **Host memory** (RAM) instead of writing to the filesystem.
  - **Use Cases:** Suitable for scenarios where high **performance** is critical (memory is faster than disk) or for storing **sensitive information** that should not be permanently written to disk.
  - **Availability:** Requires Docker to be installed directly on a **Linux machine**. Not demonstrated in this video.
  - **Lifecycle:** Data is stored in memory and **does not persist** after the container stops.

## 2. Practical Steps

### Demonstrating Bind Mounts

1.  Open a terminal.
2.  Run an Nginx container using a **Bind Mount** with the `-v` parameter (older format):
    ```bash
    docker run --name deadpool-nginx -p 8080:80 -d -v $(pwd)/deadpool-site:/usr/share/nginx/html nginx
    ```
    - `$(pwd)/deadpool-site`: The absolute path to the directory on the Host.
    - `/user/share/nginx/html`: The target directory inside the container.
3.  Verify the container is running (`docker ps`) or using the Docker extension in VS Code.
4.  Open the container in a browser (e.g., `localhost:8080`) to see the content served from the Host directory.
5.  Modify a file (e.g., `script.js`) in the Host directory mapped by the Bind Mount.
6.  Refresh the browser; the changes should appear instantly because it's a live mapping, not a copy.
7.  Inspect the Bind Mount configuration using the Docker extension in VS Code or Docker Desktop to confirm the mapping and read/write status.

8.  Run an Nginx container using a **Bind Mount** with the recommended `--mount` parameter:
    ```bash
    docker run --name deadpool-readonly -p 8081:80 -d --mount type=bind,source=$(pwd)/deadpool-site,target=/usr/share/nginx/html nginx
    ```
    - `type=bind`: Specifies the mount type.
    - `source=...`: Specifies the Host path.
    - `target=...`: Specifies the Container path.
9.  To make the mount **read-only** from the container's perspective, add `ro` or `readonly` to the mount options:
    ```bash
    docker run --name deadpool-readonly -p 8081:80 -d --mount type=bind,source=$(pwd)/deadpool-site,target=/usr/share/nginx/html,ro nginx
    ```
10. Attempt to write a file inside the container using the read-only mount (e.g., `docker exec deadpool-readonly echo "Hello World" > /usr/share/nginx/html/index.html`). It should fail with a permission denied error.
11. Modify a file in the Host directory again. Changes should still be possible from the Host side.

---

### Demonstrating Volumes

1.  Run an Nginx container using a **Volume** with the `--mount` parameter:

    ```bash
    docker run --name wolverine-site -p 8083:80 -d --mount type=volume,source=wolverine-data,target=/usr/share/nginx/html nginx
    ```

    - `type=volume`: Specifies the mount type.
    - `source=wolverine-data`: Specifies the name for the volume. (If source is omitted, Docker generates a random name).
    - `target=/usr/share/nginx/html`: Specifies the target directory inside the container.

    Can also create the volume with the command:

    ```shell
    docker volume create <name>
    ```

2.  Inspect the volume configuration using the Docker extension in VS Code or Docker Desktop; it will show the volume name instead of a Host path.
3.  Open the container in a browser (e.g., `localhost:8083`). Initially, you might see the default Nginx welcome page if the image initializes the directory, because the volume is empty.
4.  Copy content into the container's volume using the `docker cp` command:

    ```bash
    docker cp wolverine-site/. wolverine-site:/usr/share/nginx/html
    ```

5.  Refresh the browser; the content copied into the volume should now be served.
6.  View the content stored in the volume using Docker Desktop or by exploring the volume content directly via the Docker extension in VS Code. (`Explore in a Dev Container` option).
7.  Demonstrate **volume persistence** by removing the container (`docker rm -f wolverine-site`) and then creating a _new_ container using the _same volume name_ (`source=wolverine-data`). The data will still be present in the new container because the volume persisted.
