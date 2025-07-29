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
<br>  
**What does `rwx` mean?**  
**r** → read: allows viewing the file contents

**w** → write: allows editing or modifying the file

**x** → execute: allows running the file as a program  

## Numeric Permission Modes  

`000`  →  --- --- --- → No permissions for anyone  
`111`  →  --x --x --x → Execute only  
`222`  →  -w- -w- -w- → Write only  
`333`  →  -wx -wx -wx → Write and execute  
`444`  →  r-- r-- r-- → Read only  
`555`  →  r-x r-x r-x → Read and execute  
`666`  →  rw- rw- rw- → Read and write  
`777`  →  rwx rwx rwx → Full permissions for all   
<br>  
**Example**: What does `775` mean?

The number `775` **means the following**:

- **7 (Owner)** → `rwx` → Owner can read, write, and execute  
- **7 (Group)** → `rwx` → Group can also read, write, and execute  
- **5 (Others)** → `r-x` → Others can read and execute, but **cannot write**

## Example: Create and Set Permissions for a Python File  

**Step 1**: Open Linux Terminal  

**Step 2**: create and edit the file  
           `nano main.py`  → Inside the editor, write any Python code, such as: `print("Hello world")`  

**Step 3**: Save and exit the file  
            Press `Ctrl + O` → then `Enter` to save  
            Press `Ctrl + X` to exit the editor  

**Step 4**: View file permissions  
           `ls -l main.py`  

**Step 5**: Set file permissions to 775  
          `chmod 775 main.py`  

This gives:

Owner → read, write, execute

Group → read, write, execute

Others → read, execute   

**Step-by-step Screenshots** : `steps_screenshots.pdf`  

<hr>  

Created by: **Abdulaziz AL-Thomali**
           

        
