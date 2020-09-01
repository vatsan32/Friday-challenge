# Friday code challenge
## Description
An address provider returns addresses only with concatenated street names and numbers. Our own system on the other hand has separate fields for street name and street number. So the basic idea is to separate the street names and house numbers into separate entities and write them in a JSON file. 

**Input**: string of address, some examples are:

Simple cases
- `"Winterallee 3" -> {"street": "Winterallee", "housenumber": "3"}`
- `"Musterstrasse 45" -> {"street": "Musterstrasse", "housenumber": "45"}`
- `"Blaufeldweg 123B" -> {"street": "Blaufeldweg", "housenumber": "123B"}`

Consider more complicated cases

- `"Am Bächle 23" -> {"street": "Am Bächle", "housenumber": "23"}`
- `"Auf der Vogelwiese 23 b" -> {"street": "Auf der Vogelwiese", "housenumber": "23 b"}`

Consider other countries (complex cases)

- `"4, rue de la revolution" -> {"street": "rue de la revolution", "housenumber": "4"}`
- `"200 Broadway Av" -> {"street": "Broadway Av", "housenumber": "200"}`
- `"Calle Aduana, 29" -> {"street": "Calle Aduana", "housenumber": "29"}`
- `"Calle 39 No 1540" -> {"street": "Calle 39", "housenumber": "No 1540"}`

**Output**: string of street and string of house number as JSON object

Example: 

`{"street": "Winterallee", "housenumber": "3"}`
`{"street": "Musterstrasse", "housenumber": "45"}`


## Methodology  
We will be using the Python's in-built RegEx `re` module (`import re`) to complete the task. Basically we are looking to find common patterns that exist in street names and house numbers, which can then be used to create a RegEx expression. We can then compile the expression and search the input string for the street address and house numbers separately. 
An additional case is also shown, wherein, if no housenumber is provided, the program prints out `NO HOUSE NUMBER!` as the output in the housenumber variable in the JSON file. 

## How to run
python Friday.py --> which will prompt the user to enter the path of the filename with all the street names and housenumbers. 

`Enter the path of your file: [ENTER THE PATH OF THE FILE NAME HERE]`

## Example files
I have created two `.txt` files. File `/input_output/Friday_examples.txt` contains all the examples of street names and house numbers given in the default challenge. The second file `/input_output/my_own_examples.txt` has few street names and house numbers apart from the above default examples. There is also one example without a street number. 

## Required modules
All the modules used in this examples are Python built-in modules. 

`import re`

`import json`

`import os`


No external module is needed for this code to work. 
