import originpro as op
import numbers

def chara(x):#function to get the origin column position based on a integer
        if (x<26):
            b=chr(65+x)
            d=b
        if (x>=26) and (x<=51):
            a='A'
            b=chr(65+x-26)
            d=a+b
        if (x>=52) and (x<=77):
            a='B'
            b=chr(65+x-52)
            d=a+b
        if (x>=78) and (x<=103):
            a='C'
            b=chr(65+x-78)
            d=a+b
        if (x>=104) and (x<=129):
            a='D'
            b=chr(65+x-104)
            d=a+b
        if (x>=130) and (x<=155):
            a='E'
            b=chr(65+x-130)
            d=a+b
        if (x>=156) and (x<=181):
            a='F'
            b=chr(65+x-156)
            d=a+b
        if (x>=182) and (x<=210):
            a='G'
            b=chr(65+x-182)
            d=a+b
        return d
        
wks = op.find_sheet() #Loads worksheet into a variable
df = wks.to_df(head='SourceFile') #Creates a dataframe out of the worksheet

df.columns = df.columns.str.split("_").str[0] #Change the name of the column, removing the number of the file (for instance, 001,002,003,004,005)

df1 = df.groupby(by=df.columns, axis=1).apply(lambda g: g.mean(axis=1) if isinstance(g.iloc[0,0], numbers.Number) else g.iloc[:,0])
for column in df1.columns:
    df1[column + '_x'] = 0.12    
    df1.rename(columns = {column:column+'_y'}, inplace = True)
    
sort_key = lambda s: (len(s), s)
df1 = df1[sorted(df1.columns,key=sort_key)]
 
wks2 = wks.get_book().add_sheet('Result_BE_correction')
wks2.from_df(df1,head='SourceFile')
wks2.cols_axis('xy',0,-1, True)

wks4= wks.get_book().add_sheet('Result_intensity_correction',False)

c= wks2.cols  #calculate number of columns of the worksheet
 #create variables with preset values for each parameter
print(c)
data2= [None] * (c // 2)
data3= [100] * (c // 2)
data4= [400] * (c // 2)
data5= [720] * (c // 2)
data6= [3] * (c // 2)
data7= [29] * (c // 2)
data8= [36] * (c // 2)
data9= [25] * (c // 2)
data10=[0.00] * (c // 2)
data11=[1] * (c // 2)
data12=[42] * (c // 2)
data13=[55] * (c // 2)
data14=[1] * (c // 2)

i=0		
for x in range(0, c):
    if x % 2 == 0: 
        b=chara(x)
        a_string = wks2.get_label(b,'SourceFile')
        split_string = a_string.split("_", 1)
        data2[i] = split_string[0]
        i=i+1
wks3 = wks.get_book().add_sheet('Parameters',False)
wks3.from_list(0, data2)
wks3.from_list(1, data3)
wks3.from_list(2, data4)
wks3.from_list(3, data5)
wks3.from_list(4, data6)
wks3.from_list(5, data7)
wks3.from_list(6, data8)
wks3.from_list(7, data9)
wks3.from_list(8, data10)
wks3.from_list(9, data11)
wks3.from_list(10, data12)
wks3.from_list(11, data13)
wks3.from_list(12, data14)
wks3.set_labels(['Filename', 'ug','Photon Energy(eV)', 'e-beam', 'Work Function of e-Gun','Pixel/eV (Alpha)','Pixel/eV (Beta)','Pixel/eV (Gamma)','Correction offset','time(s)','w1','w2','Activate ug correct.'], 'L')

j=1	

for x in range(0, c):  #Loop to add specific formula, correcting the binding energy axis for different files, and core levels
    if x % 2 == 0: 
        b=chara(x)
        pb = 'Parameters!B'+str(j)
        pc = 'Parameters!C'+str(j)
        pd = 'Parameters!D'+str(j)
        pe = 'Parameters!E'+str(j)
        pf = 'Parameters!F'+str(j)
        pg = 'Parameters!G'+str(j)
        ph = 'Parameters!H'+str(j)
        pi = 'Parameters!I'+str(j)
        pm = 'Parameters!M'+str(j)
        s = str(j)
        formula='ifs('+pm+'=1&&'+pb+'<50,('+pi+')+('+pc+')-('+pe+')-('+pb+'+0.055)+ (((i-1)-('+pd+'))/('+pf+')) - ((((i-1)-('+pd+'))/(('+pf+')*('+pg+')))^2)  - ((((i-1)-('+pd+'))/(('+pf+')*('+ph+')))^3),'+pm+'=1&&'+pb+'>=50&&'+pb+'<370,('+pi+')+('+pc+')-('+pe+')-('+pb+'+0.0012*'+pb+')+ (((i-1)-('+pd+'))/('+pf+')) - ((((i-1)-('+pd+'))/(('+pf+')*('+pg+')))^2)  - ((((i-1)-('+pd+'))/(('+pf+')*('+ph+')))^3) ,'+pm+'=1&&'+pb+'>=370,('+pi+')+('+pc+')-('+pe+')- (('+pb+')+ 0.1 +('+pb+'*0.00097))+ (((i-1)-('+pd+'))/('+pf+')) - ((((i-1)-('+pd+'))/(('+pf+')*('+pg+')))^2)  - ((((i-1)-('+pd+'))/(('+pf+')*('+ph+')))^3) ,'+pm+'=0,('+pi+')+('+pc+')-('+pe+')- ('+pb+')+ (((i-1)-('+pd+'))/('+pf+')) - ((((i-1)-('+pd+'))/(('+pf+')*('+pg+')))^2)  - ((((i-1)-('+pd+'))/(('+pf+')*('+ph+')))^3))'
        wks2.set_formula(b,formula)
        j=j+1
wks4.from_df(df1,head='SourceFile') 
wks4.cols_axis('xy',0,-1, True)

j=1
for x in range(0, c): #Loop to add specific formula, correcting the intensity axis for different files, and core levels
    b=chara(x)
    if x % 2 == 0:
        formula='Result_BE_correction!'+b       
    else:
        formula='(Result_BE_correction!'+b+ '/(Parameters!J'+str(j//2)+'))* (exp(((((i-1)-(Parameters!D'+str(j//2)+'))/((Parameters!F'+str(j//2)+')*(Parameters!K'+str(j//2)+')))^2)-((((i-1)-(Parameters!D'+str(j//2)+'))/((Parameters!F'+str(j//2)+')*(Parameters!L'+str(j//2)+')))^4)))'
        photon='=Parameters!C'+str(j//2)
        ug='=Parameters!B'+str(j//2)
        wks4.set_label(b,photon,type = 'Photon energy (eV)' )
        wks4.set_label(b,ug,type = 'ug (eV)' )
    wks4.set_formula(b,formula)  
    j=j+1
  
