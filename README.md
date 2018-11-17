Environment: Linux

In order to run the program, input the following in the terminal:

python3.6 solution.py


then feed the input.

For timestamp in input, according to the spec, I assume it is iso 8601 format.


If the input is price update, it will output nothing.

If the input is exchange rate requests, it will output the desired result followed by the spec, but there are following possible situations:

1) The source exchange, source currency, destination exchange, destionation currency are all in the Graph, then it output the desired path.

2) Among source exchange, source currency, destination exchange, destionation currency, any of them is not in the graph, it output:
Unknown currency, continue...


If you want to quit the program, press: ctrl + c, otherwise, the program will run forever, which means you can feed the inputs all the time.


I did something simple for sanity check:
1) if the input is empty, continue
2) If the input is invalid, which means the input is not the price update and the input is not exchange rate requests, output error and continue
