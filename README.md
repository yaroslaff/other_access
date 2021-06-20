# other_access

other_access is more flexible implementation of [os.access()](https://docs.python.org/3/library/os.html#os.access) which can check access for other users. 

For example, root user can use `other_access.other_access(path, 'www-data')` to ensure files are readable by www-data user.

## Limitation
otheraccess does not supports filesystem ACL

## Usage

`other_access(path, mode, uid, gids=None)` - main function. similar to [os.access()](https://docs.python.org/3/library/os.html#os.access), but checks for other user (`uid`) and list of groups (`gids`). User and group id's are integer (not names).

`oaccess(path, mode, user, groups)` - wrapper for other_access which takes names for user/groups, converts it to numerical uid/gids and calls other_access()


## Examples
Lets use /etc/shadow for example:
~~~
-rw-r----- 1 root shadow 1841 Jun  2 04:07 /etc/shadow
~~~

~~~python
# user root can read and write
assert(oaccess('/etc/shadow', os.R_OK | os.W_OK, 'root') == True)

# group shadow can read
assert(oaccess('/etc/shadow', os.R_OK, 'nobody', ['shadow']) == True)

# Other can check existence of file, but cannot read
assert(oaccess('/etc/shadow', os.F_OK, 'nobody') == True)
assert(oaccess('/etc/shadow', os.R_OK, 'nobody') == False)
~~~