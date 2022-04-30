ahorcado_title = """


 .d8b.  db   db  .d88b.  d8888b.  .o88b.  .d8b.  d8888b.  .d88b.  
d8' `8b 88   88 .8P  Y8. 88  `8D d8P  Y8 d8' `8b 88  `8D .8P  Y8. 
88ooo88 88ooo88 88    88 88oobY' 8P      88ooo88 88   88 88    88
88~~~88 88~~~88 88    88 88`8b   8b      88~~~88 88   88 88    88 
88   88 88   88 `8b  d8' 88 `88. Y8b  d8 88   88 88  .8D `8b  d8' 
YP   YP YP   YP  `Y88P'  88   YD  `Y88P' YP   YP Y8888D'  `Y88P'


                             ________
                            /       |
                            |       0     
                            |      /|\\
                            |      / \\
                            |     
                            

"""

ahorcado_0 = """





                            


"""

ahorcado_1 = """
                            
                            
                            
                        
 
                            |
    
                            
"""

ahorcado_2 = """




                            |
                            |


"""

ahorcado_3 = """



                            |
                            |     
                            |     


"""

ahorcado_4 = """


                            |
                            |
                            |     
                            |     


"""

ahorcado_5 = """
                             
                            /       
                            |           
                            |      
                            |      
                            |     


"""

ahorcado_6 = """
                             _
                            /       
                            |           
                            |      
                            |      
                            |     


"""

ahorcado_7 = """
                             __
                            /       
                            |           
                            |      
                            |      
                            |     


"""

ahorcado_8 = """
                             ___
                            /       
                            |           
                            |      
                            |      
                            |     


"""

ahorcado_9 = """
                             ____
                            /       
                            |           
                            |      
                            |      
                            |     


"""

ahorcado_10 = """
                             _____
                            /       
                            |           
                            |      
                            |      
                            |     


"""

ahorcado_11 = """
                             ______
                            /       
                            |           
                            |      
                            |      
                            |     


"""

ahorcado_12 = """
                             _______
                            /       
                            |           
                            |      
                            |      
                            |     


"""

ahorcado_13 = """
                             ________
                            /       
                            |           
                            |      
                            |      
                            |     


"""

ahorcado_14 = """
                             ________
                            /       | 
                            |           
                            |      
                            |      
                            |     


"""

ahorcado_15 = """
                             ________
                            /       | 
                            |       0    
                            |      
                            |      
                            |     


"""

ahorcado_16 = """
                             ________
                            /       |
                            |       0     
                            |       |
                            |      
                            |     


"""

ahorcado_17 = """                 
                             ________
                            /       |
                            |       0     
                            |      /|
                            |     
                            |     


"""

ahorcado_18 = """                 
                             ________
                            /       |
                            |       0     
                            |      /|\\
                            |     
                            |     


"""

ahorcado_19 = """
                             ________
                            /       |
                            |       0     
                            |      /|\\
                            |      / 
                            |     


"""

ahorcado_20 = """
                             ________
                            /       |
                            |       0     
                            |      /|\\
                            |      / \\
                            |     


"""

ahorcado_list = [ahorcado_0, ahorcado_1,
                 ahorcado_2, ahorcado_3,
                 ahorcado_4, ahorcado_5,
                 ahorcado_6, ahorcado_7,
                 ahorcado_8, ahorcado_9,
                 ahorcado_10, ahorcado_11,
                 ahorcado_12, ahorcado_13,
                 ahorcado_14, ahorcado_15,
                 ahorcado_16, ahorcado_17,
                 ahorcado_18, ahorcado_19,
                 ahorcado_20]


def ahorcado_display(difficult=1):
    try:
        if difficult == 1:
            return ahorcado_list
        elif difficult == 2:
            return ahorcado_list[::2]
        elif difficult == 3:
            return [*ahorcado_list[::3], ahorcado_list[-1]]
        else:
            raise Exception('El nivel tiene que ser entre 1 y 3')
    except Exception as e:
        print(e)
        return e