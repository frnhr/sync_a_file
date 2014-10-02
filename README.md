sync\_a\_file
===========

A setup to keep a remote directory in sync as local directory changes.

Works fast with large directories thanks to [fswatch](https://github.com/emcrisostomo/fswatch) - fswatch doesn't scan files but instead it "listens" to changes on the filesystem close to OS.

Works on OS X and probably on Linux as well. Would probably work on Windows too if you can get it `sshfs` to mount remote directory. If on Windows, you might want to check [WinSCP](http://winscp.net/) it provides a similar feature and thus renders this setup unnecessary.

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


# why on earth...

A few advantages over a simple sshfs mount:

 * It's faster to keep a local copy of very\_large\_directory as oposed to simply mounting it via sshfs and working on the mounted copy. For example, an IDE will want to index the project, which means downloading all the files on remote, and that takes time.
 * See when upload is done - the `sync_a_file.py` echoes the path of a file when it starts the upload, and a "." when the upload is completed, so you can know when your files are done uploading.
 * After-upload hooks - it's simple to edit `sync_a_file.py` to make it perform some additional tasks after it has finished uploading a file
 * Exclude certan files - simple regex patterns to skip uploading certan directories or file types (e.g. .pyc files, IDE project directory etc)

A few disadvantages:
 * One file at a time upload - this setup is intended to be used for uploading a few files at a time (or one at a time), it's not a massive sync-the-lot tool.


