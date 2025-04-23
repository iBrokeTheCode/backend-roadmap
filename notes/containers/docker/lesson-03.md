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

    > [!ERROR]
    > Error: creating build container: short-name "nginx:latest" did not resolve to an alias and no unqualified-search registries are defined in "/etc/containers/registries.conf"

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

---

## Continues at minute 12:00

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
10. **Clean Up (Optional):** Stop and remove the running containers and images if no longer needed (commands not explicitly shown in this excerpt but implied from previous lessons).
11. **Create a .NET Web API Project:**
    Use the .NET CLI to create a new Web API project.

    ```bash
    dotnet new webapi -o TourOfHeroesApi
    ```

12. **Modify the .NET API Code:**
    Navigate into the project directory and modify the default API code (e.g., `Program.cs`) to serve custom data (like a list of heroes) instead of the default weather forecast.
13. **Run the .NET API Locally:**
    Execute `dotnet run` in the project directory to test the API locally and access its endpoints via a browser (e.g., `localhost:<port>`, `localhost:<port>/api/Hero`).
14. **Create an Initial Dockerfile for the .NET API (Requires Manual Publish):**
    Create a `Dockerfile` in the root of the .NET API project directory. Define the base image (`aspnet:8.0`), set the working directory, expose the application port (5000), set the `ASPNETCORE_URLS` environment variable, copy the _published_ application output, and define the entry point to run the application DLL.

    ```dockerfile
    FROM aspnet:8.0
    WORKDIR /app
    EXPOSE 5000
    ENV ASPNETCORE_URLS="http://+:5000"
    COPY publish .
    ENTRYPOINT ["dotnet", "TourOfHeroesApi.dll"]
    ```

15. **Manually Publish the .NET Project:**
    Before building the image from the Dockerfile above, manually publish the .NET project using the .NET CLI to create the `/publish` directory containing the build output.

    ```bash
    dotnet publish -c Release -o publish
    ```

16. **Build the .NET API Docker Image (Version 1):**
    Build the Docker image using the `docker build` command, tagging it appropriately.

    ```bash
    docker build -t tour-of-heroes-api:v1 .
    ```

17. **Run a Container from the .NET API Image (Version 1):**
    Run a container from the built image, mapping a host port (e.g., 9000) to the container's exposed port (5000).

    ```bash
    docker run --name tour-of-heroes-api-v1 -p 9000:5000 -d tour-of-heroes-api:v1
    ```

18. **Access the Containerized .NET API:**
    Access the API endpoints via a browser using the mapped host port (e.g., `localhost:9000`, `localhost:9000/api/Hero`).
19. **Create a Second Dockerfile for the .NET API (Includes Build Step):**
    Replace the content of the Dockerfile to use a .NET SDK base image, copy the project files, run `dotnet publish` _within_ the Docker build process, set the working directory, expose the port, set the environment variable, copy the published output from the build location (within the image) to the final app directory, and define the entry point.

    ```dockerfile
    FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
    WORKDIR /src
    COPY ["TourOfHeroesApi.csproj", "./"]
    RUN dotnet restore
    COPY . .
    RUN dotnet publish -c Release -o /app

    FROM mcr.microsoft.com/dotnet/aspnet:8.0
    WORKDIR /app
    EXPOSE 5000
    ENV ASPNETCORE_URLS="http://+:5000"
    COPY --from=build /app .
    ENTRYPOINT ["dotnet", "TourOfHeroesApi.dll"]
    ```

20. **Build the .NET API Docker Image (Version 2):**
    Build the image using the updated Dockerfile. Note that you don't need to manually publish the project beforehand.

    ```bash
    docker build -t tour-of-heroes-api:v2 .
    ```

21. **Run a Container from the .NET API Image (Version 2):**
    Run a container from the v2 image, mapping it to a different host port (e.g., 9001).

    ```bash
    docker run --name tour-of-heroes-api-v2 -p 9001:5000 -d tour-of-heroes-api:v2
    ```

22. **Compare Image Sizes:**
    Use `docker images` to compare the sizes of `tour-of-heroes-api:v1` (around 221MB) and `tour-of-heroes-api:v2` (around 911MB), highlighting the impact of including the SDK in the image.
23. **Create a Third Dockerfile for the .NET API (Multistage Build):**
    Replace the Dockerfile content with a multistage build definition. This involves a first stage using the .NET SDK image to perform the build/publish and a second, final stage using the smaller ASP.NET runtime image, copying only the published output from the first stage.

    ```dockerfile
    FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
    WORKDIR /src
    COPY ["TourOfHeroesApi.csproj", "./"]
    RUN dotnet restore
    COPY . .
    RUN dotnet publish -c Release -o /app /p:UseAppHost=false

    FROM mcr.microsoft.com/dotnet/aspnet:8.0
    WORKDIR /app
    EXPOSE 5000
    ENV ASPNETCORE_URLS="http://+:5000"
    COPY --from=build /app .
    ENTRYPOINT ["dotnet", "TourOfHeroesApi.dll"]
    ```

24. **Build the .NET API Docker Image (Version 3 - Multistage):**
    Build the image using the multistage Dockerfile.

    ```bash
    docker build -t tour-of-heroes-api:v3 .
    ```

25. **Verify the Size of the Multistage Image:**
    Use `docker images` again. The `v3` image should be significantly smaller, similar in size to the `v1` image (around 221MB), demonstrating the effectiveness of multistage builds.
26. **Run a Container from the Multistage Image:**
    Run a container from the smaller, multistage-built image, mapping it to a different host port (e.g., 9002).

    ```bash
    docker run --name tour-of-heroes-api-v3 -p 9002:5000 -d tour-of-heroes-api:v3
    ```

27. **Access the Containerized .NET API (Version 3):**
    Verify that the application is running correctly from the container built with the multistage process.

The lesson highlights how Dockerfiles enable defining reproducible image builds and how techniques like multistage builds are essential for creating efficient images.
