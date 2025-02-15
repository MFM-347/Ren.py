import unittest
from pathlib import Path

from renpy.core import RenPy


class TestRenPy(unittest.TestCase):
    def setUp(self):
        self.renpy = RenPy(debug=True)
        self.test_dir = Path("test_files")
        self.test_dir.mkdir(exist_ok=True)

        for i in range(3):
            (self.test_dir / f"file_{i}.txt").touch()

    def tearDown(self):
        for file in self.test_dir.iterdir():
            file.unlink()
        self.test_dir.rmdir()

    def test_get_sorted_files(self):
        files = self.renpy.sortFn(self.test_dir, order="alphabet")
        self.assertEqual(len(files), 3)

    def test_rename_files_simulation(self):
        self.renpy.renFn("Test", self.test_dir, order="alphabet", simulate=True)
