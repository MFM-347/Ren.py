import logging

from pyfiglet import Figlet


class RenPy:
    def __init__(self, debug=False):
        self.logger = logging.getLogger(__name__)
        self._setup_logging(debug)

    def _setup_logging(self, debug):
        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(message)s",
            level=logging.DEBUG if debug else logging.INFO,
        )

    @staticmethod
    def banner():
        f = Figlet(font="speed")
        print(f.renderText("RenPy"))

    def sortFn(self, directory, order="old", case_sensitive=False):
        files = [f for f in directory.iterdir() if f.is_file()]
        if order == "alphabet":
            files.sort(key=lambda f: f.name if case_sensitive else f.name.lower())
        elif order == "new":
            files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
        else:
            files.sort(key=lambda f: f.stat().st_mtime)
        return files

    def renFn(
        self, base_name, directory, order="old", simulate=False, case_sensitive=False
    ):
        try:
            files = self.sortFn(directory, order, case_sensitive)
            if not files:
                self.logger.warning("No files found in the directory.")
                return

            for index, file in enumerate(files, start=1):
                new_name = f"{base_name}-{index}{file.suffix if file.suffix else ''}"
                new_path = directory / new_name
                counter = 1

                while new_path.exists():
                    new_name = f"{base_name}-{index}_{counter}{file.suffix if file.suffix else ''}"
                    new_path = directory / new_name
                    counter += 1

                if simulate:
                    self.logger.info(f"Simulated: {file.name} -> {new_name}")
                else:
                    file.rename(new_path)
                    self.logger.info(f"Renamed: {file.name} -> {new_name}")

            if simulate:
                self.logger.info(f"Simulated renaming of {len(files)} files.")
        except Exception as e:
            self.logger.error(f"Error: {e}")
