# Tools  
A project with my tools for cracking    
  
## rulegen 
A simple tool to make single rules. Append and Preppend or both.  
This tool will also make special chars into hex.  
Usage: `python3 ./rulegen.py -c 0 -f file.txt -o out.rule` 
  
C/Converting words:  
0 = Append  
1 = Prepend  
2 = Append and Prepend  
  

## domainConvert  
This tool will generate from domain.com into $@$d$o$m$a$i$n$.$c$o$m.  
Really great when testing a wordlist with names and using this as rule to generate emails.  
  
Usage: `python3 ./dconvert.py -f inputfile.txt -o outputfile.rule`  
  
Output Example: `$@$h$e$l$l$o$.$w$o$r$l$d`  
Stripped Example: `@hello.world`  
