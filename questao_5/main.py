from classes import tree

BANNER = '''
       ###        
      #o###       
    #####o###     
   #o#\#|#/###    
    ###\|/#o#     
     # }|{  #     
       }|{        '''


def main():
    print(BANNER)

    raiz = tree.Tree(9, 5, 1)
    print(f"{raiz.__str__()}")


if __name__ == "__main__":
    main()
