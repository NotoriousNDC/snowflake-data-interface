# GitHub Setup Instructions

Follow these steps to push this repository to GitHub:

## 1. Create a new repository on GitHub

1. Go to [GitHub](https://github.com)
2. Log in to your account
3. Click the "+" icon in the top right corner and select "New repository"
4. Name your repository (e.g., "snowflake-data-interface")
5. Add a description (optional)
6. Keep it public or set it to private as needed
7. Do NOT initialize it with a README, .gitignore, or license as we already have these files locally
8. Click "Create repository"

## 2. Push your local repository to GitHub

After creating the repository, GitHub will show instructions for pushing an existing repository. Execute the following commands in your terminal:

```bash
# Add the remote repository (replace 'YOUR-USERNAME' with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/snowflake-data-interface.git

# Push the changes to GitHub
git push -u origin master
```

If you want to use SSH instead of HTTPS, use:
```bash
git remote add origin git@github.com:YOUR-USERNAME/snowflake-data-interface.git
git push -u origin master
```

## 3. Verify the repository

Go to your GitHub account and verify that the repository has been created with all the files.

## 4. Using the Snowflake VSCode Extension

1. Make a copy of `config/connection.json.example` to `config/connection.json` and update it with your Snowflake credentials
2. Make a copy of `.vscode/settings.json.example` to `.vscode/settings.json` and update it with your Snowflake connection details
3. Open the repository in VSCode and install the Snowflake extension if not already installed
4. Use the extension to connect to your Snowflake account and run queries 