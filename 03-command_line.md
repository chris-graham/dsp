# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > - xargs: takes input from one command and tokenizes it for input into another command
- ls -R & ls -t: -R lists files in the current directory and all sub directories; ls -t lists files in order of their modified time (newest first)
- pushd / popd: pushd saves your location when you navigate to another directory; popd returns you to the last saved location
- find: searches for a given filename
- grep: searches for a string contained inside files
- touch: creates a file with the given name or updates the modify timestamp on an existing file
- sudo: executes given command as a super user
- pwd: shows your current path
- which -a: lists all instances of executables found; very handy when you can't figure out why your computer is executing the wrong version of git!
- mkdir -P: creates all intermediate directories


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > - ls: lists all unhidden files and directories in the current directory
- ls -a: lists all files and directories in the current directory (including hidden ones)
- ls -l: lists all unhidden files and directories in the current directory in long format (one per line including permissions, owner, group, size, modified date); also displays the total size of all files and directories
- ls -lh: long listing and limits the file size to 3 digits w/unit (byte, kilobyte, megabyte, etc...) in base 2
- ls -lah: long listing that includes hidden files and directories, and displays a 3 digit file size w/unit
- ls -t: sorts list by modified time (most recently modified first)
- ls -Glp: long listing that enables colorized output and writes a "/" after each directory

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > - ls -l
- ls -R
- ls -a
- ls -F
- ls -t
- I alias ll to ls -Fal on my machine, so that gets used a lot. -R and -t are new to me and seem pretty useful.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > - xargs takes input from one command and tokenizes it for input into another command
- Example: find . -name "*.py" | xargs rm -rf