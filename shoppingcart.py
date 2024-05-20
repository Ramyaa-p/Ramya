class shopping_cart():
    shopname:'Flipcart'
    location:'all over india'
    items={'mobile':[10,20000],'watch':[7,2500],'tv':[30,50000]}
    
    def __init__(self,name,phno,location,cart):
        self.name=name
        self.phno=phno
        self.location=location
        self.cart=cart

        
    @classmethod    
    def product_detail(cls):
        
        print('products are available!!!')
        print('------------------------')
        print('product qty     price')
        print('------------------------')
        for product in cls.items:
            print(product,cls.items[product][0],cls.items[product][1],sep='\t')
       
          
       
        
    def customer(self):

        
        print('This is your Details!!')
        print('----------------------------------')
        print(f'NAME:{self.name}')
        print(f'PHNO:{self.phno}')
        print(f'LOCATION:{self.location}')
        print(f'CART:{self.cart}')
        print('----------------------------------')
        
    def add_product(self):
        
       print('Add your product into your cart :)') 
       print('----------------------------------')
       product_name=input('ENTER YOUR PRODUCT:')
       if product_name in shopping_cart.items:
           
           qty=int(input('Enter your quantity:'))
           
           if qty <= shopping_cart.items[product_name][0]:
               self.cart[product_name]=qty
               shopping_cart.items[product_name][0] -=qty
           else:
               print(f'This is only available  {shopping_cart.items[product_name][0]}')
       
       else:
           print(f'sry this    {product_name}    item not available')

           
    def remove_product(self):
        
        print('Remove your product from your cart ;)') 
        print('----------------------------------')
        remove_product=input('enter your product name:')
        if remove_product in self.cart:
            qty=int(input('enter your quantity:'))
            if qty < self.cart[remove_product]:
                self.cart[remove_product]-=qty
            else:        
                self.cart.pop(remove_product)
      
        else:
           print('This item not in your cart')
           
    def Exit(self):
        
        print('THANKS FOR YOUR SHOPPING \n COME AGAIN!!!')
        
      
        
        
    def frontpage(self):
        
        print('Enter 1 display all the product')
        print('Enter 2 display your details')
        print('Enter 3 to add a product into the cart')
        print('Enter 4 remove product from your cart')
        print('Enter 5 is Exit')
       
        choice=int(input('ENTER YOUR CHOICE!!:'))
        print('----------------------------------')
        if choice==1:
            s1.product_detail()
            print('----------------------------------')
            s1.frontpage()
        
        if choice==2:
                    s1.customer()
                    s1.frontpage()
        if choice==3:
                    s1.add_product()
                    print('----------------------------------')
                    s1.frontpage()
                
        if choice==4:
                    s1.remove_product()
                    print('----------------------------------')
                    s1.frontpage()
                
        if choice==5:
                    s1.Exit()
            
        
                           






        

                   
s1=shopping_cart('Ramya',23456789109,'chennai',{})
s1.frontpage()











