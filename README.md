# revolut-challenge
My code to Revolut Python Engineer Data Challenge

### Installation
1) Clone the repo to your local machine
2) Create a virtual environment with python 3.6 or higher and install the dependencies listed on requirements.txt by running:

    pip install -r requirements.txt

### Usage
#### CLI

    cat <filename> | python nest.py nesting_level_1 nesting_level_2 ... nesting_level_n
    
#### API
The API version runs over Flask RESTful. The virtual env must be activated before posting to API.

First, move to the folder where the virtual env python version is installed, then run:

    source bin/activate
    
   Then from the root folder from the API, run:
    
    flask run
    
Now, the API can be accessed by **curl**:

    curl -X GET http://localhost:5000/nest -d file=input.json -dlevel=country -d level=city --user revolut:YouWillNeverFindOut
    
NOTE:
**-d file**: specify the name of the input file
**-d level**: specify the nesting levels to be considered in order
**\-\-user**: basic authenticantion method
