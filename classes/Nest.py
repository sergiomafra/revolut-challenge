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

    def _read_input_stdin(self):
        ''' Read input information from stdin '''

        ## Reading input from stdin
        input_text = ''
        for line in sys.stdin.readlines():
            input_text += line

        ## Loading string as JSON
        ## Returning to run
        return json.loads(input_text)

    def read_input_from_file(self, filename):
        ''' Read input from a specified file '''

        with open(filename, 'r') as json_data:
            json_data = json.loads(json_data.read())

        return json_data

    def _not_listed(self, nlevels, data):
        ''' Returns a list of dicts of not considered keys in nlevels '''

        not_listed = []
        for key in data:
            if key not in nlevels:
                not_listed.append({key: data[key]})

        return not_listed

    def _prepare_output(self, input_data, nlevels):
        ''' From input args order, prepares the output dict '''

        ## Variables
        outdict = {}        # Will hold the final data structure
        aux = outdict       # Auxiliar

        ## Loop to build the final data structure
        for data in input_data:
            for i,level in enumerate(nlevels):
                if i + 1 < len(nlevels):
                    if data[level] not in aux:
                        aux[data[level]] = {}
                    aux = aux[data[level]]
                else:
                    aux[data[level]] = self._not_listed(nlevels, data)
            aux = outdict

        return outdict

    def run(self):
        ''' Run, Nest. Run! '''

        ## Read input json formatted from stdin
        input_data = self._read_input_stdin()

        ## Instantiate an ArgumentParser object to deal with arguments
        parser = argparse.ArgumentParser(
            description = 'CLI for Revolut Python Engineer Data Challenge')
        parser.add_argument(                ## Receives a list of strings
            'nesting_levels',               ## to be parsed as keys from
            type=str,                       ## input dict
            nargs='+',
            help='Nesting level order')
        args = parser.parse_args()

        ## Prepare output dict
        output_dict = self._prepare_output(input_data, args.nesting_levels)

        print(json.dumps(output_dict, indent=2))
