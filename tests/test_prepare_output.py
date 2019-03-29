class PrepareOutputTests:

    def test_output1(self, nest_instance):

        test_nlevels1 = ['currency', 'country', 'city']
        test_input1 = [{
            'country': 'FR',
            'city': 'Paris',
            'currency': 'EUR',
            'amount': 20
        }]
        test_output1 = {'EUR': {'FR': {'Paris': [{'amount': 20}]}}}

        nest = nest_instance

        assert nest._prepare_output(test_input1, test_nlevels1) == test_output1

    def test_output2(self, nest_instance):
        test_nlevels2 = ['city', 'amount', 'currency']
        test_input2 = [{
            'country': 'UK',
            'city': 'London',
            'currency': 'FBP',
            'amount': 10.9
        }]
        test_output2 = {'London': {10.9: {'FBP': [{'country': 'UK'}]}}}

        nest = nest_instance

        assert nest._prepare_output(test_input2, test_nlevels2) == test_output2

    def test_output3(self, nest_instance):

        test_nlevels3 = ['country', 'city', 'currency']
        test_input3 = [{
            'country': 'ES',
            'city': 'Madrid',
            'currency': 'EUR',
            'amount': 8.9
        }]
        test_output3 = {'ES': {'Madrid': {'EUR': [{'amount': 8.9}]}}}

        nest = nest_instance

        assert nest._prepare_output(test_input3, test_nlevels3) == test_output3
