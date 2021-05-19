BANNER = '''
       ###        
      #o###       
    #####o###     
   #o#\#|#/###    
    ###\|/#o#     
     # }|{  #     
       }|{        '''

from classes import tree

def main():
    
    print(BANNER)

    raiz = tree.Tree(9, 5, 1)
    print(f"{raiz.__str__()}")
    
    raiz.search_order()

if __name__ == "__main__":    
    main()