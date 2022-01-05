# Python_pickle_rce_patch
--------------------------------------------------------------------------------------------------------------------------------------------------------------------


I came across a challenge where i had to exploit and mitigate the python pickle serialization and was given 2 python files that i have shared in unpatched_code folder.

On searching on internet i came accross a wonderful article. The link is - https://versprite.com/blog/application-security/into-the-jar-jsonpickle-exploitation/

I will explain in brief, how the pickle can be exploited.

## POC ##

python pcikle doc contained a function __reduce__(), which helped in exploiting the serialization.
__reduce__ function take two items, first item in a tuple that contians the argumetns and second contains the callable. Meanins using argument you can call the callable. For example - let argument be os.system (first item) and and callable be whoami (second item). This the python system.os will call the whoami command on linux .

![Screenshot_2022-01-05_15-08-25](https://user-images.githubusercontent.com/53575624/148196632-e0efca31-35b0-4c5a-97e0-658f6f0d5ce7.jpg)

and the content of json file that was produced by exploit.py is


![Screenshot_2022-01-05_15-16-50](https://user-images.githubusercontent.com/53575624/148196791-dee78026-a9a9-4417-a721-8af4546df9c1.png)

and this json file is used by server.py which will execute the command 


![Screenshot_2022-01-05_15-07-52](https://user-images.githubusercontent.com/53575624/148196281-bd6bb759-0a93-43f9-b8d6-520c2f282de3.jpg)

## Threats ##
This is serious issue and can lead Local File Inclusion and Remote Code Exectuion attacks.

## Mitigation ##

On little googling how to prevent this attack, a solution came was to use HMAC (Hash Message Authentication Code)

HMAC is cryptography technique which is used to proof authenticity between messenger and sender.
HMAC is a big topic, so i will cover it other time.It just help in maitaining the authenticity of message.

I have written the patch code in patch_code foler. A same secret key is used by both client and sever which is used for encryption and decryption. To use, just add the secret key known to both client and server, and if third party chnages the content of message, then secret key and hash send will be used to check authenticity of message.

![Screenshot_2022-01-05_16-03-40](https://user-images.githubusercontent.com/53575624/148205136-2f4f84ef-ec22-4f85-9e75-c23c1a5fc064.jpg)
