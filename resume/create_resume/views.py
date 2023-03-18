from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .models import profile,staff,jobvacancy,journal_publication,conference,patent,Rejected
from django.core.files import File
from io import BytesIO,StringIO
from django.contrib import messages
import os
from django.http import HttpResponseRedirect, Http404,FileResponse,HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from .task2 import send_email
from .tasks import send_email
from .report import create_pdf
from datetime import datetime

context = dict()
jobpost = dict()
def home(request):
	global jobpost
	if request.method =='POST':
		if 'apply' in request.POST:
			jobpost={}
			return redirect('accept')
		if 'avail' in request.POST:
			return redirect('available')
	return render(request,'create_resume/homepage.html')


def getInput(request):
	global context
	if request.method == 'POST':
		if 'submit' in request.POST:
			pic = request.FILES['pic']
			fs = FileSystemStorage()
			img = pic.name.replace(' ','_')
			if(not os.path.exists(f'{settings.MEDIA_ROOT}/{img}')):
				fs.save(img, pic)
			context = {
				'post_applied' : request.POST['post_applied'],
				'dob' : request.POST['dob'],
						'dept' : request.POST['dept'],
						'name'  :request.POST['name'],
						'email' :request.POST['email'],
						'phone' :request.POST['phone'],
						'aadhar':request.POST['aadhar'],
						'f_name' :request.POST['f_name'],
						'm_name' : request.POST['m_name'],
						'f_status' : request.POST['f_status'],
						'f_occupation':request.POST['f_occupation'],
						'm_occupation':request.POST['m_occupation'],
						'b_occupation':request.POST['b_occupation'],
						'address':request.POST['address'],
						'religion':request.POST['religion'],
						'community':request.POST['community'],
						'caste' :request.POST['caste'],
						'marital_status':request.POST['marital_status'],
						's_name' : request.POST['s_name'],
						's_qualification' : request.POST['s_qual'],
						'no_of_child' : request.POST['no_of_child'],
						's_occupation':request.POST['s_occupation'],
						'tenth_spec':request.POST['tenth_spec'],
						'tenth_inst':request.POST['tenth_inst'],
						'tenth_place':request.POST['tenth_place'],
						'tenth_yop':request.POST['tenth_yop'],
						'tenth_per':request.POST['tenth_per'],
						'twelvth_spec':request.POST['twelvth_spec'],
						'twelvth_inst':request.POST['twelvth_inst'],
						'twelvth_place':request.POST['twelvth_place'],
						'twelvth_yop':request.POST['twelvth_yop'],
						'twelvth_per':request.POST['twelvth_per'],
						'diplamo_spec':request.POST['diplamo_spec'],
						'diplamo_inst':request.POST['diplamo_inst'],
						'diplamo_place':request.POST['diplamo_place'],
						'diplamo_yop':request.POST['diplamo_yop'],
						'diplamo_per':request.POST['diplamo_per'],
						'ug_spec':request.POST['ug_spec'],
						'ug_inst':request.POST['ug_inst'],
						'ug_place':request.POST['ug_place'],
						'ug_yop':request.POST['ug_yop'],
						'ug_per':request.POST['ug_per'],
						'pg_spec':request.POST['pg_spec'],
						'pg_inst':request.POST['pg_inst'],
						'pg_place':request.POST['pg_place'],
						'pg_yop':request.POST['pg_yop'],
						'pg_per':request.POST['pg_per'],
						'mphil_spec':request.POST['mphil_spec'],
						'mphil_inst':request.POST['mphil_inst'],
						'mphil_place':request.POST['mphil_place'],
						'mphil_yop':request.POST['mphil_yop'],
						'mphil_per':request.POST['mphil_per'],
						'phd_spec':request.POST['phd_spec'],
						'phd_inst':request.POST['phd_inst'],
						'phd_place':request.POST['phd_place'],
						'phd_yop':request.POST['phd_yop'],
						'phd_per':request.POST['phd_per'],
						'addon_qual':request.POST['addon_qual'],
						'ug_exp':request.POST['ug_exp'],
						'pg_exp':request.POST['pg_exp'],
						'phd_exp':request.POST['phd_exp'],
						'total_exp':request.POST['total_exp'],
						'salary':request.POST['salary'],
						'pic' : img,
						'journal_author' : request.POST.getlist('j_author'),
						'journal_title' : request.POST.getlist('j_title'),
						'journal_name' : request.POST.getlist('j_name'),
						
						'conference_author' : request.POST.getlist('c_author'),
						'conference_title' : request.POST.getlist('c_title'),
						'conference_name' : request.POST.getlist('c_name'),
						
						'patent_author' : request.POST.getlist('p_author'),
						'patent_title' : request.POST.getlist('p_title'),
						'patent_status' : request.POST.getlist('p_status'),
			}
			return convertInputIntoPdf(request)
	return render(request,'create_resume/index.html',{'p':jobpost})


