import string as st
class Solution:
    def isPalindrome(self,s:str)->bool:
        self.s=s.lower().replace(' ','')
        new_list=[]
        for letter in self.s:
            if letter in st.punctuation:
                continue
            else:
                new_list.append(letter)
        half=len(new_list)//2
        right=new_list[:half]
        left=list(reversed(new_list[half:]))
        if len(new_list)%2==1:
            remo=left.pop()
        if right == left:
            return True 
        else:
            return False 
        

            
                                               
                                                                
                                                                    
                                                                                                                                        
                                                                                                                
                                                                                                                                        
                                                                                                                                                                    
                                                                                                                                                                    
                                                                                                                                            