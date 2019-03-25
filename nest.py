## Revolut Python Engineer Data Challenge
##
## Author: Sérgio Mafra <sergio@mafra.io>
## Coded Date: 2019-03-24
## Editor: Vim
##

import argparse
import json
import sys


class Nest:
    ''' Collects input from stdin '''

    def __init__(self):
        ''' Initial state variables '''

        self.input_data = {}

    def _read_input_stdin(self):
        ''' Read input information from stdin '''

        ## Reading input from stdin
        input_text = ''
        for line in sys.stdin.readlines():
            input_text += line

        ## Loading string as JSON
        ## Saving in on input_json
        self.input_data = json.loads(input_text)

    def _not_listed(self, nlevels, data):
        ''' Returns a list of dicts of not considered keys in nlevels '''

        not_listed = []
        for key in data:
            if key not in nlevels:
                not_listed.append({key: data[key]})

        return not_listed

    def _prepare_output(self, nlevels):
        ''' From input args order, prepares the output dict '''

        ## Variables
        outdict = {}        # Will hold the final data structure
        aux = outdict       # Auxiliar

        ## Loop to build the final data structure
        for data in self.input_data:
            for i,level in enumerate(nlevels):
                if i + 1 < len(nlevels):
                    if level not in aux:
                        aux[data[level]] = {}
                        aux = aux[data[level]]
                else:
                    aux[data[level]] = self._not_listed(nlevels, data)
            aux = outdict

        ## Prints to stdout the json formatted data
        print(json.dumps(outdict, indent=2))

    def run(self):
        ''' Run, Nest. Run! '''

        ## Read input json formatted from stdin
        self._read_input_stdin()

        ## Instantiate an ArgumentParser object to deal with arguments
        parser = argparse.ArgumentParser(
            description = 'CLI for Revolut Python Engineer Data Challenge')
        parser.add_argument(                ## Receives a list of strings
            'nesting_levels',               ## to be parsed as keys from
            type=str,
            nargs='+',
            help='Nesting level order')     ## input dict
        args = parser.parse_args()

        ## Prepare output dict and print it to stdout
        self._prepare_output(args.nesting_levels)

## Run the command
if __name__ == '__main__':

    nest = Nest()
    nest.run()
