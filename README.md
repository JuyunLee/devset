# lazy_linuxer
My toolkit    

## scp_helper  
If you are bothered with type scp command  
1. Give execute permission to installer
2. Run

Then,  
scp [file] [host]@[ip]:[filename] --> scp_helper upload [file]  
scp [host]@[ip]:[file] [filename] --> scp_helper download [file]  

## traffic_test.py
Send web requests with multiprocess to test traffic of your site  
*don't use this to attack website without agreement  
*issue : it dies when the request number is larger than 500. But I will not fix it until next usage.