def convertInputIntoPdf(request):
		pdf = create_pdf(context)
		if(not (profile.objects.filter(aadhar=context['aadhar']).exists() and Rejected.objects.filter(aadhar=context['aadhar']).exists())):
			p = profile.objects.create(name=context['name'],email=context['email'],phone=context['phone'],
			department=context['dept'],aadhar=context['aadhar'])
			for i in range(len(context['journal_author'])):
				journal_publication.objects.create(name=p,author=context['journal_author'][i],title=context['journal_title'][i],journal_name=context['journal_name'][i])

			for i in range(len(context['conference_author'])):
				conference.objects.create(name=p,author=context['conference_author'][i],title=context['conference_title'][i],conference_name=context['conference_name'][i])
			
			for i in range(len(context['patent_author'])):
				patent.objects.create(name=p,author=context['patent_author'][i],title=context['patent_title'][i],status=context['patent_status'][i])
			
			p.resume.save(f"{context['aadhar']}.pdf", File(BytesIO(pdf.content)))
			os.remove(os.path.join(settings.MEDIA_ROOT,context['pic']))
			messages.success(request,'applied successflly')
			return redirect('home')
		else:
			messages.error(request,'Already Applied')
			return redirect('home')
		return redirect(home)


@login_required
def viewIndividualPdf(request,name):
	try:
		p = profile.objects.filter(aadhar=name).first()
		if(request.user.username != 'hr@krct.ac.in'):
			p.viewed = True
			p.save()
		filepath = os.path.join(settings.MEDIA_ROOT,p.resume.name)
		return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
	except:
		return render(request,'create_resume/pages-error.html')


'''@login_required(login_url='/login/')
def viewAllPdf(request):
	#print(request.user)
	try:
		if request.method == 'POST':
			if 'del' in request.POST:
				name = request.POST['del']
				p = profile.objects.filter(name = name).first()
				os.remove(os.path.join(settings.MEDIA_ROOT,p.resume.name))
				p.delete()
				messages.success(request,'deleted')
			elif 'select' in request.POST:
				send_email.delay(request.POST['select'])
				p = profile.objects.filter(name = request.POST['select']).first()
				p.short_listed = True
				p.save()
				
		if(request.user.username == 'admin'):
			p = profile.objects.all()
			return render(request,'create_resume/viewpdf.html',{'context':p})
		elif(request.user.staff.department == 'HR'):
			p = profile.objects.all()
			return render(request,'create_resume/hr.html',{'context':p})
		else:
			p=profile.objects.filter(department=request.user.staff.department)
			return render(request,'create_resume/app.html',{'context':p})
	except:
		return render(request,'create_resume/pages-error.html')
'''
def viewAllPdf(request):
	if request.method == 'POST':
		if 'del' in request.POST:
			aadhar = request.POST['del']
			p = profile.objects.filter(aadhar = aadhar).first()
			os.remove(os.path.join(settings.MEDIA_ROOT,p.resume.name))
			p.delete()
			Rejected.objects.create(aadhar=aadhar)
			messages.success(request,'deleted')
		elif 'select' in request.POST:
			send_email(request.POST['select'])
			p = profile.objects.filter(aadhar = request.POST['select']).first()
			p.short_listed = True
			p.save()
	if(request.user.username == 'rnd@krct.ac.in'):
		return redirect('rnd')
	if(request.user.username == 'admin'):
		p = profile.objects.all()
		return render(request,'create_resume/app.html',{'context':p})
	elif(request.user.staff.department == 'HR'):
		p = profile.objects.all()
		return render(request,'create_resume/hr.html',{'context':p})
	else:
		p=profile.objects.filter(department=request.user.staff.department)
		return render(request,'create_resume/app.html',{'context':p})
	return render(request,'create_resume/app.html')

