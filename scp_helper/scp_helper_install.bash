#!/usr/bin/bash
if [ $# -ne 2 ]; then
	echo -e "\nUsage: $0 <user> <ip>"
	echo "Please run this with root privilege\n"
	exit -1
elif [ "$USER" = "root" ]; then
		echo -e "#!/usr/bin/bash\n if [ \$# -ne 2 ]; then\n\techo \"Usage: \$0 <upload or download> <file>\"\n\texit -1\nfi\nIFS=\"/\" read -r -a array <<< \"\$2\"\nif [ \"\$1\" = \"upload\" ]; then\n\tscp \$2 $1@$2:/home/$1/\${array[@]: -1:1}\nelif [ \"\$1\" = \"download\" ]; then\n\tscp $1@$2:\$2  ./\${array[@]: -1:1}\nelse\n\techo \"Usage \$0 <upload or download> <file>\"\n\texit -1\nfi" > /usr/bin/scp_helper
		chmod +x /usr/bin/scp_helper
		echo -e "\nscp_helper installed.\nDon't forget to gain access permission to your ssh server\n"
else
	echo -e "\nPlease run this with root privilege\n"
	exit -1
fi
