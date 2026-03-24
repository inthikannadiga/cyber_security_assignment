CAMPUSPE – CYBERSECURITY TRACK
BASH SCRIPTING AUTOMATION ASSIGNMENT

Name: Darshan M
Total Scripts Completed: 5

PROJECT OVERVIEW

This project consists of five Bash scripts developed as part of the CampusPe Cybersecurity internship track. The purpose of the assignment was to strengthen practical skills in Linux shell scripting, automation, file handling, log analysis, backup creation, and basic user account auditing.

All scripts were written and tested in a Debian-based Linux environment (Kali Linux).

FILES INCLUDED

q1_system_info.sh
q2_file_manager.sh
q3_log_analyzer.sh
q4_backup.sh
q5_user_report.sh
README.txt

HOW TO RUN THE SCRIPTS

Step 1: Make all scripts executable

chmod +x *.sh

Step 2: Run scripts individually

System Information Script
./q1_system_info.sh
Displays details such as current user, hostname, OS information, uptime, disk usage, and memory status.

File Manager Script
./q2_file_manager.sh
A menu-driven tool to create, delete, rename, search, and count files inside a directory.

Log Analyzer Script
./q3_log_analyzer.sh access.log
Analyzes a log file and extracts useful statistics.
If a non-existing file is provided, the script shows an error message.

Backup Automation Script
./q4_backup.sh
Prompts the user to enter source and destination directories and creates a timestamp-based compressed backup using tar.

User Account Report Script
./q5_user_report.sh
or
sudo ./q5_user_report.sh

Generates user account information and performs basic security checks.
Sudo access is required for password-related checks.

TESTING PERFORMED

Log analyzer was tested using a sample access log file.
Backup script was verified by creating a temporary test directory with multiple files.
File manager functions were tested individually for all available options.

LEARNING OUTCOMES

Developed structured Bash scripting skills
Implemented file and directory validation
Practiced text processing using awk, sort, uniq, and wc
Automated backup creation with timestamps
Understood how Linux stores user data in /etc/passwd
Improved overall confidence in working with the Linux terminal

DEVELOPMENT ENVIRONMENT

Operating System: Kali Linux (Debian-based)
Shell: Bash
Tools Used: nano, awk, find, tar, grep, git
