Have you ever wanted to over complicate remote code execution? Now you can. 

`Server.py` will listen on a user specified port (default 8000) for HTTP GET requests with a base64 encoded cookie containing a command to run on the remote machine. It uses `subprocess.Popen` to spawn a new process, execute the command, and retrieve the results, separate from the process the server is running in before returning the results base64 encoded in the `Set-Cookie` response header.  

`Client.py` uses the `requests` module to craft an HTTP GET request with the input command base64 encoded in the cookie header. It parses the response for the `Set-Cookie` header and outputs the decoded results to the terminal. `Client.py` uses the `cmd` module to provide a command interpreter then uses the `cmdloop `method to repeatedly issue a prompt.
