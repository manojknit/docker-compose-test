# Docker Compose Quickstart
https://docs.docker.com/compose/gettingstarted/

## Branching
```
# Create main/master first time - default branch
git checkout -b main
git add .
git commit -m "Initial commit"
git push -u origin main

# Step 1: Create and switch to the new branch
git checkout -b mybranch

# Step 2: Make changes and commit
# Add your changes
git add .

# Commit your changes
git commit -m "Add new feature in mybranch"

# Step 3: Push the new branch to the remote repository
git push -u origin mybranch

# After pushing the branch, you can verify that it has been pushed to the remote repository by running:
git branch -r

#Create PR from Pull Request in GitHub Base = your branch
switch back after pr merge
git checkout main
git pull
```


### Build and run your app with Compose
```
$ docker compose up --build
$ docker-compose down
docker compose up -d: This flag stands for "detached mode." When used, it runs the containers in the background, allowing you to continue using the terminal for other tasks.
```
Enter http://localhost:8000/ in a browser to see the application running