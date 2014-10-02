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
    
