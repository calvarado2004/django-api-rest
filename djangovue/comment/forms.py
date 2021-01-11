from django.forms import ModelForm, Textarea
from django.forms import widgets
from .models import Comment, TypeContact
from django.core.validators import MinLengthValidator, EmailValidator

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text' : Textarea(attrs={'class':'form-input'})
        }
    '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-input'})'''
        
    def save(self,commit=True, text=" "):
        instance = super(CommentForm, self).save(commit=commit)
        
        if(text == ""):
            instance.text=text
            
        if(commit):
            instance.save()
            
from django import forms

class ContactForm(forms.Form):
        
    GENDER = ( ('M', 'Male'),
               ('F', 'Female'),
               ('N', 'Non binary'))

    
    name = forms.CharField(label="Name:",initial='John',required=True,max_length=255, min_length=4, validators=[MinLengthValidator(4)])
    email = forms.CharField(label='Email:', initial='john@mail.com', validators=[EmailValidator(message='You did not send a valid email'),MinLengthValidator(6)])
    surname = forms.CharField(label="Last Name:",initial='Doe',required=True,max_length=255, min_length=3)
    phone = forms.RegexField(label='Phone',initial='(123)123-1234',regex='\(\w{3}\)\w{3}-\w{4}',max_length=13,min_length=13)
    birth_date = forms.DateField(label='Birth Date:',initial='1900-01-20')
    type_contact = forms.ModelChoiceField(label='Type of contact', queryset=TypeContact.objects.all(),initial=2)
    vgender = forms.ChoiceField(label='Gender', choices=GENDER, initial=1)
    terms = forms.BooleanField(label='I Accept terms and conditions')
    document = forms.FileField(label='Document', required=False)

            