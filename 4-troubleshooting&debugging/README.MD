#TROUBLESHOOT AND DEBUG: ##COURSE 4 OF IT *Google IT Automation with Python Professional Certificate*

# **First week**
# Steps To Troubleshoot
> 1-Gather information
> 2-Find the Root Cause
> 3-Performe The Necessary Remediation :both => *long*|*short* Term

# Intermittent Issues
> werner heisenberg heisenbug :observer effect => observing the phenomenon alters the phenomenon  
> issues with bad ram allocation 
> net conx wasn't initiated in gd way

# Binary Searching
> binary search is search dichotomic
> Bisecting dividing the list of elements into 2halfs so you can check each till you get to the bottom of error

# **Second week**
# Slowness
> identify the bottleneck slowness
> ab -n 500 site.com  => check website response time for 500requests |apache benchmark unix tool
*how to optimise code execution*
>-store already calculated data
>-use right data structure
>-make sure pgm keep working while I/O or other interactions
>profiler => tools to measure the ressources our program uses

> **data structures:**
                        java        c++             ruby        go
> list :                arraylist   vector          array       slice >manipulate at end 
> dictionaries :        hashmap     unorderedmap    hash        map 

#slow script times:

>**time =>give 3 times :**
>time ./script.py => will give 3times:
> real : actual time amount (wall clock time)
> user : time spent doing the ops in the user space 
> sys  : time spent doing  sys-level ops
>-real => wall-clock time | how much time prgm takes no-matter what computer is doing (wont necessary be adding user+sys)
>---------------------------------------------------------------
>**profiler tool :measure ressources that our pgm is using **
> **modules like:**
>cprofile =>to analyze python prgm     
>gprof =>to analyze c program
>pprofile => pprofile3 -f callgrid -p profile.out >
>kcachegrind  => to see the time spend by prgm and its func calls with a gui interface

> **parallelisme :**
##services:
> memcached :>chaching service dynamic one
> varnish => caching service

##threads & processes:
> threading or asyncIO in python
> executor :the process in charge of distributing the work among workers
> from concurrent import futures => futures submodule provide many executors :-using thread|processes

# **Third week**

> System logs => in /var/log/sys.log |event viewer on windows or process monitor
> User logs => in  .xsessions-errors file 
**debugging app crashing**
>see the available logs & figure out what changes
>trace the sys|library calls the pgm makes
>create the smallest reproduction cases 

**fixings**:
## basic steps to diagnostic app crash:
>-what were you trying to do
>-what steps did you follow
>-what did you expect to happen
>-what was the actual output
>--------------------------------------------------------------------------------------------------
> wrappper =>pgrm that sets in between two apps to give assistance or changing of data from one to other.
> watchdog =>process periodically check status of program and start it when its off

**code that crash**
>debugging symbols =>
A debug symbol is a special kind of symbol that attaches additional information to the symbol table of an object file, such as a shared library or an executable. This information allows a symbolic debugger to gain access to information from the source code of the binary, such as the names of identifiers, including variables and routines.

> PBD file is used to generate debugging symbols using Microsoft compilers
> printf debugging => display infos from code by printing
> core file => store all info about the app crash
> **gdb debugger:**
> backtrace =>shows lines of different functions that being executed when problem happened
> -up =>move to the calling func in backtrace 
> -list =>shows lines around the current line
> -print => print var

> **pdb3 debugger:**
> -pdb3 script args
> -next => run the debugger linebyline
> -continue => run exec till finish|crash
> -bom byte-order-mak => used in utf-16 tell diff-betwn little-&-big-indian

**working details:**
>communication lead =>the one in charge to communicate and give updates to users ,making shield for devs to work
>incident controller =>the one who
>*postmortem :* =>documents describ details of incidents that helps us learn more from our mistakes doit like this:
> -what caused the issue
> -what was the impact of the issue
> -how it was diagnosed
> -Short-term remediation u applied
> -Long-term remediation u recommend

# **Fourth week**
# Memory Leaks and How to Prevent Them
# Disk Leaks and How to detect them
# Network staturation and how to find them
> traffic shaping => marking data packets with different priorities to prevent congestion
> -by huge chunks of data     
> ```sh thecodebuzz@DESKTOP-NUEMRRD:~$ od-cx /dev/urandom 
> ```
> top cmd details:
>-VIRT => list virtual memory allocated for each process.
>-RES => dynamic memory preserved for specific process.
>-SHR => mem shared accros prcesses.

# Managing Our Time
**Getting to the Important Tasks**
>the Eisenhower Decision Matrix =>split tasks to urgent and important
>technical depts => when short term solutions deployed ,and the prblm not really solved

