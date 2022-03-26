# Tools  
A project with my tools for cracking    
  
## SingleRuleConverter  
A simple tool to make single rules. Append and Preppend.  
This tool will also make special chars into hex.  
Usage: ``python3 SingleRuleConverter.py``  
  
You will be asked to input a string then a number for which method you want to use.  
0 = Append  
1 = Preppend   


## domainConvert  
This tool will generate from domain.com into $@$d$o$m$a$i$n$.$c$o$m.  
Really great when testing a wordlist with names and using this as rule to generate emails.  
  
Usage: `./dconvert.py -f inputfile.txt -o outputfile.rule`  
  
Output Example: `$@$h$e$l$l$o$.$w$o$r$l$d`  
Stripped Example: `@hello.world`  
