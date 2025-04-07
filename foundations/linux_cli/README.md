# Linux Command Line & Environment Management

## 1. Essential Commands:

**File and Directory Manipulation:**

- `ls [options] [path]`: List directory contents.

  - `ls -l`: Long listing format, showing file permissions, ownership, size, and modification time.
  - `ls -a`: List all files, including hidden files (those starting with a dot).
  - `ls -h`: Human-readable file sizes.
  - `ls -t`: Sort by modification time.
  - `ls -r`: Reverse order.

- `cd [path]`: Change directory.

  - `cd ~`: Go to the home directory.
  - `cd ..`: Go up one directory level.
  - `cd -`: Go to the previous directory.

- `pwd`: Print working directory (the current directory).
- `mkdir [options] directory_name`: Create a directory.

  - `mkdir -p path/to/nested/directory`: Create nested directories.

- `rm [options] file_or_directory`: Remove files or directories.
  - `rm file.txt`: Remove file.txt.
  - `rm -r directory`: Remove a directory and its contents recursively.
  - `rm -f file.txt`: Force removal, ignoring non-existent files and suppressing prompts.
- `cp [options] source destination`: Copy files or directories.
  - `cp file1.txt file2.txt`: Copy file1.txt to file2.txt.
  - `cp -r directory1 directory2`: Copy directory1 to directory2 recursively.
- `mv [options] source destination`: Move or rename files or directories.
  - `mv file1.txt file2.txt`: Rename file1.txt to file2.txt.
  - `mv file.txt directory/`: Move file.txt to the directory.

**Text File Manipulation:**

- `cat [file]`: Concatenate and display file contents.
- `less [file]`: View file contents page by page.
- `head [file]`: Display the first few lines of a file.
- `tail [file]`: Display the last few lines of a file.
  - `tail -f file.log`: Follow (continuously display) the contents of a log file.
- `grep [options] pattern [file]`: Search for patterns in files.
  - `grep -i "pattern" file.txt`: Case-insensitive search.
  - `grep -r "pattern" directory/`: Recursive search in a directory.
- `sed [options] 'command' [file]`: Stream editor for text manipulation.
  - `sed 's/old/new/g' file.txt`: Replace all occurrences of "old" with "new".
- `awk '[pattern] {action}' [file]`: Powerful text processing tool.
  - `awk '{print $1}' file.txt`: Print the first column of each line.

**Process Management:**

- `ps [options]`: List running processes.
  - `ps aux`: List all processes with detailed information.
  - `ps -ef | grep process_name`: find a process by name.
- `top`: Display real-time system information and process activity.
- `kill [options] PID`: Terminate a process (where PID is the process ID).
  - `kill -9 PID`: Forcefully terminate a process.
- `bg`: List background jobs; resume a suspended job in the background.
- `fg`: List background jobs; resume a suspended job in the foreground.

**Networking:**

- `ping [host]`: Check network connectivity.
- `curl [URL]`: Transfer data from or to a server.
  - `curl -O URL`: Download a file.
- `wget [URL]`: Download files from the web.
- `netstat [options]`: Display network connections and statistics.
  - `netstat -tuln`: List listening TCP and UDP ports.
- `ssh [user]@[host]`: Secure shell to connect to a remote server.
- `ifconfig or ip addr`: Display network interface information.

**System Information:**

- `uname -a`: Display system information.
- `df -h`: Display disk space usage.
- `du -sh directory/`: Display directory space usage.
- `free -h`: Display memory usage.
- `history`: Display command history.

**Other:**

- `sudo [command]`: Execute a command with superuser privileges.
- `man [command]`: Display the manual page for a command.
- `echo [string]`: Display a string.
- `find [path] [options]`: Search for files and directories.
  - `find . -name "\*.txt"`: find all files with .txt extension in the current directory.
- `tar`: used to archive and extract files.
  - `tar -czvf archive.tar.gz directory/`: create a compressed archive.
  - `tar -xzvf archive.tar.gz`: extract a compressed archive.

## 2. Permissions

**Understanding File Permissions:**

- In Linux, every file and directory has associated permissions that control who can access them.
- These permissions are divided into three categories:

  - **User (u):** The owner of the file.
  - **Group (g):** The group that owns the file.
  - **Others (o):** All other users on the system.

