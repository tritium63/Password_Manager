class wiSet():
    def __init__(self):
        self.wiList = []
    def addWi(self,widget):
        for i in self.wiList:
            if i[0]==widget:
                raise Exception(f"the widget alredy exists in {self},\n you can just place,pack or grid it")
        self.wiList.append([widget,lambda : print(),lambda :print ()])
        return widget

    def place(self,wi,**kwargs):
        for i in self.wiList:
            if wi==i[0]:
                i[1]=lambda :wi.place(**kwargs)
                i[2]=lambda :wi.place_forget()
    
    def pack(self,wi,**kwargs):
        for i in self.wiList:
            if wi==i[0]:
                i[1]=lambda :wi.pack(**kwargs)
                i[2]=lambda :wi.pack_forget()

    def grid(self,wi,**kwargs):
        for i in self.wiList:
            if wi==i[0]:
                i[1]=lambda :wi.grid(**kwargs)
                i[2]=lambda :wi.grid_forget()
    def create(self):
        for i in self.wiList:
            i[1]()
    def dest(self):
        for i in self.wiList:
            i[2]()

def switch(a,b):
    a.dest()
    b.create()
