import unittest

from robot import(
    Robot
)

from robot import(
    Tabletop
)

class SimulationTest(unittest.TestCase):

    def test_simulation_test_case_1(self):
        simulation=Robot()
        print("Testing case 1: one PLACE in origin, one MOVE one REPORT.")
        self.assertEqual(simulation.executeCommands('PLACE 0,0,NORTH MOVE REPORT'),'01NORTH')

    def test_simulation_test_case_2(self):
        simulation=Robot()
        print("Testing case 2: one PLACE in origin, one LEFT (rotation of robot).")
        self.assertEqual(simulation.executeCommands('PLACE 0,0,NORTH LEFT REPORT'),'00WEST')

    def test_simulation_test_case_3(self):
        simulation=Robot()
        print("Testing case 3: one PLACE in non-origin, multiple MOVE, one LEFT (rotation of robot).")
        self.assertEqual(simulation.executeCommands('PLACE 1,2,EAST MOVE MOVE LEFT MOVE REPORT'),'33NORTH')

    def test_simulation_test_case_4(self):
        simulation=Robot()
        print("Testing case 4: one PLACE in origin, one RIGHT (rotation of robot), multiple MOVE.")
        self.assertEqual(simulation.executeCommands('PLACE 0,0,EAST MOVE MOVE RIGHT MOVE MOVE REPORT'),'20SOUTH')

    def test_simulation_test_case_5(self):
        simulation=Robot()
        print("Testing case 5: one PLACE in origin, out of bounds (east, x) MOVE.")
        self.assertEqual(simulation.executeCommands('PLACE 0,0,NORTH RIGHT MOVE MOVE MOVE MOVE MOVE MOVE REPORT'),'50EAST')

    def test_simulation_test_case_6(self):
        simulation=Robot()
        print("Testing case 6: one PLACE in origin, out of bounds (north, y) MOVE.")
        self.assertEqual(simulation.executeCommands('PLACE 0,0,NORTH MOVE MOVE MOVE MOVE MOVE MOVE REPORT'),'05NORTH')

    def test_simulation_test_case_7(self):
        simulation=Robot()
        print("Testing case 7a: one PLACE in origin, out of bounds (west, x; south, y) MOVE.")
        self.assertEqual(simulation.executeCommands('PLACE 0,0,WEST MOVE LEFT MOVE MOVE MOVE REPORT'),'00SOUTH')

        simulation=Robot()
        print("Testing case 7b: one PLACE in origin, multiple LEFT (rotation of robot), out of bounds (west) MOVE.")
        self.assertEqual(simulation.executeCommands('PLACE 0,0,EAST LEFT LEFT MOVE MOVE MOVE REPORT'),'00WEST')

    def test_simulation_test_case_8(self):
        simulation=Robot()
        print("Testing case 8: multiple PLACE in non-origin, out of bounds (west) MOVE.")
        self.assertEqual(simulation.executeCommands('PLACE 4,4,EAST MOVE LEFT MOVE PLACE 1,2,WEST MOVE MOVE MOVE REPORT'),'02WEST')

    def test_simulation_test_case_9(self):
        simulation=Robot()
        print("Testing case 9: discard all commands before valid PLACE (non-origin), mulitple MOVE, multiple rotation.")
        self.assertEqual(simulation.executeCommands('REPORT MOVE LEFT MOVE PLACE 4,4,EAST MOVE LEFT MOVE REPORT'),'55NORTH')
    



if __name__ == '__main__':
    unittest.main()
