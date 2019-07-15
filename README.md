# python_test_japan

Please find below instruction to run the application :

Prerequisites :
 1) Python version 3.0 or above (python should be installed with package "requests")
 2) Mysql 5.0 or above  
 3) Application setup method 
    
	i) Download the folder (python_test_japan) from url and copy to /var/www/html folder in your linux server.
        
		https://github.com/jitendragamit/python_test_japan
		
		OR 
	
	ii) use git clone command to donwload files
	 git clone https://github.com/jitendragamit/python_test_japan.git

    iii) Import given mysql script file(db_python_test.sql)into mysql database (db_python_test).
     db_python_test database should be created in your mysql   
 
 4) run below script from command line as below instruction 
    i) Go into /var/www/html/your_folder_name then 
	   # python client_call_api.py 

      then it will be prompt to ask the Mac address, please type Mac address name 
	  and then press enter, It will be returned the Company name.
	
	 
 


