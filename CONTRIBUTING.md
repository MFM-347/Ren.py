# Contributing to RenPy

Thank you for considering contributing to RenPy! 🎉
Your contributions, whether big or small, are essential to the success of this project. We welcome **bug reports**, **feature requests**, **documentation updates**, and **code improvements**.

## Contribution Guide

### Step 1: Fork the Repository

1. Navigate to the [RenPy repository](https://github.com/MFM-347/Ren.py).
2. Click the **Fork** button in the top-right corner to create your own copy of the repository.

### Step 2: Clone Your Fork

Clone your forked repository to your local machine:

```bash
git clone https://github.com/<your-username>/RenPy.git
cd RenPy
```

### Step 3: Set Up Your Environment

Ensure you have Python installed (Python 3.7+ recommended). Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Ensure everything is working by running the CLI tool:

```bash
python renpy/cli.py --help
```

### Step 4: Create a Branch

Create a descriptive branch name based on your contribution:

```bash
git checkout -b <branch-name>
```

Examples:

- `fix-typo-in-readme`
- `feature-add-new-command`
- `enhance-error-handling`

### Step 5: Make Your Changes

- Update the code, fix bugs, or implement new features in the `renpy` folder.
- Ensure your changes:
  - Are properly documented.
  - Adhere to coding best practices and project conventions.
  - Are accompanied by relevant test cases, if applicable.

### Step 6: Run and Test Your Changes

- Run the project to test functionality:

```bash
python renpy/cli.py <your-arguments>
```

- Run unit tests using `unittest`:

```bash
python -m unittest discover tests
```

- Check code formatting using `black`:

```bash
black .
```

- Check for linting errors using `flake8`:

```bash
flake8 renpy/
```

### Step 7: Commit Your Work

Commit your changes with a clear and descriptive commit message:

```bash
git add .
git commit -m "feat: Add new renaming option"
```

Use [Conventional Commits](https://www.conventionalcommits.org/) format for consistency:

- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation updates
- `style`: Code style changes (non-functional)
- `refactor`: Code refactoring
- `test`: Adding or updating tests

### Step 8: Push and Submit a Pull Request

Push your branch to your fork:

```bash
git push origin <branch-name>
```

Then, navigate to the **original RenPy repository** and submit a pull request.
Include the following in your PR description:

- A summary of changes.
- Related issue IDs (e.g., "Closes #123").
- Screenshots or logs (if applicable).

## Reporting Issues

Encountered a bug or have a great idea for a new feature? Create an issue [here](https://github.com/MFM-347/Ren.py/issues).

### Guidelines for Issues:

- **Bug Reports**:
  Include:

  - Steps to reproduce the issue.
  - Expected vs. actual behavior.
  - Relevant error logs or stack traces.

- **Feature Requests**:
  Describe:
  - The feature and its use case.
  - Any benefits or improvements it will bring.

## Code Standards

To maintain a high-quality codebase, please follow these guidelines:

1. **Coding Style**:

   - Use clean, consistent, and readable code.
   - Follow PEP 8 coding standards.
   - Use `black` for code formatting.

2. **Commit Practices**:

   - Keep commits small and focused.
   - Write clear and meaningful commit messages.

3. **Documentation**:

   - Update documentation for any changes that impact the project’s functionality or usage.

4. **Testing**:
   - Add or update tests for your changes where applicable.
   - Ensure all tests pass before submitting your PR.

## Need Help?

If you’re unsure about something or need guidance:

- Start a [discussion](https://github.com/MFM-347/Ren.py/discussions).
- Join our community for support and collaboration.

Thank you ✨ for contributing to RenPy! Your effort makes this project better for everyone.
