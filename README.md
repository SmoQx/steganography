<div align="center">
    <h1>Simple Web Steganograph</h1>
</div>


![](/screenshots/sc1.png)
![](/screenshots/sc2_with_email.png)
![](/screenshots/sc3_after_encoding.png)

## Contents ##
1. [Details](#details)
2. [Dependencies](#dependencies)
3. [Documentation](/doc/doc.pdf)


<a name="details"></a>
## Details ##
The application supports most graphic file formats however, the encoded file is in .png format.  
The application utilizes the Caesar cipher as the algorithm for encrypting data.  
The encrypted data is saved in the least significant bit at the beginning of the image.  
To find the end of the text for decryption, a marker is used, in the form of a single byte composed of all zeros.  
After saving the file can be sent via email.  
Email configuration is saved in email.cfg.  
Default server is set to gmail and the password to the plications must be creted in gmail's (https://myaccount.google.com/signinoptions/passkeys) 


<a name="dependencies"></a>
## Dependencies ##
Used libraries
1. PIL
2. pathlib
3. flask
4. os
5. werkzeug
