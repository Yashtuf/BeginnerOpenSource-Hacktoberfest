

### Steps to Add Contributors

If you have done it before skip these and directly jump to How to add contributors.
- Star the project

![1727809286330](image/Contributors/1727809286330.png)

- Fork this repo 

![1727802141861](image/Contributors/1727802141861.png)



- click on create fork

![1727802179610](image/Contributors/1727802179610.png)


- After creating the fork you will see like this

![1727802242826](image/Contributors/1727802242826.png)


- now Click here to create new branch

![1727802405048](image/Contributors/1727802405048.png)

- Now click on new branch

![1727802435304](image/Contributors/1727802435304.png)

- Now  give the new branch name as you like prefer use your username as branch name and click on create new branch.


![1727802525712](image/Contributors/1727802525712.png)



- Now we can see the branch names and you can find your branch name here

![1727802612463](image/Contributors/1727802612463.png)





- Now we need to go back to the project which is in your github. click here you can find your branch name here

![1727802778042](image/Contributors/1727802778042.png)


- click on your branch name now you can find that there is change in branch name instead of main you can find your branch name here.

![1727802860788](image/Contributors/1727802860788.png)

- so now we are ready to make changes in your project. And make sure any changes you are making in the project should be done in your branch only.

![1727802973447](image/Contributors/1727802973447.png)


- Now before we make any changes in our project we should check these two things 
     - first check the branch name is it our's or not,if it's not our branch we need to change the branch.
     - we need check that our branch is doesn't have commits behind the main(repository owner branch)
     - if we found that any commit's behind like in the picture just click on sync fork.

![1727803442001](image/Contributors/1727803442001.png)

- You can click on the comapre  or you can click on the update branch directly it will change to lastest commit on the branch.

![1727803818397](image/Contributors/1727803818397.png)




- First pull request 


![1727804007016](image/Contributors/1727804007016.png)

- first click on the Contributors_website

- Next It will Change like this 

![1727804063234](image/Contributors/1727804063234.png)

- Now Click on the contributors

![1727804185569](image/Contributors/1727804185569.png)

- Now open the contributersList.js and copy the code from here

![1727804249810](image/Contributors/1727804249810.png)



- Now click on the pencil symbol to edit the file.
![1727804377647](image/Contributors/1727804377647.png)


- Before editing the file
![1727804490484](image/Contributors/1727804490484.png)

- After Editing,like this you need add id numbers and details

![1727804597072](image/Contributors/1727804597072.png)

- click on commit changes
![1727804686356](image/Contributors/1727804686356.png)


- click on commit changes
![1727804725666](image/Contributors/1727804725666.png)

- Now go back to your github repository make sure you are in your branch where you find like this comapare and pull request
![1727804889954](image/Contributors/1727804889954.png)


- click on that compare and pull request and click on create pull request

![1727804992542](image/Contributors/1727804992542.png)


- here like this your pull request sent successfully now once we will  acept that pull request

![1727805124958](image/Contributors/1727805124958.png)
 
-  For maintainer he will recive like this when ever he accepts and merges the pull request
![1727805371290](image/Contributors/1727805371290.png)

-It will look like this which is maintainer duty to merge 

![1727805459864](image/Contributors/1727805459864.png)

- After successfull pr/merge you can find 1 commit back so we need to sync fork and start next Pull request.

![1727805613409](image/Contributors/1727805613409.png)


2. Now we create 2nd pull request for the Programs 
click on the programs and select the programming language we need to add programs

![1727807651485](image/Contributors/1727807651485.png)

- here i'm selecting the python ,now click on the add file

![1727807768270](image/Contributors/1727807768270.png)


- Here you can create or upload file 
![1727807816069](image/Contributors/1727807816069.png)

 - here i select the create new file option

- and add name.py here i choose factorial.py and commit changes
 ![1727807976522](image/Contributors/1727807976522.png)

 -Now we succesfully created another pull request

  ![1727808057486](image/Contributors/1727808057486.png)

- Now we can see 1 commit behit now click  on the contibute button



![1727808181769](image/Contributors/1727808181769.png)


- click on open pull request

![1727808245565](image/Contributors/1727808245565.png)


- Now click on create pull request

![1727808332758](image/Contributors/1727808332758.png)

- Now we successfull  sent and completed pr/merge request

3. Now 3rd pull request

- now we can complete this by using upload file 

- first go programs and in programs select any language for this i'm selecting python
- Click on the Add file and select upload file

![1727808660842](image/Contributors/1727808660842.png)

- Now we can add file or drang and drop file next click on commit changes

![1727808715940](image/Contributors/1727808715940.png)
-here file uploaded successfully

![1727808852428](image/Contributors/1727808852428.png)

now click on contribute ->open pullrequest->create pull request 
- next sync fork the branch and do the remaing pull requests



### CLI commands

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


### Example


## How to add Contributors??


- First Open the [file](https://github.com/yaswanthteja/BeginnerOpenSource-Hacktoberfest/blob/main/Contributors_Website/contributors/contributorsList.js)




Congrats! You just completed the standard _fork -> clone -> edit -> pull request_ workflow that you'll often encounter as a contributor!

1. Fork the repository and create a copy to your github

2. Clone the repository
```
git clone https://github.com/yaswanthteja/BeginnerOpenSource-Hacktoberfest.git
```


3. **Navigate to the Project Directory:**

   ```bash
   cd BeginnerOpenSource-Hacktoberfest
   ```

4. **Create a New Branch:**

   ```bash
   git checkout -b my-new-branch
   ```
   

5. **Make Your Changes:**
```
cd contributors/
```
   - Add your name to `contributors/contributorsList.js` and make any other contributions.


now open the contributorsList.js file and edit and add the details


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





   ```bash
   git add .
   ```

6. **Commit Your Changes:**

   ```bash
   git commit -m "Relevant message"
   ```

7. **Push to Your Branch:**

   ```bash
   git push origin my-new-branch
   ```

8. **Create a Pull Request:**
   - Go to your forked repository on GitHub and create a pull request to the main repository.

## Avoiding Conflicts {Syncing Your Fork}

To keep your fork up-to-date with the main repository and avoid conflicts:

1. **Add Upstream Remote:**

   ```bash
   git remote add upstream https://github.com/yaswanthteja/BeginnerOpenSource-Hacktoberfest
   ```

2. **Verify the New Remote:**

   ```bash
   git remote -v
   ```

3. **Sync Your Fork with Upstream:**

   ```bash
   git fetch upstream
   git merge upstream/main
   ```

   This will pull in changes from the parent repository and help you resolve any conflicts.

4. **Keep Updated:**
   - Regularly pull changes from the upstream repository to keep your fork updated.

