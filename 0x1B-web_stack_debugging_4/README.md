# Debugging website to figure out why some reguest are fialling
In this case, 2000 requests were made to the server with 100 requests at a time. 943 requests failed, had to fix the stack to get to 0 fails

## Problem
Encountered a "too many files open" error in the Nginx server logs. This error indicates that the server has reached its limit on the number of open files, causing it to fail in handling additional requests.
 
## Solution
After debugging the issue, I found that increasing the ULIMIT resolved the problem. ULIMIT is a system resource limit that specifies the maximum number of open files a process can have. By increasing this limit, you allow Nginx to handle more simultaneous connections and avoid running into the "too many files open" error.

## Steps to Increase ULIMIT
To increase the ULIMIT on your system, follow these steps:

1. **Identify the Current ULIMIT**: Check the current ULIMIT value to understand the current limit on open files.

2. **Modify ULIMIT Configuration**: Modify the system-wide ULIMIT configuration to increase the maximum number of open files allowed by the operating system.

3. **Apply Changes**: Apply the changes to the ULIMIT configuration to take effect.

4. **Restart Nginx**: After increasing the ULIMIT, restart the Nginx server to apply the changes.