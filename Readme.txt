Name:-	 Mukul M
USN:- 	1PI12IS059
Q.NO:-	 1
Q.Title:-  Calculating the net profit or loss from a .csv file containing the selling price
 		 and cost price of all the items based on either they are used or unused.

   
  The source code files that are being submitted are :-

	1)asn4.c
	2)function.py
	3)README.txt
	4)upgrade.py
	5)sequence.py
	6)digest.txt
	7)data.csv
	
  The instructions to be followed while executing the code are 
        1) compile the program using gcc asn4.c
        2) run using ./a.out -f data.csv -l logfile.txt
     
     logfile.txt is the any log file that will be created on execution.
	 
	      Version checking is being done in this assignment for upgradation. "system("python3 upgrade.py ");" 
		  is being called in main function which further reads the value in the file "digest.txt" (which has a 
          number which is the present version value) and checks if the latest upgrade version is greater than
		  the present version, if the present version number is smaller than the latest upgrade number then it 
		  needs an upgrade and changes the value in the digest.txt and there is one stage upgradation at a time.		  
	      If they are equal then there is no need and it displays "Nothing to Upgrade!".