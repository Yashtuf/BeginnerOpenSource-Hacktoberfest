

### Steps to Add Contributors

If you have done it before skip these and directly jump to How to add contributors.

- Fork this repo 
- Clone it on your local machine

```terminal
git clone https://github.com/yaswanthteja/BeginnerOpenSource-Hacktoberfest.git
```

- Navigate to the project directory.

```terminal
cd BeginnerOpenSource-Hacktoberfest
```

- Create a new branch

```markdown
git checkout -b my-new-branch
```

<!--- - Add your name to `contributors/contributorsList.js`. -->

```markdown
git add .
```

- Commit your changes.

```markdown
git commit -m "Relevant message"
```

- Then push

```markdown
git push origin my-new-branch
```

- Create a new pull request from your forked repository

<br>

## Avoid Conflicts {Syncing your fork}

An easy way to avoid conflicts is to add an 'upstream' for your git repo, as other PRs may be merged while you're working on your branch/fork.   

```terminal
git remote add upstream https://github.com/yaswanthteja/BeginnerOpenSource-Hacktoberfest
```

You can verify that the new remote has been added by typing:

```terminal
git remote -v
```

To pull any new changes from your parent repo, simply run:

```terminal
git merge upstream/main
```

This will give you any eventual conflicts and allow you to easily solve them in your repo. It's a good idea to use it frequently in between your own commits to make sure that your repo is up to date with its parent.

For more information on syncing forks, [read this article from GitHub](https://help.github.com/articles/syncing-a-fork/).





## How to add Contributors??


- First Open the [file](https://github.com/yaswanthteja/BeginnerOpenSource-Hacktoberfest/blob/main/Contributors_Website/contributors/contributorsList.js)




<img align="Center" width="400" src="image/Contributors/1727791025228.png" alt="Add contributor details" />



- Now copy the Following code and add the following details.
- Just follow the id number and Paste  below  as shown 

```
  {
    id: number,                            //add continuos numbers ex 1,2,3...
    fullname: "Enter your name ",          //add your full name
    username: "Your github link",          //add your github link
  },
```

example:- suppose already we have 11 members entered their details next id number should be 12 and so on

```
{
    id: 12,                            //add continuos numbers
    fullname: "Pavan ",          //add your full name
    username: "https://github.com/use",          //add your github link
  },

```

