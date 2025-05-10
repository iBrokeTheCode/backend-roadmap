# Docker Networking Explained

This tutorial explores the networking capabilities within **Docker**, focusing on how containers communicate with each other and the outside world. It covers the different built-in networking modes provided by Docker upon installation, including **None**, **Host**, and the default **Bridge** network. The video also explains **Port Mapping** as a mechanism for external access to containers. Crucially, it demonstrates the advantages of creating **custom networks**, which enable containers to communicate using their names via a built-in **DNS** server, a more robust approach than relying on dynamic internal IPs. The learning objective is to understand these concepts and apply them to connect multiple containers in a practical application scenario.

## 1. Core Concepts

- **Default Docker Networks:** When Docker is installed, it configures three default network options:

  - **Bridge Network:** This is the **default network** for containers if no specific network is specified. Containers on the same bridge network receive internal **IP addresses** and can communicate with each other using these IPs. However, these internal IPs are **dynamic** and can change, making communication unreliable if relying solely on IPs. Accessing a container on the bridge network from the host machine typically requires **Port Mapping**. The built-in DNS server is not enabled on the default bridge network for security reasons.
  - **Host Network:** This mode allows a container to **share the network interface** with the **Host machine** where Docker is installed. This means the container directly uses the Host's ports. The advantage is potentially higher performance due to fewer network hops, beneficial in scenarios where **low latency** is critical. The disadvantage is that if multiple containers need to use the same port, only one can run on that port on the Host network at a time, requiring potentially many Host machines. When using Docker Desktop, the "Host" is typically a virtual machine, not your local machine, which affects how this mode behaves unless specific settings are enabled.
  - **None Network:** Containers configured with this network mode have **no network interface**. They are completely **isolated** and cannot communicate with other containers or the outside world.

- **Port Mapping (`-p` or `--publish`):** This mechanism is used to make a container's internal port accessible from the Host machine's external network. You map a port on the Host (e.g., `8080`) to a specific port inside the container (e.g., `80`). This allows external applications (like a web browser on your machine) to reach the container via the Host's IP and the specified Host port.

  - **`EXPOSE` Instruction:** Found in a **Dockerfile**, this instruction documents the ports that a container intends to listen on. It does **not** actually publish the port or make it accessible externally.
  - **Publish All (`-P` or `--publish-all`):** This option automatically maps all ports documented with the `EXPOSE` instruction in an image to **randomly assigned ports** on the Host machine.

- **Custom Networks:** Users can create their own networks using `docker network create`.
  - **Built-in DNS Server:** A key advantage of custom networks is that Docker provides a built-in **DNS** server. This server allows containers connected to the same custom network to resolve each other's IP addresses using their **container names**. This makes communication between containers much more reliable than relying on dynamic internal IPs, especially when containers are stopped, started, or reordered.

## 2. Practical Steps

1.  **List Default Networks:**

    ```bash
    docker network list
    ```

    This command shows the default networks: `bridge`, `host`, and `none`.

2.  **Inspect the Default Bridge Network:**

    ```bash
    docker inspect network bridge
    ```

    This command shows details about the default bridge network, including the containers connected to it and their assigned internal IPs.

3.  **Run a Container on the Default Bridge Network (No Port Mapping):**

    ```bash
    docker run -d nginx
    ```

    This runs an Nginx container detached (`-d`). Without port mapping, you cannot access it from the host machine's browser. Trying to open in a browser via the Docker extension will indicate no port is available.

4.  **Run a Container on the Default Bridge Network with Specific Port Mapping:**

    ```bash
    docker run -d -p 8080:80 nginx
    ```

    This runs an Nginx container detached and maps Host port `8080` to container port `80`. You can now access Nginx via `localhost:8080` on your Host machine.

5.  **Inspect an Image to Find Exposed Ports:**

    ```bash
    docker inspect image nginx
    ```

    Look for the `ExposedPorts` section in the output. For the Nginx image, it shows port `80` is exposed. This information can also be seen in the Docker extension in VS Code or Docker Desktop.

6.  **Run a Container Publishing All Exposed Ports (`-P`):**

    ```bash
    docker run -d -P nginx
    ```

    This runs an Nginx container detached and automatically maps the container's exposed port (`80`) to a random high port on the Host machine. You can find the mapped port by inspecting the running container.

    You can also expose many ports. For example, create a Dockerfile to expose many PORTS, build an image and run a container.

    ```dockerfile
    FROM nginx

    EXPOSE 80/TCP
    EXPOSE 80/UDP

    EXPOSE 8080
    EXPOSE 8081
    EXPOSE 8082
    ```

---

7.  **Communicate Between Containers on the Default Bridge Network (using IP):**

    - Run a container (`busybox`) interactively on the bridge network with auto-removal:
      ```bash
      docker run -it --rm busybox
      ```
      The `--rm` flag removes the container when you exit. The `-it` flag connects you interactively.
    - Inside the `busybox` container, find the IP address of another container (e.g., an Nginx container) from the `docker inspect network bridge` output.
    - Use `wget` to make a request to the other container's internal IP:
      ```bash
      wget -qO- http://<container_internal_ip>
      ```
      Replace `<container_internal_ip>` with the actual IP. This demonstrates internal communication via IP on the default bridge network.