def loginuser(request):
	try:
		if request.method == 'POST':
			uname = request.POST['username']
			upass = request.POST['password'] 
			user = authenticate(request,username=uname,password=upass)
			if user is not None:
				login(request,user)
				messages.success(request, 'Login successful')
				return redirect('viewpdf')
			else:
				messages.error(request, 'invalid username or password')
				return redirect('login')
		else:
			return render(request,'create_resume/login.html')
	except:
		return render(request,'create_resume/pages-error.html')

def custom_logout(request):
    logout(request)
    return redirect("home")


def viewshortlisted(request):
	user = request.user
	if user.username == 'hr@krct.ac.in':
		p = profile.objects.filter(short_listed=True)
		return render(request,'create_resume/shortlisted.html',{'context':p})
	else:
		p = profile.objects.filter(department=user.staff.department,short_listed=True)
		return render(request,'create_resume/shortlisted.html',{'context':p})

def vacancy(request):
	if request.method == 'POST':
		dept = request.POST['dept']
		role = request.POST['post_applied']
		n    = request.POST['vacancy']
		jobvacancy.objects.create(dept=dept,role=role,noofvacancy=n)
		messages.success(request,'post added')
		return redirect('a')
	return render(request,'create_resume/addvacancy.html')

def available(request):
	global jobpost
	if request.method =='POST':
		v = request.POST['apply']
		role = v.split(',')[1]
		dept = v.split(',')[0]
		jobpost = {
		'role':role,
		'dept':dept,
		}
		return redirect('accept')
	p = jobvacancy.objects.all()
	return render(request,'create_resume/vag.html',{'p':p})

def hrdelete(request):
	if request.method == 'POST':
		i = request.POST['delete']
		print(i)
		j = jobvacancy.objects.filter(id=i).first().delete()
		print(j)
	p = jobvacancy.objects.all()
	return render(request,'create_resume/hrdelete.html',{'p':p})

def rnd(request):
	if request.method =='POST':
		if 'verify' in request.POST:
			p=profile.objects.filter(aadhar=request.POST['verify']).first()
			p.verified=True
			print(p.verified)
			p.save()
	p = profile.objects.filter(short_listed=True)
	return render(request,'create_resume/rnd.html',{'context':p})

def viewresearch(request,name):
	
		if request.method == 'POST':
			if 'indexed' in request.POST:
				i = journal_publication.objects.filter(id=request.POST['indexed']).first()
				i.indexed = True
				i.unindexed = False
				i.save()
			if 'unindexed' in request.POST:
				i = journal_publication.objects.filter(id=request.POST['unindexed']).first()
				i.indexed = False
				i.unindexed = True
				i.save()
		p = profile.objects.filter(aadhar=name).first()
		j = journal_publication.objects.filter(name=p)
		c = conference.objects.filter(name=p)
		pt = patent.objects.filter(name=p)
		return render(request,'create_resume/viewauthors.html',{'journal':j,'conference':c,'patent':pt})

def verified(request):
	if request.method=='POST':
		if 'approve' in request.POST:
			p = profile.objects.filter(aadhar=request.POST['approve']).first()
			p.forward = True
			p.save()
	p = profile.objects.filter(verified=True,department=request.user.staff.department)
	return render(request,'create_resume/verified.html',{'context':p})

def appointed(request):
	if request.method=="POST":
		if 'appoint' in request.POST:
			pr = profile.objects.filter(aadhar=request.POST['appoint']).first()
			pr.approved = True
			pr.appointed_date = datetime.now()
			pr.save()
	p = profile.objects.filter(forward=True)
	return render(request,'create_resume/appointed.html',{'context':p})

def viewresearch2(request,aadhar):
	p = profile.objects.filter(aadhar=aadhar).first()
	j = journal_publication.objects.filter(name=p)
	c = conference.objects.filter(name=p)
	pt = patent.objects.filter(name=p)
	return render(request,'create_resume/viewauthors2.html',{'journal':j,'conference':c,'patent':pt})
