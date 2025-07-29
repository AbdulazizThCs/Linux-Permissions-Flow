# Linux-Permissions-Flow
Explains Linux file permissions with Python example .  

## Repository Idea

This repository is created to help beginners understand **Linux file permissions** in a clear and engaging way.  
It demonstrates how to:  
- Read file permissions
- Understand each part (`owner`, `group`, `others`)
- Apply real changes using the `chmod` command
- See it in action through a Python file

## User Types and Access Levels  

**Owner** → The person who created the file and usually has full control over it.  
Example: `rwx------` → owner can read, write, and execute.

**Group** → A set of users who belong to the same group as the owner.
Example: `---rwx---` → group members can read, write, and execute.

**Others** → All other users on the system who are not the owner or in the group.
Example: `------r-x` → others can read and execute, but not write.

