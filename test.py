# change it up 

import unittest
from levels import System

class TestSystem(unittest.TestCase):
    def setUp(self):
        """Create a new System object before each test."""
        self.system = System()

    def test_default_constructor(self):
        """Test that the default constructor initializes attributes correctly."""
        self.assertEqual(self.system.getLevel(), 0)
        self.assertEqual(self.system.getTasks(), {})

    def test_set_and_get_level(self):
        """Test setting and getting the current level."""
        self.system.setLevel(5)
        self.assertEqual(self.system.getLevel(), 5)

        self.system.setLevel(10)
        self.assertEqual(self.system.getLevel(), 10)

    def test_set_and_get_tasks(self):
        """Test setting and getting tasks."""
        tasks = {"task1": "Complete assignment", "task2": "Write report"}
        self.system.setTasks(tasks)
        self.assertEqual(self.system.getTasks(), tasks)

        updated_tasks = {"task3": "Prepare presentation"}
        self.system.setTasks(updated_tasks)
        self.assertEqual(self.system.getTasks(), updated_tasks)

    def test_update_tasks(self):
        """Test that updating tasks works correctly."""
        self.system.setTasks({"task1": "Do something"})
        self.system.tasks["task2"] = "Do another thing"
        self.assertEqual(self.system.getTasks(), {"task1": "Do something", "task2": "Do another thing"})

if __name__ == "__main__":
    unittest.main()