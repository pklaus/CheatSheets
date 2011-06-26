# VIM Text Editor

## The three modes of vi

* Command Mode
* Insert Mode
* Last Line Mode

## Editing

`i` insert  
`o` enter a new line above  
`O` enter a new line below  

##  Cutting and Pasting

`yy` yank (copy) the current line  
`3yy` yank the current and 2 more lines  
`p` paste the yanked content after current position  
`P` paste the yanked content before the current position  

## Deleting

`x` delete current character  
`8x` delete 8 characters to the right  
`dd` delete the current line  
`4dd` delete the current plus 3 more lines  
`d0` delete from position to beginning of line  
`d$` delete from current position to end of line  

## Navigation

`1G` Go to the very first line  
`G` go to the very last line  
`H` go to the first currently visible line  
`M` go to the middle of the currently visible lines  
`L` go to the last currently visible line  

## Searching

`/foo` search for *foo*  
`n` repeat last search  
`N` repeat last search backwards  
