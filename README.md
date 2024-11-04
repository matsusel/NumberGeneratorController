Generator reads commands from stdin, where each command is delimited by a line break, and writes responses to stdout.
Program handle following commands:

- Hi: Responds with "Hi" on stdout.
- GetRandom: Responds with a pseudo-random integer on stdout.
- Shutdown: Gracefully terminates the program.

Other commands are ignored

Controller launch Program A as a separate process.
After running generator controller checks its responds:

Send the Hi command to generator and verify the correct response.
Retrieve 100 random numbers by sending the GetRandom command to generator 100 times.
Send the Shutdown command to generator to terminate it.
Sort the list of retrieved random numbers and print the sorted list to the console.
Calculate and print the average and median of the numbers.

