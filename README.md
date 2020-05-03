The repository contains the following projects:

## Spammer checker

A Python 3.6 program which checks whether a list of hosts are spammers by searching [Spamhaus'](https://www.spamhaus.org/) blacklist.

### Running the program
The source, which can be found [here](https://github.com/StiliyanDr/network-programming/tree/master/spammer-check), needs to be placed as is in a single directory.  
Then, the program can be started with the Python interpreter. An example of starting the program from the directory where the source is stored is:  
$ *python spammer_check.py*

### Command line arguments
If no arguments are passed to the program, as in the above example, it checks whether the machine on which it is running is a spammer.  
  
Any list of IPv4 addresses can be passed to the program and each of them will be checked. What follows is an example of checking whether **114.231.105.37** and **222.109.135.16** are spammers:  
$ *python spammer_check.py "114.231.105.37" "222.109.135.16"*

### Signalling invalid addresses
In case some of the arguments are invalid, no checking is done. Instead, the invalid addresses and their corresponding positions in the command line are shown in an error message.  An example is:  
*$ python spammer_check.py "256.256.350.100" "114.231.105.37"*  
Invalid addresses found! The addresses and their positions are [('256.256.350.100', 1)].  
