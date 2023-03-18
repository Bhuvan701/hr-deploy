
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os
from django.conf import settings
from io import BytesIO
from django.http import HttpResponseRedirect, Http404,FileResponse,HttpResponse

os.chdir(settings.MEDIA_ROOT)
def breakaddress(st):
    f=""
    s=""
    for i in range(len(st)):
        if(i<75):
            f += str(st[i])
        else:
            s+= str(st[i])
    return f,s 

def breakstr(string):
    t = string.split(' ')
    st=""
    ft=""
    for i in range(int(len(t)/2)):
        ft += t[i] 
        ft += " "

    for  i in range(int(len(t)/2),len(t)):
        st +=t[i]
        st+=" "
    return ft,st
def bstr(st,start):
    f=""
    s=""
    start = 30
    t = st.split(' ')
    for i in range(len(t)):
        if(len(t[i])<start):
            f+=t[i]
            f+=" "
        else:
            s+=t[i]
            s+=' '
        start = start-len(t[i])
    return f,s

def create_pdf(context=dict()):
    
    buffer = BytesIO()
    

    c = canvas.Canvas(buffer,pagesize=A4)


    c.drawImage(f'{settings.MEDIA_ROOT}/img/krct.png',50,700,width=300,height=100)
    c.rect(50,600,150,30,fill=0)

    c.drawImage(f'{settings.MEDIA_ROOT}/img/kr.jpg',450,780,width=50,height=50)

    c.drawImage(f'{settings.MEDIA_ROOT}/img/bio.jpg',450,680,width=100,height=50)

    c.drawString(70,610,"Post Applied For")
    c.rect(50,570,150,30,fill=0)
    c.drawString(70,580,"Department")

    c.rect(200,600,200,30,fill=0)
    c.drawString(220,610,context['post_applied'])

    c.rect(200,570,200,30,fill=0)
    c.drawString(210,580,context['dept'])

    c.drawImage(f"{settings.MEDIA_ROOT}/{context['pic']}",450,550,width=100,height=100)

    c.drawString(60,520,"Name")
    c.drawString(130,520,":")
    c.drawString(150,520,context['name'])

    c.drawString(400,520,"DOB")
    c.drawString(430,520,":")
    c.drawString(440,520,context['dob'])

    c.drawString(60,500,"Phone No")
    c.drawString(130,500,":")
    c.drawString(150,500,context['phone'])

    c.drawString(60,480,"Aadhar No")
    c.drawString(130,480,":")
    c.drawString(150,480,context['aadhar'])

    c.drawString(60,460,"Email")
    c.drawString(130,460,":")
    c.drawString(150,460,context['email'])

    c.rect(50,410,100,30,fill=0)
    c.drawString(60,420,"Father's Name")

    c.rect(150,410,160,30,fill=0)
    c.drawString(160,420,context['f_name'])

    c.rect(310,410,100,30,fill=0)
    c.drawString(320,420,"Mother's Name")

    c.rect(410,410,160,30,fill=0)
    c.drawString(420,420,context['m_name'])

    c.rect(50,380,260,30,fill=0)
    c.drawString(60,390,"Family Status (No.of Brothers & Sisters)")

    c.rect(310,380,260,30,fill=0)
    c.drawString(320,390,context['f_status'])

    c.rect(50,290,100,90,fill=0)
    c.drawString(70,350,"Occupation")
    c.drawString(80,330,"Details")

    c.rect(150,350,200,30,fill=0)
    c.drawString(160,360,"a. Father's Occupation")

    c.rect(350,350,220,30,fill=0)
    c.drawString(360,360,context['f_occupation'])

    c.rect(150,320,200,30,fill=0)
    c.drawString(160,330,"a. Mother's Occupation")

    c.rect(350,320,220,30,fill=0)
    c.drawString(360,330,context['m_occupation'])

    c.rect(150,290,200,30,fill=0)
    c.drawString(160,300,"a. Brother's/Sister's Occupation")

    c.rect(350,290,220,30,fill=0)
    c.drawString(360,300,context['b_occupation'])

    c.rect(50,230,100,60,fill=0)
    c.drawString(70,270,"Permanent")
    c.drawString(80,250,"Address")

    f,s=breakaddress(context['address'])
    c.rect(150,230,420,60,fill=0)
    c.drawString(160,270,f)
    c.drawString(160,250,s)

    c.rect(50,200,60,30,fill=0)
    c.drawString(60,210,"Religion")
    c.rect(110,200,70,30,fill=0)
    c.drawString(120,210,context['religion'])


    c.rect(180,200,80,30,fill=0)
    c.drawString(190,210,"Community")
    c.rect(260,200,50,30,fill=0)
    c.drawString(270,210,context['community'])

    c.rect(310,200,100,30,fill=0)
    c.drawString(320,210,"caste/sub-caste")
    c.rect(410,200,160,30,fill=0)
    c.drawString(420,210,context['caste'])

    c.rect(50,170,130,30,fill=0)
    c.drawString(80,180,"Marital Status")
    c.rect(180,170,390,30,fill=0)
    c.drawString(200,180,context['marital_status'])


    c.rect(50,50,100,120,fill=0)
    c.drawString(70,130,"if Married,")
    c.drawString(70,110,"Details of")
    c.drawString(70,90,"spouse")

    c.rect(150,140,90,30,fill=0)
    c.drawString(160,150,"Name")
    c.rect(240,140,330,30,fill=0)
    c.drawString(250,150,context['s_name'])


    c.rect(150,110,90,30,fill=0)
    c.drawString(160,120,"Qualification")
    c.rect(240,110,330,30,fill=0)
    c.drawString(250,120,context['s_qualification'])


    c.rect(150,80,90,30,fill=0)
    c.drawString(160,90,"Occupation")
    c.rect(240,80,330,30,fill=0)
    c.drawString(250,90,context['s_occupation'])

    c.rect(150,50,90,30,fill=0)
    c.drawString(160,60,"No of children")
    c.rect(240,50,330,30,fill=0)
    c.drawString(250,60,context['no_of_child'])

    c.showPage()

    c.rect(50,780,510,30,fill=0)
    c.drawString(240,790,'Educational Qualification')

    c.rect(50,740,60,40,fill=0)
    c.drawString(60,760,'Details')


    c.rect(110,740,80,40,fill=0)
    c.drawString(115,760,'Specialization')

    c.rect(190,740,150,40,fill=0)
    c.drawString(200,760,'Name of the institution')

    c.rect(340,740,90,40,fill=0)
    c.drawString(344,760,'Name of the')
    c.drawString(345,745,'place')

    c.rect(430,740,60,40,fill=0)
    c.drawString(435,760,'year of')
    c.drawString(440,745,'passing')

    c.rect(490,740,70,40,fill=0)
    c.drawString(495,760,'% of marks')
    c.drawString(500,745,'obtained')

    
    c.rect(50,710,60,30,fill=0)
    c.drawString(60,720,'X std')

    c.setFont('Helvetica-Bold',8)
    f,s=breakstr(context['tenth_spec'])
    c.rect(110,710,80,30,fill=0)
    c.drawString(115,725,f)
    c.drawString(115,715,s)

    f,s=bstr(context['tenth_inst'],30)
    c.rect(190,710,150,30,fill=0)
    c.drawString(200,725,f)
    c.drawString(200,715,s)
    
    c.rect(340,710,90,30,fill=0)
    c.drawString(344,720,context['tenth_place'])

    c.setFont('Helvetica',12)

    c.rect(430,710,60,30,fill=0)
    c.drawString(440,720,context['tenth_yop'])

    c.rect(490,710,70,30,fill=0)
    c.drawString(500,720,context['tenth_per'])


    c.rect(50,680,60,30,fill=0)
    c.drawString(60,690,'XII std')

    c.setFont('Helvetica-Bold',8)
    f,s=breakstr(context['twelvth_spec'])
    c.rect(110,680,80,30,fill=0)
    c.drawString(115,695,f)
    c.drawString(115,685,s)
    f,s=bstr(context['twelvth_inst'],30)
    c.rect(190,680,150,30,fill=0)
    c.drawString(200,695,f)
    c.drawString(200,685,s)

    c.rect(340,680,90,30,fill=0)
    c.drawString(344,690,context['twelvth_place'])

    c.setFont('Helvetica',12)

    c.rect(430,680,60,30,fill=0)
    c.drawString(440,690,context['twelvth_yop'])

    c.rect(490,680,70,30,fill=0)
    c.drawString(500,690,context['twelvth_per'])

    c.rect(50,650,60,30,fill=0)
    c.drawString(60,660,'Diplamo')

    c.setFont('Helvetica-Bold',8)

    f,s=breakstr(context['diplamo_spec'])
    c.rect(110,650,80,30,fill=0)
    c.drawString(115,665,f)
    c.drawString(115,655,s)
    
    f,s=bstr(context['diplamo_inst'],30)
    c.rect(190,650,150,30,fill=0)
    c.drawString(200,665,f)
    c.drawString(200,655,s)

    c.rect(340,650,90,30,fill=0)
    c.drawString(344,660,context['diplamo_place'])

    c.setFont('Helvetica',12)

    c.rect(430,650,60,30,fill=0)
    c.drawString(440,660,context['diplamo_yop'])

    c.rect(490,650,70,30,fill=0)
    c.drawString(500,660,context['diplamo_per'])


    c.rect(50,620,60,30,fill=0)
    c.drawString(60,630,'UG')
    
    c.setFont('Helvetica-Bold',8)

    f,s=breakstr(context['ug_spec'])
    c.rect(110,620,80,30,fill=0)
    c.drawString(115,635,f)
    c.drawString(115,625,s)

    f,s=bstr(context['ug_inst'],30)
    c.rect(190,620,150,30,fill=0)
    c.drawString(200,635,f)
    c.drawString(200,625,s)

    c.rect(340,620,90,30,fill=0)
    c.drawString(344,630,context['ug_place'])

    c.setFont('Helvetica',12)

    c.rect(430,620,60,30,fill=0)
    c.drawString(440,630,context['ug_yop'])

    c.rect(490,620,70,30,fill=0)
    c.drawString(500,630,context['ug_per'])


    c.rect(50,590,60,30,fill=0)
    c.drawString(60,600,'PG')

    c.setFont('Helvetica-Bold',8)

    f,s=breakstr(context['pg_spec'])
    c.rect(110,590,80,30,fill=0)
    c.drawString(115,605,f)
    c.drawString(115,595,s)

    f,s=bstr(context['pg_inst'],30)
    c.rect(190,590,150,30,fill=0)
    c.drawString(200,605,f)
    c.drawString(200,595,s)

    c.rect(340,590,90,30,fill=0)
    c.drawString(344,600,context['pg_place'])

    c.setFont('Helvetica',12)

    c.rect(430,590,60,30,fill=0)
    c.drawString(440,600,context['pg_yop'])

    c.rect(490,590,70,30,fill=0)
    c.drawString(500,600,context['pg_per'])


    c.rect(50,560,60,30,fill=0)
    c.drawString(60,570,'M.phil')

    c.setFont('Helvetica-Bold',8)

    f,s=breakstr(context['mphil_spec'])
    c.rect(110,560,80,30,fill=0)
    
    c.drawString(115,575,f)
    c.drawString(115,565,s)

    f,s=bstr(context['mphil_inst'],30)
    c.rect(190,560,150,30,fill=0)
    c.drawString(200,575,f)
    c.drawString(200,565,s)

    c.rect(340,560,90,30,fill=0)
    c.drawString(344,570,context['mphil_place'])

    c.setFont('Helvetica',12)

    c.rect(430,560,60,30,fill=0)
    c.drawString(440,570,context['mphil_yop'])

    c.rect(490,560,70,30,fill=0)
    c.drawString(500,570,context['mphil_per'])


    c.rect(50,530,60,30,fill=0)
    c.drawString(60,540,'PhD')

    c.setFont('Helvetica-Bold',8)

    f,s=breakstr(context['phd_spec'])
    c.rect(110,530,80,30,fill=0)
    c.drawString(115,545,f)
    c.drawString(115,535,s)

    f,s=bstr(context['phd_inst'],30)
    c.rect(190,530,150,30,fill=0)
    c.drawString(200,545,f)
    c.drawString(200,535,s)

    c.rect(340,530,90,30,fill=0)
    c.drawString(344,540,context['phd_place'])

    c.setFont('Helvetica',12)

    c.rect(430,530,60,30,fill=0)
    c.drawString(440,540,context['phd_yop'])

    c.rect(490,530,70,30,fill=0)
    c.drawString(500,540,context['phd_per'])

    c.rect(50,500,60,30,fill=0)

    c.rect(110,500,80,30,fill=0)
    c.drawString(115,510,'with age')

    c.rect(110,500,450,30,fill=0)

    c.setFont('Helvetica',12)
    c.drawString(50,450,'Aditional Qualification if any')
    c.drawString(230,450,':')
    c.drawString(255,450,context['addon_qual'])


    c.drawString(50,420,'Previous Experience')
    c.drawString(230,420,':')

    c.rect(255,415,30,20,fill=0)
    c.drawString(260,420,'UG')
    c.rect(285,415,30,20,fill=0)
    c.drawString(295,420,context['ug_exp'])

    c.rect(325,415,30,20,fill=0)
    c.drawString(330,420,'PG')
    c.rect(355,415,30,20,fill=0)
    c.drawString(360,420,context['pg_exp'])

    c.rect(395,415,30,20,fill=0)
    c.drawString(400,420,'phD')
    c.rect(425,415,30,20,fill=0)
    c.drawString(435,420,context['phd_exp'])

    c.rect(465,415,40,20,fill=0)
    c.drawString(470,420,'Total')
    c.rect(505,415,30,20,fill=0)
    c.drawString(515,420,context['total_exp'])

    c.drawString(50,390,'Salary Expected')
    c.drawString(230,390,':')
    c.drawString(255,390,context['salary'])
    
    c.setFont('Helvetica-Bold',12)
    c.drawString(50,360,'Terms and Conditions : ')
    c.setFont('Helvetica',12)
    c.drawString(80,330,'1.')

    c.drawString(100,330,'Minimum of 2 years stay in the college is expected. However they can be relieved ')
    c.drawString(100,310,'immediately for Govt job if they submit proof .')

    c.drawString(80,280,'2.')
    c.drawString(100,280,'If you resign in the middle of the academic year, ypu have to pay 3 months salary.')

    c.setFont('Helvetica-Bold',12)
    c.drawString(50,250,'Additional Terms and Conditions for phD Holders : ')
    c.setFont('Helvetica',12)

    c.drawString(80,220,'1.')
    c.drawString(100,220,'Minimum one patent to be filed every year')

    c.drawString(80,190,'2.')
    c.drawString(100,190,'Minimum two papers are to be published every year in SCI/SCIE indexed journals')

    c.drawString(80,160,'3.')
    c.drawString(100,160,'Minimum three proposals seeking financial assistants are to be submitted every year to')
    c.drawString(100,145,'funding agencies and atleast one of the proposals shall be taken to the level of')
    c.drawString(100,130,'presentation. A revenue of Rs. 50,000 shall be generated through consultancy,')
    c.drawString(100,115,'if no funding proposal reaches the level of presentation.')
    c.drawString(50,50,'Date : ')
    c.drawString(75,50,'')

    c.drawString(400,50,'Signature of the candidate')

    c.save()

    pdf = buffer.getvalue()
    buffer.close()
    #response.write(pdf)
    return HttpResponse(pdf, content_type='application/pdf')

