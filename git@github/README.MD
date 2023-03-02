COMMANDS FOR GIT@GITHUB



# git tool
> tools to show differences in git files
> meld | kdiff3 | vimdiff 
> gittyup
> diff -u 1stfile.py 2ndfile.py
> wdiff highlights words that changes in files
> alternatives to git ::subversion | mercurial::
diff -u old_version.py new_version.py > file.diff
patch old_version < file.diff

## git commands 
1- **global config** 
> git init ==>> gives git directory databases
> git log --stats ====>> gives statistiques
>git commit -a Stages files automatically
>git log -p Produces patch text gives general patch details git log -p -2
>git show  ====>> shows  details(path etc...) for specific commit Shows various objects
>git diff Is similar to the Linux `diff` command, and can show the differences in various commits
>git diff --staged An alias to --cached, this will show all staged files compared to the named commit
>git add -p Allows a user to interactively review patches to add to the current commit
>git mv Similar to the Linux `mv` command, this moves a file
>git rm Similar to the Linux `rm` command, this deletes, or removes a file
>git checkout file1 file2 ==>>go back to before stage 
>git checkout -p file1 file2 ==>>individual changes
>git reset ==>> unstage files from a specific pointer|alias(like HEAD )
>git reset -p ==>> unstage specific details from a specific pointer
**Amending Commits**
>git commit --amend =>  allows us to modify and add changes to the most recent commit. 
> -it does a rewrite on commit ,and that may create a confusing situation in collaboration projects	 
**Rollback Commits**
>git revert HEAD ==>a commit contains inverse for all changes made in bad commit in POINTER HEAD
> -git commit id is a HASH SHA1
**Branches**
>branch a pointer to particular commit
>git branch =>list branches
>git branch new-features =>new branches
>git checkout newbranch =>switch branch
> -git checkout -b newbranch =>create and switch to it	
>git branch  -d => delete branch use -D to force the delete
>git merge new-feature =>to merge new-feature branch to master branch(did it when on master branch)
> -HEAD points to master branch
> -both master,new-feature points to the same commit id
**checkout a file from branch B TO A**
>git switch branchA && git show feature/B:path/utils.js > path/utils.js
>git checkout branchA && git checkout branchB -- filename => this would cp file "filename" from B to A

**merging Algorithms**
> 1-fast-forwarding =>just push the differences to the master branch
> 2-three-way-merge => when there is diversion of branches

**merging with conflict**

>git log --graph --oneline
>git merge --abort => If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action.

*git merge*
>after finding a  confilict ,we fix it then add the conflicted files 
>to the staging area then we commit and push again
>git checkout a file to


**credentials mangement**
**global for all users in the**
> git config --global user.email "abdallah.bouhannache@gmail.com"
> git config --global user.name  "abdallahbouhananche"
> git config --global credential.helper cache => manage credentials using credential.helper

**some ressources**
[ ![](https://help.github.com/en/articles/caching-your-github-password-in-git)](cache your git pass)
[ ![ssh-key-generation](https://help.github.com/en/articles/generating-an-ssh-key)](ssh-key-generation)
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](LICENSE)
[![](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-merge-conflicts)]()

[![](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line)](resolv-merge)
[![](http://google.github.io/styleguide/)](1)

[![](https://help.github.com/en/articles/about-pull-request-reviews)](1)

[![](https://medium.com/osedea/the-perfect-code-review-process-845e6ba5c31)](1)

[![](https://smartbear.com/learn/code-review/what-is-code-review/)](1)



**remote repo**
>git remote show origin ==> shows remote repo details
>git log origin/master => show remote master details
>git merge origin/master =>merges remote master to our local repo
>git remote update => fetch remote updates and we can call checkout and merge when we want
>git remote update =>Fetches the most up-to-date objects
>git fetch=> Downloads specific objects
>git push --delete origin/refractor
>git push -f => force push to remote
[![](https://help.github.com/en/articles/about-pull-request-merges](pull-request)

## **git rebase**
*STEPS*
>git checkout the branch-A that has merge-conflicts && git rebase with the new base branch-B
>git checkout the branch-B && git merge branch-A
>git rebase branch-to-set-as-new-base
>git rebase --continue => used when we need to continue rebase after fixing conflict
>git rebase -i branch => to manage your rebase fixup/squash to add two commits togheter 


**pull request**
>could be reaccessed with pull request number



**collaboration**
>pep8 =>style guide 
>pypi => python package index
>issue tracker  =>An issue tracker tells us the tasks that need to be done, the state they're in and who's working on them
>bug tracker =>like bugzilla ,github has its own bug tracker
>jenkins => CI/CD 
>travis => used with github for CI/CD [![](www.travis-ci.com)](travis)
>*piplines* : **the steps that need to run to reach the result**
>*artifacts* :**the name used to describe anyfiles that are genrated from piplines**
>advisable =>to make log for piplines




git set-upstream  
git push

git fetch branch --prune
git branch --delete --remotes remotes/main
git branch set-upstream
git stash and squash
git switch
git restore


# github tool



# checking the difference tools
