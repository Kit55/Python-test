class Observable():
    def __init__(self,kwargs):
        self.__dict__=dict(self.__class__.__dict__,**kwargs)#обновление __dict__
    def __str__(self):#при обращении к экзепляру как к строке
        s=self.__class__.__name__+('( ')
        for i in self.__dict__:
            if not i.startswith('_'):
                s+=str(i)+'='+str(self.__dict__[i])+' '
        s+=')'      
        return s

class X(Observable): 
    """
    x=X({'foo':1, 'bar':5, '_bazz':12, 'name':'Amok', 'props':('One', 'two')})

    >>> print (x)
    X( name=Amok foo=1 bar=5 props=('One', 'two') )

    >>> print (x.foo)
    1

    >>> print (x.name)
    Amok

    >>> print (x._bazz)
    12
    """
    pass
    
x=X({'foo':1, 'bar':5, '_bazz':12, 'name':'Amok', 'props':('One', 'two')})#В Python для обозначения protected атрибутов используют "_", для private — "__" перед названием переменной. 
print (x)
print (x.foo)
print (x.name)
print (x._bazz)

if __name__ == "__main__":
    import doctest
    doctest.testmod()