# Creating Custom Docker Images

## 1. Core Concepts

In this lesson, the core concepts around defining, building, and managing custom Docker images are explained:

- **Dockerfiles (Recipes):** Dockerfiles are text files that contain a set of instructions for building a Docker image. They act as a recipe, specifying everything needed to create the image, including the base operating system, necessary software, application code, and how the application should run.
- **Base Image (`FROM` instruction):** Every Dockerfile starts with the `FROM` instruction, which specifies the base image to use as the starting point. This could be a minimal OS image, an image with a specific language runtime, or a more complete application image like Nginx. You can specify different versions (tags) of the base image.
- **Working Directory (`WORKDIR` instruction):** The `WORKDIR` instruction sets the working directory for any subsequent instructions in the Dockerfile like `COPY`, `RUN`, `CMD`, and `ENTRYPOINT`. It's good practice to define a specific work directory. If the directory doesn't exist, it will be created.
- **Copying Files (`COPY` instruction):** The `COPY` instruction is used to copy files or directories from the build context (usually the directory where the Dockerfile is located) into the Docker image at a specified destination.
- **Exposing Ports (`EXPOSE` instruction):** The `EXPOSE` instruction informs Docker that the container listens on the specified network ports at runtime. While it doesn't actually publish the port, it serves as documentation and is used by the `-p` flag in `docker run` to map container ports to host ports.
- **Environment Variables (`ENV` instruction):** The `ENV` instruction sets environment variables within the Docker image. These variables are then available to the application running inside the container. This is useful for configuration, such as specifying the listening port for a .NET application.
- **Entrypoint (`ENTRYPOINT` instruction):** The `ENTRYPOINT` instruction configures a container that will run as an executable. It defines the primary command that will run when the container starts. This command can be combined with arguments provided via `CMD`.
- **Building Images (`docker build`):** The `docker build` command processes a Dockerfile and builds a Docker image based on the instructions within it. The `-t` or `--tag` flag is used to give the image a name and optionally a tag (version). The command typically ends with a dot (`.`) or a path, indicating the build context (the directory containing the Dockerfile and source files).
- **Image Tags (Versions):** Images can have different versions or variants specified by tags after the image name (e.g., `image_name:tag`). Using meaningful tags (like version numbers or descriptors) is crucial for managing different iterations of an image and ensuring consistency when running containers. The `latest` tag is used by default if no tag is specified, but relying solely on `latest` can lead to ambiguity regarding the actual content of the image.
- **Image Size:** The size of a Docker image is an important consideration. Large images consume more disk space, take longer to pull and push, and can impact scalability. The base image chosen and the contents added during the build process significantly influence the final image size.
- **Multistage Builds:** Multistage builds are a technique used in Dockerfiles to create smaller, more efficient images. They involve using multiple `FROM` instructions in a single Dockerfile, where each `FROM` instruction can have a different base image and serve a specific purpose (e.g., one stage for building/compiling the application, another for the final runtime image). Files are copied between stages, allowing you to discard build tools and dependencies that are not needed in the final runtime image.

## 2. Practical Steps

This lesson demonstrates the process of creating and running custom Docker images through several examples:

1.  **Prepare a Static Site Example:**
    Copy a directory containing static HTML and CSS files into your working directory.
2.  **Create a Dockerfile for the Static Site:**
    Create a file named `Dockerfile` in the same directory as the static site content. Add instructions to define the base image (Nginx), set the working directory, copy the static content, and expose the web server port.

    ```dockerfile
    FROM nginx:latest
    WORKDIR /usr/share/nginx/html
    COPY ./site .
    EXPOSE 80
    ```

3.  **Build the Docker Image:**
    Open a terminal in the directory containing the Dockerfile and static site content. Execute the `docker build` command, providing a tag (name and version) for the image and specifying the current directory (`.`) as the build context.

    ```bash
    docker build -t star-wars-app:v1 .
    ```

4.  **Verify the Built Image:**
    Use the `docker images` command in the terminal or check the Docker Desktop interface to see the newly created image listed among your local images.
5.  **Run a Container from the Custom Image:**
    Execute the `docker run` command, giving the container a name, mapping a host port to the exposed container port (80), running it in detached mode (`-d`), and specifying the name and tag of the custom image to use.

    ```bash
    docker run --name web -p 8080:80 -d star-wars-app:v1
    ```

6.  **Access the Application in the Container:**
    Open a web browser and navigate to `localhost` followed by the host port you mapped (e.g., `localhost:8080/index.html`) to see the static site being served from the container.

7.  **Modify the Source Code and Rebuild:**
    Edit the static site files (e.g., change a color in the CSS). Then, rebuild the image using the same build command but perhaps with a different tag to represent the change.

    ```bash
    # Example with a new tag for the modified version
    docker build -t star-wars-app:v2 .
    ```

8.  **Run a New Container with the Updated Image:**
    Run a new container from the updated image, mapping it to a different host port to avoid conflicts with the first container.

    ```bash
    docker run --name web2 -p 8070:80 -d star-wars-app:v2
    ```

9.  **Access Both Container Versions:**
    Verify that the original container (`localhost:8080`) shows the old content and the new container (`localhost:8070`) shows the updated content, demonstrating the importance of tags.
