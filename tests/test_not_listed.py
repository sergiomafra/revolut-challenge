class NotListedTests:

    data = {
        'country': 'US',
        'city': 'Boston',
        'currency': 'USD',
        'amount': 100
    }

    def test_not_listed1(self, nest_instance):
        test_nlevels1 = ['currency', 'country', 'city']
        test_output1 = [{'amount': 100}]

        nest = nest_instance

        assert nest._not_listed(test_nlevels1, self.data) == test_output1

    def test_not_listed2(self, nest_instance):
        test_nlevels2 = ['amount', 'country', 'currency']
        test_output2 = [{'city': 'Boston'}]

        nest = nest_instance

        assert nest._not_listed(test_nlevels2, self.data) == test_output2

    def test_not_listed3(self, nest_instance):
        test_nlevels3 = ['city', 'amount', 'country']
        test_output3 = [{'currency': 'USD'}]

        nest = nest_instance

        assert nest._not_listed(test_nlevels3, self.data) == test_output3
