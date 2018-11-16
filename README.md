Environment: Linux

In order to run the program, input the following in the terminal:

python3.6 solution.py


then feed the input.

If the input is price update, it will output nothing.

If the input is exchange rate requests, it will output the desired result followed by the spec, but there are following possible situations:

1) The source exchange, source currency, destination exchange, destionation currency are all in the Graph, then it output the desired path.

2) Among source exchange, source currency, destination exchange, destionation currency, any of them is not in the graph, it output:
Unknown currency, continue...


If you want to quit the program, press: ctrl + c, otherwise, the program will run forever, which means you can feed the inputs all the time.


