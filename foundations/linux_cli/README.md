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

## 3. Package Managers

## 4. Virtual Environments

See [Notes](./notes.md)
