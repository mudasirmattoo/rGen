from django.shortcuts import redirect, render
from .models import Profile
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfcrowd

# Create your views here.


def form(request):
    
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        linkedin = request.POST.get("linkedin","")
        objective = request.POST.get("objective","")
        work1 = request.POST.get("work1","")
        work1r = request.POST.get("work1r","")
        work1d = request.POST.get("work1d","")
        work2 = request.POST.get("work2","")
        work2r = request.POST.get("work2r","")
        work2d = request.POST.get("work2d","")
        work3 = request.POST.get("work3","")
        work3r = request.POST.get("work3r","")
        work3d = request.POST.get("work3d","")
        college = request.POST.get("college","")
        degree = request.POST.get("degree","")
        cgpa = request.POST.get("cgpa","")
        higher = request.POST.get("higher","")
        higherp = request.POST.get("higherp","")
        high = request.POST.get("high","")
        highp = request.POST.get("highp","")
        proj1 = request.POST.get("proj1","")
        proj1d = request.POST.get("proj1d","")
        proj2 = request.POST.get("proj2","")
        proj2d = request.POST.get("proj2d","")
        proj3 = request.POST.get("proj3","")
        proj3d = request.POST.get("proj3d","")
        cert1 = request.POST.get("cert1","")
        cert2 = request.POST.get("cert2","")
        skills = request.POST.get("skills","")
        ach1 = request.POST.get("ach1","")
        ach2 = request.POST.get("ach2","")

        profile = Profile(name=name,email=email,phone=phone,linkedin=linkedin,objective=objective,work1=work1,work1r=work1r,work1d=work1d,work2=work2,work2r=work2r,work2d=work2d,work3=work3,work3r=work3r,work3d=work3d,college=college,degree=degree,cgpa=cgpa,higher=higher,higherp=higherp,high=high,highp=highp,proj1=proj1,proj1d=proj1d,proj2=proj2,proj2d=proj2d,proj3=proj3,proj3d=proj3d,cert1=cert1,cert2=cert2,skills=skills,ach1=ach1,ach2=ach2)
        profile.save()  
        
        return redirect('download', id=profile.id)
    return render(request,'resume/form.html')


# def pdf(request,id):
#     user_profile = Profile.objects.get(pk=id)
#     template = loader.get_template('resume/pdf.html')
#     html = template.render({'user_profile':user_profile})
#     # css_path = request.build_absolute_uri("{% static 'resume/mycss.css' %}")

#     options = {
#         'page-size': 'A4',
#         'encoding': "UTF-8",
#         'margin-top': '10mm',
#         'margin-bottom': '10mm',
#         'margin-left': '10mm',
#         'margin-right': '10mm',
#         'zoom': '1.0',  # Adjust the zoom factor if needed
#         'no-outline': None,  # Optional: Remove PDF outline
#         'print-media-type': '',  # Use print CSS media type
#         'disable-smart-shrinking': ''  # Prevent shrinking to fit the page
#     }
#     pdf = pdfkit.from_string(html,False,options=options)
#     response = HttpResponse(pdf,content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment'
#     filename = "resume.spdf"
    
#     return response 

def pdf(request, id):
    try:
        user_profile = Profile.objects.get(pk=id)
        html_string = render_to_string('resume/pdf.html', {'user_profile': user_profile})

        client = pdfcrowd.HtmlToImageClient('mudasirmattoo', '62b9d8c5a4ad213bd696dcc5a400e6f4')

        client.setOutputFormat("png")
        output_image = client.convertString(html_string)

        response = HttpResponse(output_image, content_type='image/png')
        response['Content-Disposition'] = f'attachment; filename="resume_{id}.png"'

        return response

    except pdfcrowd.Error as e:
        return HttpResponse(f"Pdfcrowd Error: {str(e)}", status=500)
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)
    
    
def download(request, id):
    return render(request, 'resume/download.html', {'id': id})

def about(request):
    return render(request, 'resume/about.html')