# BlindSQLiVulnerableApp
Deliberately vulnerable (BlindSQLi ) web app
Simple Flask application. Application has the following API endpoint:
`/users/<int>`

the path parameter takes an integer user id and returns the string "FOUND " if that user details exist in the underlying database. In this case that is a MySQL database.
The above endpoint is vulnerable to SQL injection.

## Instrcutions to run the app
1. Restore the table so that the application can use it. This can be done by running the below 2 commands consecutively one after the other
`mysql -u root -p -e "create database baba";` => creates a database by the name baba
`mysql -u [user] -p baba < baba_users.sql` => restores the sql file into the baba database created above
2. Run the app as `python vulnerable.py` (the app runs on default flask port. You may need to tweak that in case you have some other app running on that port already)
3. Check/verify if the API is vulenrable to SQLinjection already
4. To exploit the vulnerability run the exploit as `python exploit.py`. The exploit is just a sample that tries to enumerate the DB username that the application uses

## Steps to verify blind SQLi in API
1.  Access the API as :
`http://127.0.0.1:5000/users/3`
and notice that the output is the string FOUND 
2. The same API when accessed with the path parameter as 6 does not give anything
`http://127.0.0.1:5000/users/6`
3. Playing with the endpoint gives the results as shown in the comments:
- `http://127.0.0.1:5000/users/3 and 1=1` => FOUND 
- `http://127.0.0.1:5000/users/3 or 1=1` => FOUND FOUND FOUND FOUND FOUND
- `http://127.0.0.1:5000/users/3 and 1=2` => << gives nothing >>

**The above tests prove that the endpoint is indeed vulnerable to SQL injection (blind boolean)**
