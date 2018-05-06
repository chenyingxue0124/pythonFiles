def reverseWords(s):
   #t = ""
   #for x in s.split():
      #t = t +" " + x[::-1]
   #return t
      
        
    return " ".join(x[::-1] for x in s.split())
    
print(reverseWords("Let's do it again"))
            
        
        