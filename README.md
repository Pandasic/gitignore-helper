# gitignore-helper

## Introduction

a tool to help you generator gitignore file

## how to use

1. python needed
2. change conf file to set resource and default gitignore files

   ```json
   {
       "source_path": "",
       "default": []
   }
   ```

   * soruce_path: the directory where the script get files
   * default: default files you wanna append to new .gitignore file
3. use `--list` to show files in sourece

   ```
   python3 main.py --list
   ```
4. run command

   ```
   python main.py <sub file1> <sub file 2>

   eg:
   python main.py python
   python main.py python C
   ```
5. you can use alias command to use these command in all your projects

## how to get .gitignore files?

you can broswer this project https://github.com/github/gitignore
