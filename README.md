# Installation

* Clone the `cidrchk` git repository
* `sudo python setup.py install`

If you are unable to install `cidrchk` as root, please use the following notation instead:

* `python setup.py install --user`

# What is cidrchk?

`cidrchk` is a simple Python script with only one purpose: To inform a user whether or not their computer is connected to a particular network. For example, on your "work" laptop, you depend on autofs to automatically mount NFS directories. However, when you are off-site or not connected to your institution's VPN, you quickly realize attempting to access these data areas will cause significantly long delays (i.e. the *five minute* default timeout period)

# Options

```
usage: cidrchk [-h] [--ignore IGNORE] [--debug] [--verbose] cidr [cidr ...]

Detects whether or not any ethernet devices match to a defined CIDR range.

positional arguments:
  cidr                  IP range(s) to detect

optional arguments:
  -h, --help            show this help message and exit
  --ignore IGNORE, -i IGNORE
                        IP range(s) to ignore (Default: link-local and
                        localhost)
  --debug, -d
  --verbose, -v
```

# How do I use it?

Consider the following **.cshrc** example:

```
setenv PATH $HOME/bin:${PATH}
setenv MYDATA /remote/data1
alias badidea "cd ${MYDATA}"
```

What happens if you, out of habit, attempt to execute your favorite alias?

```
$ badidea
[ no output, waiting for autofs to timeout ]
```

Whoops! Things didn't go as planned, so let's take a look at the same **.cshrc** example using `cidrchk`:

```
setenv PATH $HOME/bin:${PATH}
setenv MYDATA /remote/data1

set _OFFSITE = `cidrchk 10.0.0.0/20 66.55.32.0/20 >/dev/null`
setenv OFFSITE $status
unset _OFFSITE

alias badidea "cd ${MYDATA}"

if ( ${OFFSITE} ) then
    unalias badidea
endif
```

In the above example the following is *true*: 

If 10.0.0.0/20 represents your institution's VPN address space and 66.55.32.0/20 represents your company's local intranet, and your home IP was 192.168.1.101, `cidrchk` returned a non-zero value indicating your computer was "off-site".

Inversely, if your computer's IP address was 66.55.45.10 (i.e. you are in your cubicle), `cidrchk` would return zero indicating your computer was "on-site".

## Other Possiblities

Issuing `-v` to `cidrchk` will echo the return value to the console, resulting in slightly more cleaner code:

```
setenv OFFSITE `cidrchk -v 10.0.0.0/24 66.55.32.0/20`

if ( ${OFFSITE} ) then
    # do something clever to prevent personal hardship
endif
```

## How do I use BASH with cidrchk?

The notation required for `cidrchk` to use BASH is nearly identical to TCSH:

```
_OFFSITE=$(cidrchk 10.0.0.0/24 66.55.32.0/20 >/dev/null)
export OFFSITE=$?

if (( ${OFFSITE} )); then
    #do something clever to prevent personal hardship
fi
```

# Bug Reporting

Submit bug reports via this project's issue tracker: https://bitbucket.org/jhunkeler/cidrchk/issues

Please remember to include your computer's operating system, the name of the shell you executed `cidrchk` from, the output of `cidrchk -d`, and any relevant code snippets you may have.