- For each category, there are three types of permissions:
  - **Read (r):** Allows viewing the contents of a file or listing the contents of a directory.
  - **Write (w):** Allows modifying the contents of a file or creating/deleting files within a directory.
  - **Execute (x):** Allows executing a file (if it's a script or program) or entering a directory.

**Symbolic vs. Numeric Permissions:**

- **Symbolic:**
  - Uses letters to represent permissions (r, w, x) and operators to modify them (+, -, =).
  - **Example:** `chmod u+x file.sh` (adds execute permission for the user).
- **Numeric (Octal):**
  - Uses numbers to represent permissions, where each digit corresponds to user, group, and others.
  - The numbers are calculated by adding the values: read (4), write (2), execute (1).
  - Example: `chmod 755 file.sh` (rwx for user, rx for group and others).

**`chmod` Command:**

- Used to change file and directory permissions.
- **Syntax:** `chmod [options] mode file(s)`
- **Example:**
  - `chmod 644 file.txt`: Sets read-write for the owner and read-only for group and others.
  - `chmod a+x script.sh`: Adds execute permission for all users.
  - `chmod g-w directory`: Removes write permission for the group.

**`chown` Command:**

- Used to change the owner and group of a file or directory.
- Syntax: `chown [options] user[:group] file(s)`
- Example:
  - `chown user file.txt`: Changes the owner to user.
  - `chown user:group file.txt`: Changes the owner to user and the group to group.

**Important considerations:**

- The root user can change any file permissions.
- Be careful when using the -R (recursive) option with `chmod` and `chown`.

## 3. Package Managers

**Purpose:**

- Package managers simplify the process of installing, updating, and removing software on Linux systems.
- They handle dependencies and ensure that software is installed correctly.

**`apt` (Advanced Package Tool):**

- Used on Debian-based distributions (Ubuntu, Debian, Linux Mint).
- **Essential commands:**
  - `sudo apt update`: Updates the package list.
  - `sudo apt upgrade`: Upgrades installed packages.
  - `sudo apt install package_name`: Installs a package.
  - `sudo apt remove package_name`: Removes a package.
  - `sudo apt search package_name`: Search for a package.
  - `sudo apt autoremove`: Remove unnecessary packages.

**`yum`/`dnf` (Yellowdog Updater, Modified / DNF Package Manager):**

- Used on Red Hat-based distributions (CentOS, Fedora, RHEL).
- **Essential commands:**
  - `sudo yum update / sudo dnf update`: Updates installed packages.
  - `sudo yum install package_name / sudo dnf install package_name`: Installs a package.
  - `sudo yum remove package_name / sudo dnf remove package_name`: Removes a package.
  - `sudo yum search package_name / sudo dnf search package_name`: Search for a package.

**Important considerations:**

- Always use sudo when installing or removing packages.
- Keep your package list updated.

## 4. Virtual Environments

**Purpose:**

- Virtual environments isolate Python projects and their dependencies.
- This prevents conflicts between different projects and ensures that each project has its own set of packages.

**`venv` (Virtual Environment):**

- Built into Python 3.
- **Essential commands:**
  - `python3 -m venv myenv`: Creates a virtual environment named `myenv`.
  - `source myenv/bin/activate`: Activates the virtual environment.
  - `deactivate`: Deactivates the virtual environment.
  - `pip install package_name`: Installs a package within the environment.
  - `pip freeze > requirements.txt`: Creates a list of installed packages.
  - `pip install -r requirements.txt`: Installs packages from a requirements file.

**`conda` (Anaconda/Miniconda):**

- A popular alternative to venv, especially for data science and machine learning.
- **Essential commands:**
  - `conda create -n myenv python=3.9`: Creates a virtual environment named myenv with Python 3.9.
  - `conda activate myenv`: Activates the virtual environment.
  - `conda deactivate`: Deactivates the virtual environment.
  - `conda install package_name`: Installs a package within the environment.
  - `conda env export > environment.yml`: Creates an environment file.
  - `conda env create -f environment.yml`: Creates an environment from an environment file.

**Important considerations:**

- Always activate a virtual environment before installing packages.
- Use `requirements.txt` or `environment.yml` to manage project dependencies.

> [!INFO]
>
> See [Notes](./notes.md)
