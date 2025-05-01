# 🐳 Docker Installation & Setup Guide (Linux Mint / Ubuntu)

This guide documents the installation and basic setup of **Docker Engine** on a Linux system using the **APT repository** method. It includes setup for permissions, startup configuration, and common troubleshooting commands.

## Installation Methods Overview

Docker Engine can be installed in several ways:

- From Docker's official **APT repository** **(Recommended)**
- Using Docker **Desktop for Linux** (not commonly used on Mint/Ubuntu)
- Manual installation (advanced)
- Using the **convenience script** (for testing only)

## Install Docker Engine via APT (Recommended)

### 1. Set up Docker's APT repository

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl

# Create the keyrings directory and download GPG key
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

### 2. Add the Docker repository to APT sources

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```

### 3. Install Docker Engine and related components

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Verify Installation

Run the test container:

```bash
sudo docker run hello-world
```

You should see a message confirming that Docker is working.

## Post-Installation: Run Docker as a Non-Root User

To avoid using `sudo` with every Docker command:

### 1. Create the `docker` group (if it doesn’t exist)

```bash
sudo groupadd docker
```

### 2. Add your user to the group

```bash
sudo usermod -aG docker $USER
```

### 3. Apply the group changes

Option A: Log out and log back in  
Option B: Run this command:

```bash
newgrp docker
```

### 4. Test Docker again without `sudo`

```bash
docker run hello-world
```

## Enable Docker to Start on Boot

By default, Docker starts on boot for Ubuntu/Mint. If needed, you can explicitly enable or disable this behavior.

### Enable auto-start:

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

### Disable auto-start:

```bash
sudo systemctl disable docker.service
sudo systemctl disable containerd.service
```

## Useful Commands

- `systemctl status docker` - Check Docker service status
- `sudo systemctl start docker` - Start Docker manually
- `sudo systemctl stop docker` - Stop Docker
- `getent group docker` - Show users in the `docker` group
- `getent group | grep $USER` - Check what groups your user belongs to
- `docker info` - Get full Docker system information

## Notes

- Always make sure your user is in the `docker` group if you want to avoid using `sudo`.
- Adding users to `docker` group grants root-level control — only do this for trusted accounts.
- For multi-container projects, learn to use **Docker Compose** with a `docker-compose.yml` file.

## References

- [Docker Official Linux Install Guide](https://docs.docker.com/engine/install/ubuntu/)
- [Docker Post-installation Steps](https://docs.docker.com/engine/install/linux-postinstall/)
- [Docker Desktop Linux Install Guide](https://docs.docker.com/desktop/setup/install/linux/)
