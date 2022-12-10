
Algorithm USed: Histogram based gradient boosting regression tree

Following Assumptions Considered:

REGION_TYPE = RURAL(0), URBAN(1)

GENDER = M(0), F(1)   

EDUCATION = 10th Std and below (0),
            Post Graduate (1)       
            Graduate (2)             
            12th Std. Pass (3)  

OCCUPATION = Subsistence crop farmers (Small crop farmers)   (0)                                                   
             Smaller businessmen (smaller shops or offices), Shopkeepers, small dhaba owners (1)   
             Mazdoor/Helpers  (2)                                                                                    
             Agricultural labourers/Plantation workers  (3)                                                         
             (Organised crop farmers) Crop cultivators, vegetable cultivators, fruit growers, Floriculturists (4)
             Accountants and auditors  (5)                                                                         
             Other health related workers (anganwadi workers & helpers)  (6)                                
             Private teachers for school children, Tuition teachers  (7)                                  
             Masons (Mistri), Brick layers  (8)                                                                
             Auto rickshaw drivers  (9)                                                                          
             Stone cutters  (10)                                                                                 
             Industrial and machine workers  (11)                                                                 
             University or college teachers  (12)                                                                 
             Sales representatives, sales executives, Store Managers (13)                                     
             Home Makers  (14)                                                                                   
             Bus/Car and Van drivers (15)                                                                        
             School teachers  (16)                                                                              
             Engineers  (17)                                                                                     
             Tailors, Dressmakers, Dress designers  (18)  

MARITAL_STATUS = Married (0)
                 Unmarried (1)
                 Widowed (2)

API CALL:

curl --location --request POST 'http://127.0.0.1:5000/income-predict' \
--form 'REGION_TYPE="0"' \
--form 'GENDER="1"' \
--form 'AGE="53"' \
--form 'EDUCATION="0"' \
--form 'OCCUPATION="0"' \
--form 'MARITAL_STATUS="0"'

