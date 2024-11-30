# change it up 

import unittest
from src.tasks import Task
from src.levels import Level

#testing task class
class TestTask(unittest.TestCase):
    def setUp(self):
        self.task = Task()

    def test_initial_tasks(self):
        self.assertEqual(self.task.getTasks(), {}, "Initial task list should be empty.")

    def test_add_task(self):
        self.task.addingTasks("Task1", 10)
        self.assertIn("Task1", self.task.getTasks(), "Task1 should be added.")
        self.assertEqual(self.task.getTasks()["Task1"], 10, "Task1's XP should be 10.")

    def test_multiple_tasks(self):
        self.task.addingTasks("Task1", 10)
        self.task.addingTasks("Task2", 20)
        self.assertEqual(len(self.task.getTasks()), 2, "There should be two tasks.")
        self.assertDictEqual(self.task.getTasks(), {"Task1": 10, "Task2": 20}, "Tasks should match the expected dictionary.")

#testing level class
class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level()

    def test_initial_values(self):
        self.assertEqual(self.level.getLevel(), 0, "Initial level should be 0.")
        self.assertEqual(self.level.getXp(), 0.0, "Initial XP should be 0.0.")

    def test_set_and_get_level(self):
        self.level.setLevel(15)
        self.assertEqual(self.level.getLevel(), 15, "Level should be set to 15.")

    def test_set_and_get_xp(self):
        self.level.setXp(200.5)
        self.assertEqual(self.level.getXp(), 200.5, "XP should be set to 200.5.")

    def test_xp_requirement(self):
        self.level.setLevel(10)
        expected_xp_req = 10 + 57 * 10 + 100.0  # 10 + 570 + 100 = 680.0
        self.assertEqual(self.level.getXpRequirement(), expected_xp_req, f"XP requirement should be {expected_xp_req}.")

    def test_tier_ranking(self):
        test_cases = {
            5: "F",
            15: "E",
            30: "D",
            50: "C",
            70: "B",
            90: "A",
            110: "S",
            130: "S+",
        }
        for level, expected_tier in test_cases.items():
            with self.subTest(level=level):
                self.level.setLevel(level)
                self.assertEqual(self.level.getTier(), expected_tier, f"Tier for level {level} should be {expected_tier}.")

if __name__ == "__main__":
    unittest.main()