using System;

class HelloWorld
{
    static void Main()
    {
        Console.WriteLine("Hello World");
    }
}
 
# Test and validation commands
csc HelloWorld.cs
$output = & .\HelloWorld.exe
echo $output

# Validation:
# - File exists: HelloWorld.cs
# - When run, prints "Hello World"
# This meets acceptance criteria.