Description
-----------

Have you ever wanted to over complicate remote code execution? Me neither.  

`Server.py` will listen on a user specified port (default 8000) for HTTP GET requests with a base64 encoded cookie containing a command to run on the remote machine. It uses `subprocess.Popen` to spawn a new process, execute the command, and retrieve the results, separate from the process the server is running in before returning the results base64 encoded in the `Set-Cookie` response header.  

`Client.py` uses the `requests` module to craft an HTTP GET request with the input command base64 encoded in the cookie header. It parses the response for the `Set-Cookie` header and outputs the decoded results to the terminal. `Client.py` uses the `cmd` module to provide a command interpreter then uses the `cmdloop` method to repeatedly issue a prompt.

I was more interested in creating this to see what artifacts I could find on the victim machine (the one running server.py) to indicate there was an HTTP connection being used to transfer data to a remote attacker (me).

Example
-------
<img src="images/example.png">

Artifacts
---------
First the obvious
`netstat -antp` and `ps auxf` show the listener on port 8000 and the python process
