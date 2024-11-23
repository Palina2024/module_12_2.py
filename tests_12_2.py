from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for place, runner in cls.all_results.items():
            print(f"{place}: {runner.name}")


    def test_race_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results = results
        print(f"Results race 1: {results}")
        self.assertTrue(self.all_results[max(self.all_results.keys())] == "Ник")


    def test_race_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results = results
        print(f"Results race 2: {results}")
        self.assertTrue(self.all_results[max(self.all_results.keys())] == "Ник")

    def test_race_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results = results
        print(f"Results race 3: {results}")
        self.assertTrue(self.all_results[max(self.all_results.keys())] == "Ник")



if __name__ == "__main__":
        unittest.main()