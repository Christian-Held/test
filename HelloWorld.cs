using System;

class HelloWorld
{
    static void Main()
    {
        Console.WriteLine("Hello World");
    }
}
# Run compilation and execution test

# Compile the C# file
csc HelloWorld.cs

# Execute the program and capture output
$output = & .\HelloWorld.exe

# Print output for validation
echo $output
# Validation:
# - File exists: HelloWorld.cs
# - When run, prints "Hello World"
# This meets acceptance criteria.