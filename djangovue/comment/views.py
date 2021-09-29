from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Comment, Contact
from .forms import CommentForm, ContactForm


def testview(request):
    return render(request, 'test/testview.html')

# Create your views here.
def index(request):
    comments = Comment.objects.all()
    
    return render(request, 'index.html', {'comments': comments})


def add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form.errors.as_json())
        if form.is_valid():
            form.save()
            return redirect('comment:index')
    else:
        form = CommentForm()
        
    #if(form.errors):
    #    raise ValidationError(form.errors)
        
    return render(request, 'add.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        
        if form.is_valid():
            
            if 'document' in request.FILES:
                print('Content')
            else:
                print('No file uploaded')
                
            contact = Contact()
            contact.name = form.cleaned_data['name'] 
            contact.surname = form.cleaned_data['surname'] 
            contact.phone = form.cleaned_data['phone'] 
            contact.email = form.cleaned_data['email']
            contact.birth_date = form.cleaned_data['birth_date'] 
            contact.vgender = form.cleaned_data['vgender']
            contact.type_contact = form.cleaned_data['type_contact']
            if 'document' in request.FILES:  
                contact.document = request.FILES['document']
            contact.save()
            
            messages.add_message(request, messages.INFO,'Contact saved.')
            
            return redirect('comment:contact')
        else:
            print('Not valid')

    else:
        form = ContactForm()
        
    #print(request.FILES)
    
    return render(request, 'contact.html',{'form':form})


def update(request, pk):
    
    comment = get_object_or_404(Comment, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save(commit=True)
            return redirect('comment:update', pk=comment.id)
    else:
        form = CommentForm(instance=comment)
        
    return render(request, 'update.html', {'form': form, 'comment':comment})


