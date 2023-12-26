<div align="center">
    <h1>Simple Web Steganograph</h1>
</div>


![](/screenshots/sc1.png)
![](/screenshots/sc2_with_email.png)
![](/screenshots/sc3_after_encoding.png)

## Contents ##
1. [Details](#details)
2. [Dependencies](#dependencies)
3. [How to use](#how_to_use)


<a name="details"></a>
## Details ##
The application supports most graphic file formats however, the encoded file is in .png format.  
The application utilizes the Caesar cipher as the algorithm for encrypting data.  
The encrypted data is saved in the least significant bit at the beginning of the image.  
To find the end of the text for decryption, a marker is used, in the form of a single byte composed of all zeros.  
After saving the file can be sent via email.  
Email configuration is saved in email.cfg.  
Default server is set to gmail. Password to the application must be created in gmail's (https://myaccount.google.com/signinoptions/passkeys) 


<a name="dependencies"></a>
## Dependencies ##
Used libraries
1. PIL
2. pathlib
3. flask
4. os
5. werkzeug


<a name="how_to_use"></a>
## How to use ##

<h3>Encode</h3>

If you want to insert text in to a photo u need to select a file from then you need to
input a password with which the shift of a caesar cypher is generated. Then you can write or drag txt file in to text box 
below text to encrypt. Encoding is done by changing the text to binary data and saved with a marker to the least significant bit of a pixel.
After upload button is pressed the link to a file is generated and deleted from downloads folder.

<h3>Decode</h3>

To decode the file u need to upload a file and select the decode button type in the password to decode it.
It takes the least significant bit transforms all the pixels in to binary data splits it in to byts then saves it as 
a characters until marker is found. Then the decoded text is displayed in to second page.

<h3>Email</h3>

To send encoded file via email. Email.cfg file must be configured. 
After that u can select email button and fill the box and attach the file and pres send email button.