**Managing our futures Lives**
>-Rubber duck debugging =>explaining the problem to rubber duck
>-Proactive Practices
>-deploy software in phases or canaries =>means upgrade set of computers,and not all so 
> we don't break the system as all
> centrelized logs collections
> playbooks => docs to detail what a person on call can do diagnose and mitigate a  prblm

**planing future ressources usage**

>Problem Domains just describe the complexity of a given problem that one is trying to solve. Let’s look at an example below:
>Failure Domains


# Debugging tools

>strace => show sys-calls that a prgm made during exec
>ltrace =>
>lsof => shows open files in system
> -strace -o execution.strace ./prgm.py
>iostat => show stats on in/out of mem ops
>vmstat => show stats on virtual mem ops
>ionice =>  make the system changes his priority to allow other app(here webserver ) access it
>iotop => for read/write soft
>iftop => debug network  issue congestion,shows how much data each active cnx is sending
>trickle => to limite the bandwith 
>nice => start process with different priority
>renice => renice(newpriority,pid) | change priority of cpu already running
>locate file =>to find a specific file
>daemonize => run a program seperatly as it were a daemon
>zenity =>the app shows gui date chooser
>pidof => show process priority
>locate => locate static/001.webm | helps to find a 
> grep ffmpeg * => this shows if any file here made a call to ffmpeg
> killall -STOP name-of-prgm  => send sigStop to processes but does not kill | then send " -CONT "
> killal -stop pgm => gives true if sucess
> kCachgrind => shows 
>rsync =>usual used for backing_up data >it should include -bwlimit to apply limitbandwidth
>memtest-86 => check mem health ran on boot
>ls -lt =>order last modified date
>netstat -nlp =>  n:print numeric addresses ,l:only sockets that are listening for a cnx,
> -p to print the process ID and name to which each socket belong
>Dr memory(win) |valgrin =>tells us if the program is doing any invalid operations no matter it crashes or not
>unlimited -c unlimited => allow core files of any size
>gdb -c core scriptname => to debug the core file of the scriptname
>memory_profiler => from the profiler module ,we use it inside python script with decorators







# Ressources:

>https://docs.microsoft.com/en-us/sysinternals/downloads/procmon 
>http://www.brendangregg.com/linuxperf.html
>http://brendangregg.com/usemethod.html

    #Performance Monitor on Windows:
>https://www.windowscentral.com/how-use-performance-monitor-windows-10
>https://www.digitalcitizen.life/how-use-resource-monitor-windows-7
>https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer
>https://en.wikipedia.org/wiki/Cache_(computing)
>https://www.reddit.com/r/linux/comments/d7hx2c/why_nice_levels_are_a_placebo_and_have_been_for_a/
    #profiling
>https://en.wikipedia.org/wiki/Profiling_(computer_programming)

    #parallelism and concurrency:
>https://realpython.com/python-concurrency/
>https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32
    #Understanding Crashes:
>https://www.digitalmastersmag.com/magazine/tip-of-the-day-how-to-find-crash-logs-on-windows-10/
>https://www.fosslinux.com/8984/how-to-check-system-logs-on-linux-complete-usage-guide.htm
>https://docs.microsoft.com/en-us/sysinternals/downloads/procmon
>https://www.howtoforge.com/linux-strace-command/
    #Debugging crashes
>https://realpython.com/python-concurrency/
>https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32
>https://stackoverflow.com/questions/33047452/definitive-list-of-common-reasons-for-segmentation-faults
>https://sites.google.com/a/case.edu/hpcc/home/important-notes-for-new-users/debugging-segmentation-faults

>##readable code on github 
>https://github.com/fogleman/Minecraft
>https://github.com/cherrypy/cherrypy
>https://github.com/pallets/flask
>https://github.com/tornadoweb/tornado
>https://github.com/gleitz/howdoi
>https://github.com/bottlepy/bottle/blob/master/bottle.py
>https://github.com/sqlalchemy/sqlalchemy

>##Managing Computer Ressources
>https://realpython.com/python-concurrency/
>https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32
>https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python
>https://www.linuxjournal.com/content/troubleshooting-network-problems
>https://blog.rescuetime.com/how-to-prioritize/
>https://simpleprogrammer.com/understanding-the-problem-domain-is-the-hardest-part-of-programming/
>https://blog.turbonomic.com/blog/on-technology/thinking-like-an-architect-understanding-failure-domains
>https://landing.google.com/sre/sre-book/chapters/effective-troubleshooting/