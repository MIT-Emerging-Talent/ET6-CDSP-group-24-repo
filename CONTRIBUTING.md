# Contributing to CrystalPearl Rising Team Project

Welcome to our collaborative data science project! This guide will help you
contribute effectively to our repository while maintaining code quality and consistency.

## 🚀 Getting Started

### 1. Repository Setup

```bash
# Clone the repository
git clone [repository-url]
cd [repository-name]

# Install dependencies
pip install -r requirements.txt

# Install development dependencies for linting and formatting
pip install ruff pylint
```

### 2. Development Environment

- Python 3.8+
- Notebook environment (Jupyter, VS Code, Colab, etc.)
- Git for version control

## 📋 Contribution Workflow

### 1. Before Making Changes

- Pull the latest changes from main branch
- Check existing issues or create a new issue to track your work
- Create a new branch for your work:

  ```bash
  git checkout -b your-feature
  ```

### 2. Making Changes

- Follow our folder structure for organizing work by milestones
- Add your work to the appropriate milestone folder (0_domain_study, 1_datasets,
etc.)
- Document any notes in the `notes/` folder if helpful for the team

### 3. Code Quality Standards

#### Python Code

- **Formatting**: All Python code must pass `ruff format`
- **Linting**: Code must pass both `ruff` and `pylint` checks
- Use meaningful variable names and add comments for complex logic
- Include docstrings for functions and classes

#### Markdown Files

- Follow consistent markdown formatting (our CI checks this automatically)
- Use proper headers hierarchy (# ## ### ####)
- Include blank lines around code blocks and lists
- Use descriptive link text

### 4. Running Quality Checks Locally

Before pushing your changes, run these commands to ensure CI will pass:

```bash
# Format Python code
ruff format .

# Check Python linting
ruff check .
pylint **/*.py

# Your markdown will be checked automatically by CI
```

### 5. Pull Request Process

- Push your branch and create a pull request with the template
- Link the relevant issue and milestone to your pull request
- Add the pull request to the project board if not linked to an issue already
present in the board
- Ensure all CI checks pass (markdown formatting, ruff format, ruff + pylint)
- Request review from at least one team member
- Address any feedback before merging

## 📁 Repository Organization

### Where to Put Your Work

- **0_domain_study/**: Initial research, domain exploration
- **1_datasets/**: Data storage and management
- **2_data_preparation/**: Data cleaning and preprocessing code
- **3_data_exploration/**: Exploratory data analysis
- **4_data_analysis/**: Advanced analysis and modeling
- **5_communication_strategy/**: Communication strategy for research findings
- **6_final_presentation/**: Final deliverables and presentation materials
- **notes/**: Team notes, insights, useful resources

## 🤝 Team Collaboration

### Code Reviews

- Be constructive and respectful in feedback
- Focus on code quality, logic, and adherence to our standards
- Appreciate different approaches and perspectives

### Conflict Resolution

- Follow our [group norms](collaboration/group-norms.md)
- Discuss disagreements openly and respectfully
- Reach out to a team member if needed

## 🔧 CI/CD Pipeline

Our automated checks include:

- **Markdown Formatting**: Ensures consistent documentation style
- **Python Formatting**: `ruff format` for code style consistency
- **Python Linting**: `ruff` + `pylint` for code quality and best practices

All checks must pass before merging. If CI fails:

1. Check the error messages in the GitHub Actions tab
2. Fix the issues locally
3. Test your fixes with the commands above
4. Push the corrected code

## ❓ Getting Help

- Check existing issues in the repository
- Review our [collaboration documentation](collaboration/)
- Reach out to team members for pair programming or code review

## 🎯 Quality Checklist

Before submitting your contribution:

- [ ] Code follows our formatting standards (ruff format)
- [ ] Code passes linting checks (ruff + pylint)
- [ ] Markdown is properly formatted
- [ ] Work is in the appropriate milestone folder
- [ ] Commit messages are clear and descriptive

---

Thank you for contributing to CrystalPearl Rising Team! Together, we transform
raw potential into brilliant insights. 💎
