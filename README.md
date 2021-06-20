# other_access

other_access is more flexible implementation of os.access() which can check access for other users. 

For example, root user can use `other_access.other_access(path, 'www-data')` to ensure files are readable by www-data user.

## Limitation
otheraccess does not supports filesystem ACL

## Examples

