# 0x05. Processes and signals

## Resources:books:
Read or watch:
* [Bash CheatSheets](https://devhints.io/bash)
* [Linux PID](http://www.linfo.org/pid.html)
* [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
* [Linux signal](https://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/)
* [How to find the process id in Linux](https://www.youtube.com/watch?v=_5vBubyo1Hs)
* [ps - command in linux](https://linuxize.com/post/ps-command-in-linux/)
* [pgrep](https://linuxize.com/post/pgrep-command-in-linux/)
* [Intorduction to Unix commands - Kill](https://kb.iu.edu/d/afsk#kill)
* [How to soft kill GUI-applications via terminal?](https://unix.stackexchange.com/questions/19474/how-to-soft-kill-gui-applications-via-terminal/19475#19475)
* [Kill signal](https://linux.die.net/Bash-Beginners-Guide/sect_12_01.html)
* [Job control - kill signal](http://linuxcommand.org/lc3_lts0100.php)
* [Errors and Signals](http://linuxcommand.org/lc3_wss0150.php)
* [pkill](https://www.howtoforge.com/linux-pkill-command/)
* [Read "Traps" pag 453 - The Linux Command Line A Complete Introduction by William E. Shotts](https://books.google.com.co/books?id=ZBKsMYz1Q4kC&pg=PA426&lpg=PA426&dq=In+Chapter+10,+we+saw+how+programs+can+respond+to+signals.+We+can+add+this+capability+to+our+scripts,+too.+While+the+scripts+we+have+written+so+far+have+not+needed+this+capability&source=bl&ots=fLwBYGgSSV&sig=ACfU3U2FDEYQFPPeuDyWxhIJFOwPOdD5KA&hl=en&sa=X&ved=2ahUKEwjT_9X3vJbqAhXCSt8KHfScAOIQ6AEwAHoECAkQAQ#v=onepage&q=In%20Chapter%2010%2C%20we%20saw%20how%20programs%20can%20respond%20to%20signals.%20We%20can%20add%20this%20capability%20to%20our%20scripts%2C%20too.%20While%20the%20scripts%20we%20have%20written%20so%20far%20have%20not%20needed%20this%20capability&f=false)
* [kill -9: kills a process with Kill signal](https://linux.die.net/Bash-Beginners-Guide/sect_12_01.html)
* [Create a file in bash scripting](https://www.cyberciti.biz/faq/create-a-file-in-linux-using-the-bash-shell-terminal/)
* [Read command line](https://www.computerhope.com/unix/bash/read.htm)
* [Zombie](https://zombieprocess.wordpress.com/what-is-a-zombie-process/)
* [Ampersands & on the command line](https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html)
* [Get To Know Linux: The /etc/init.d ](https://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/)
* [Daemon (computing)](https://en.wikipedia.org/wiki/Daemon_%28computing%29)
* [Positional Parameters](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html)

---
## Learning Objectives:bulb:
What did I learn from this project:

* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

---

### [0. What is my PID](./0-what-is-my-pid)
* Write a Bash script that displays its own PID.


### [1. List your processes](./1-list_your_processes)
* Write a Bash script that displays a list of currently running processes.


### [2. Show your Bash PID](./2-show_your_bash_pid)
* Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.


### [3. Show your Bash PID made easy](./3-show_your_bash_pid_made_easy)
* Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.


### [4. To infinity and beyond](./4-to_infinity_and_beyond)
* Write a Bash script that displays To infinity and beyond indefinitely.


### [5. Kill me now](./5-kill_me_now)
* We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.


### [6. Kill me now made easy](./6-kill_me_now_made_easy)
* Write a Bash script that kills 4-to_infinity_and_beyond process.


### [7. Highlander](./7-highlander)
* Write a Bash script that displays: To infinity and beyond indefinitely, With a sleep 2 in between each iteration


### [8. Beheaded process](./8-beheaded_process)
* Write a Bash script that kills the process 7-highlander.


### [9. Process and PID file](./100-process_and_pid_file)
* Write a Bash script that: Creates the file /var/run/holbertonscript.pid containing its PID


### [10. Manage my process](./101-manage_my_process)
* Write a manage_my_process Bash script


### [11. Zombie](./102-zombie.c)
* Write a C program that creates 5 zombie processes.


### [12. Screencast](./103-screencast_unix_signal)
* Now that you have mastered signals, how about sharing your knowledge?

---

## Author

* [GitHub - Julian Franco Rua](https://github.com/julianfrancor)

* [LinkedIn - Julian Franco Rua](https://www.linkedin.com/in/julianfrancor/)