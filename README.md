Generator reads commands from stdin, where each command is delimited by a line break, and writes responses to stdout.
The program supports the following commands:

- Hi: Responds with "Hi" on stdout.
- GetRandom: Responds with a pseudo-random integer on stdout.
- Shutdown: Gracefully terminates the program.
- *Other commands are ignored*

Controller launch generator as a separate process.
After starting the generator, the controller checks its responds:

- Send the Hi command to generator and check the correctness of the answers..
- Retrieve 100 random numbers by sending the GetRandom command to generator 100 times.
- Send a Shutdown command to generator to terminate it.
- Sort the list of retrieved random numbers and print the sorted list to the console.
- Calculate and print the average and median of the numbers.

