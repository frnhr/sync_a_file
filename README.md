sync_a_file
===========

A setup to keep a remote directory in sync as local directory changes.

Works with large directories thanks to [fswatch](https://github.com/emcrisostomo/fswatch).

Directory structure:

    /somewhere/
             |/local/  <-- local directory here
             |/remote/ <-- empty directory, a mounting point
             |/sync_a_file.py
             |/remote_mount.sh
             |/remote_unmount.sh
             |/remote_watch.sh
             
Usage:

    $ cd /somewhere
    $ ./remote_mount.sh
    $ ./remote_watch.sh
    
    
## ssh_config?

A snippet from ~/.ssh/config file. It enables multiplexing of ssh connections. The effect is that user gets asked for login info only once and subsequent connection will use the established master (a.k.a. ssh socket) connection instead of opening a new one.

Usage:

    local$ ssh example_com_master
    ... login as usual ...
    remote$
    
    from another terminal or another piece of software:
    
    local$ ssh my.example.com
    remote$
    
    (no credentials prompt! because using already established connection)
    
Gotchas:

Only single connection can trancfer data at a time, other conections will wait (block).

The master connection has to be opened first. Any conenctions to `my.example.com` that are opened before the master connection will behave as usual, i.e. prompt for credentials and open a stand-alone ssh connection.


    

