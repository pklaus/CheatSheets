# VIM Text Editor

## The three modes of vim

* *Command Mode*: active when starting vim
* *Insert Mode*: active when pressed any of the editin commands
* *Last Line Mode*: active after pressing : or / in command mode

## Editing

`i` insert before cursor  
`a` insert after cursor  
`o` open new line above  
`O` open new line below  

##  Cutting and Pasting

`yy` yank (copy) the current line  
`3yy` yank the current and 2 more lines  
`p` paste the yanked content after current position  
`P` paste yanked content before current position  

## Deleting

`x` delete current character  
`8x` delete 8 characters to the right  
`dd` delete the current line  
`4dd` delete the current plus 3 more lines  
`d0` delete from position to beginning of line  
`d$` delete from current position to end of line  

## Navigation

`$` go to the end of the current line  

`w` forward one word  
`b` backward one word  

`1G` Go to the very first line  
`G` go to the very last line  

`H` go to the first currently visible line  
`M` go to the middle of the currently visible lines  
`L` go to the last currently visible line  

## Searching

`/foo` search for *foo*  
`n` repeat last search  
`N` repeat last search backwards

## Windows and SplitView

`:split filename` and  
`:vsplit filename` will split your vim and open another file simultaneously.

Navigate using the `Ctrl-w` window commands:  
`Ctrl-w h` or `Ctrl-w l` to move left and right  
`Ctrl-w j` or `Ctrl-w k` to move down and up  
`Ctrl-w c` - Close this window  
`Ctrl-w o` - close all Other windows (mnemonic - Only)  
`Ctrl-w 5+` - increase this window size by 5 lines  

## Special commands

`:!ls` run the `ls` command in the working directory
