#include <stdio.h>
#include <iostream>

int main(int argc, char **argv)
{
    std::string commands = "python main.py ";
    for(int i = 0; i < argc; i++)
    {
        if(i == 0)
            i += 1;
        commands += argv[i];
        commands += " ";
    }
    system(commands.c_str());
}