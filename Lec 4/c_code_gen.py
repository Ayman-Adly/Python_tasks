import subprocess

text = input("Please Enter the text you want to configure as C++ code:")
f1 = open("g_code.cpp","w+")
output = "#include<iostream>\nint main()\n{\nstd::cout<<\""+text+"\"<<std::endl;\n}"
f1.write(output)
f1.close();
subprocess.call('g++ g_code.cpp -o APP')
subprocess.call('APP')