8.  **Run a Container on the Host Network:**

    ```bash
    docker run -d --network host nginx
    ```

    This runs an Nginx container using the Host network. By default in Docker Desktop, accessing `localhost:80` may not reach this container. You might need to enable "Enable Host networking" in Docker Desktop settings.

9.  **Run a Container on the None Network:**

    ```bash
    docker run -it --network none busybox
    ```

    Connect interactively to a `busybox` container on the none network.

    - Inside the container, run `ifconfig`:
      ```bash
      ifconfig
      ```
      You will only see the `lo` (loopback) interface, confirming no external network connectivity.

10. **Create a Custom Network:**

    ```bash
    docker network create tour-heroes-bnet
    ```

    This creates a new bridge network named `tour-heroes-bnet`. Verify its creation using `docker network list`.

11. **Build an Image with Network Tools:**

        - Create a Dockerfile (e.g., `Dockerfile.ubuntu-nettools`) with content like:
          ```dockerfile
          FROM ubuntu
          RUN apt-get update && apt-get install -y iputils-ping wget
          ```
        - Build the image:
          `bash

    docker build -t ubuntu-with-net-tools -f Dockerfile.ubuntu-nettools .
    `      This builds an image based on Ubuntu with`ping`and`wget` installed.

12. **Run Containers on the Custom Network (using Names):**

    - Run the first container:
      ```bash
      docker run -it --name donPepito --network tour-heroes-bnet ubuntu-with-net-tools
      ```
      This runs an interactive container named `donPepito` on the `tour-heroes-bnet` network.
    - Run the second container in a separate terminal:
      ```bash
      docker run -it --name DonJose --network tour-heroes-bnet ubuntu-with-net-tools
      ```
      This runs an interactive container named `DonJose` on the same network.
    - Inside the `donPepito` container, ping `DonJose` by name:
      ```bash
      ping DonJose
      ```
      The built-in DNS resolves the name to the correct IP, and the ping is successful.
    - Inside the `DonJose` container, ping `donPepito` by name:
      ```bash
      ping donPepito
      ```
      This also works, showing bidirectional communication using names.

13. **Set up Tour of Heroes Application with a Database:**

    - Ensure you have the necessary application code, including modifications to connect to a SQL Server database (e.g., using Entity Framework in a .NET application). This includes configuring the connection string in `appsettings.json` to point to the database container by its name and the default SQL Server port (1433).
    - Run a SQL Server container on the custom network:
      ```bash
      docker run -d --name db --network tour-heroes-bnet -e ACCEPT_EULA=Y -e SA_PASSWORD=<YourStrongPassword> mcr.microsoft.com/mssql/server:2019-latest
      ```
      Replace `<YourStrongPassword>` with a strong password. This runs the database container named `db` on the custom network.

14. **Build and Run the API Container on the Custom Network:**

    - Build the API image from its Dockerfile:
      ```bash
      docker build -t tour-heroes-api:v1 .
      ```
    - Run the API container on the custom network with Port Mapping for external access:
      ```bash
      docker run -d --name api --network tour-heroes-bnet -p 5051:5000 tour-heroes-api:v1
      ```
      This runs the API container named `api` on the custom network, mapping container port `5000` (where the API listens) to Host port `5051`. The API container can communicate with the `db` container using its name (`db`) because they are on the same custom network. External access to the API is via `localhost:5051`.

15. **Build and Run the Frontend Container:**

    - Modify the frontend application code (e.g., Angular) to call the API using the Host's external address and mapped port (e.g., `http://localhost:5051`).
    - Build the frontend image from its Dockerfile:
      ```bash
      docker build -t tour-heroes-web:v1 .
      ```
    - Run the frontend container:
      ```bash
      docker run -d --name web -p 80:80 tour-heroes-web:v1
      ```
      This runs the frontend container, mapping container port `80` to Host port `80`. The frontend container runs on the default bridge network or no specific network, but it accesses the API via the Host's mapped port, not via the internal custom network.

16. **Verify the Running Application:**

    - Access the frontend application in your browser at `http://localhost` (or the mapped port if different). The frontend calls the API via `localhost:5051`, the API communicates with the `db` container via the custom network's DNS (`db:1433`), retrieves data, and serves it back to the frontend.

17. **Clean Up Resources:**
    - Stop and remove all running containers:
      ```bash
      docker stop $(docker ps -q)
      docker rm $(docker ps -aq)
      ```
      Alternatively, use `docker container prune` to remove stopped containers. Individual containers can be removed using the Docker extension or `docker rm <container_name_or_id>`.
    - Remove unused images, especially intermediate or dangling images:
      ```bash
      docker image prune
      ```
      Individual images can be removed using the Docker extension or `docker rmi <image_name_or_id>`.
    - Remove custom networks (only possible if no containers are attached):
      ```bash
      docker network prune
      ```
      Individual networks can be removed using the Docker extension or `docker network rm <network_name_or_id>`.
